import re
from pyspark import SparkConf, SparkContext

def normalizeWords(text):
    return re.compile(r'\W+', re.UNICODE).split(text.lower())

conf = SparkConf().setMaster("local").setAppName("WordCount")
sc = SparkContext(conf = conf)

input = sc.textFile("data/book.txt")
words = input.flatMap(normalizeWords)

# make each word to (word, 1) then group by each word and add the 1s together
wordCounts = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
# flip key-value to value-key then sort
wordCountsSorted = wordCounts.map(lambda x: (x[1], x[0])).sortByKey()
# execute DAGs, this will return from RDD to python object
results = wordCountsSorted.collect()

for result in results:
    count = str(result[0])
    word = result[1].encode('ascii', 'ignore')
    if (word):
        print(word.decode() + ":\t\t" + count)
