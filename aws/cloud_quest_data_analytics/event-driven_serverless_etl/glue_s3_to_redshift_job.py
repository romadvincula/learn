import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1762402872243 = glueContext.create_dynamic_frame.from_catalog(database="toll-raw-db", table_name="landing_bucket_019964248372_us_east_1", transformation_ctx="AmazonS3_node1762402872243")

# Script generated for node Change Schema
ChangeSchema_node1762402933444 = ApplyMapping.apply(frame=AmazonS3_node1762402872243, mappings=[("transaction_id", "int", "transaction_id", "bigint"), ("transaction_date", "string", "transaction_date", "string"), ("toll_booth", "string", "toll_booth", "string"), ("vehicle_make", "string", "vehicle_make", "string"), ("vehicle_category", "string", "vehicle_category", "string"), ("transaction_amount", "double", "transaction_amount", "double")], transformation_ctx="ChangeSchema_node1762402933444")

# Script generated for node Amazon Redshift
AmazonRedshift_node1762403035384 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1762402933444, connection_type="redshift", connection_options={"redshiftTmpDir": "s3://staging-bucket-019964248372-us-east-1", "useConnectionProperties": "true", "dbtable": "public.toll_table", "connectionName": "redshift_conn", "preactions": "CREATE TABLE IF NOT EXISTS public.toll_table (transaction_id VARCHAR, transaction_date VARCHAR, toll_booth VARCHAR, vehicle_make VARCHAR, vehicle_category VARCHAR, transaction_amount DOUBLE PRECISION);"}, transformation_ctx="AmazonRedshift_node1762403035384")

job.commit()