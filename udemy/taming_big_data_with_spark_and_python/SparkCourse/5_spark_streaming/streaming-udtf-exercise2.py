import random
import os
import re

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf, udtf
from pyspark.sql.types import StringType, IntegerType

TWEETS_FILE = "./bluesky.jsonl"

spark = SparkSession.builder \
    .appName("BlueskyStream") \
    .getOrCreate()

@udf(StringType())
def get_random_log_line():
    """Returns a random line from the log file without reading the entire file into memory."""
    try:
        if not os.path.exists(TWEETS_FILE):
            return None  # Handle the case where the log file is missing

        file_size = os.path.getsize(TWEETS_FILE)
        if file_size == 0:
            return None  # Handle empty file scenario

        with open(TWEETS_FILE, "r") as lf:
            while True:
                random_position = random.randint(0, file_size - 1)  # Pick a random position
                lf.seek(random_position)  # Jump to that position
                lf.readline()  # Discard partial line (move to next full line)
                line = lf.readline().strip()  # Read a full line
                
                if line:  # Ensure we get a valid line
                    return line

    except Exception as e:
        print(str(e))
        return None

@udtf(returnType="hashtag: string")
class HashtagExtractor:
    def eval(self, text: str):
        """ get hashtags from text """
        if text:
            hashtags = re.findall(r"#\w+", text)
            for ht in hashtags:
                yield (ht, )

spark.udtf.register("extract_hashtags", HashtagExtractor)

rate_df = spark.readStream \
    .format("rate") \
    .option("rowsPerSecond", 50) \
    .load()

tweetLines = rate_df.withColumn("value", get_random_log_line())

tweetLines.createOrReplaceTempView("raw_tweets")

tweetsDF = spark.sql("""
    SELECT value,
    hashtag
    FROM raw_tweets, LATERAL extract_hashtags(value)
""")

tweetsDF.createOrReplaceTempView("hashtags")

topHashtags = spark.sql("""
    SELECT hashtag,
    COUNT(*) as count
    FROM hashtags
    WHERE hashtag IS NOT NULL
    GROUP BY hashtag
    ORDER BY count DESC
    LIMIT 10
""")

query = (topHashtags.writeStream \
         .outputMode("complete") \
         .format("console") \
         .queryName("top_hashtags")
         .start())

query.awaitTermination()

spark.stop()