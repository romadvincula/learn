from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.appName("MostObscureSuperhero").getOrCreate()

schema = StructType([ \
                     StructField("id", IntegerType(), True), \
                     StructField("name", StringType(), True)])

names = spark.read.schema(schema).option("sep", " ").csv("data/Marvel-names.txt")

lines = spark.read.text("data/Marvel-graph.txt")

# Small tweak vs. what's shown in the video: we trim each line of whitespace as that could
# throw off the counts.
connections = lines.withColumn("id", func.split(func.trim(func.col("value")), " ")[0]) \
    .withColumn("connections", func.size(func.split(func.trim(func.col("value")), " ")) - 1) \
    .groupBy("id").agg(func.sum("connections").alias("connections"))

# find the minimum number of connections in the dataset
minimumConnectionCount = connections.agg(func.min("connections")).first()[0]

# filter only those with the minimum number of connections
minConnection = connections.filter(connections.connections == minimumConnectionCount)

# join with names dataframe
minConnectionNamed = minConnection.join(names, "id")

minConnectionNamed.show()

# Stop the session
spark.stop()
