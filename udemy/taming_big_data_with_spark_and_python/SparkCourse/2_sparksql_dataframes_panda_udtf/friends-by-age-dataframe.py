from pyspark.sql import SparkSession, functions as func


spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

lines = spark.read.option("header", "true").option("InferSchema", "true")\
    .csv("data/fakefriends-header.csv")

# remove unused columns to save resources
people = lines.select("age", "friends")

print("Show Schema for people")
people.printSchema()

print("Average Number of friends by age using Dataframe functions")
people.groupBy("age").avg("friends").show()

print("Sorted")
people.groupBy("age").agg(func.round(func.avg("friends"), 2).alias("friends_average"))\
    .sort("age").show()

print("Average Number of friends by age using SparkSQL")
people.createOrReplaceTempView("people")
friendsByAge = spark.sql("""
                         SELECT 
                            age, 
                            ROUND(AVG(friends),2) AS friends_average 
                         FROM people 
                         GROUP BY age 
                         ORDER BY age
                         """)
for row in friendsByAge.collect():
    print(row)

spark.stop

