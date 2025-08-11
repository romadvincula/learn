from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType


spark = SparkSession.builder.appName("CustomerSpendDF").getOrCreate()

schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("item_id", IntegerType(), True),
    StructField("spend", FloatType(), True)
])

# read file as dataframe
df = spark.read.schema(schema).csv("data/customer-orders.csv")
df.printSchema()

# select only the relevant cols and 
customerSpend = df.select("customer_id", "spend")
customerSpend.show(10)

# group by customer and sum their spend then sort by descending
spendByCustomer = customerSpend.groupBy("customer_id")\
    .agg(func.round(func.sum("spend"), 2).alias("sum_spend"))\
    .sort("sum_spend", ascending=False)

# show results
spendByCustomer.show(spendByCustomer.count())

spark.stop()

