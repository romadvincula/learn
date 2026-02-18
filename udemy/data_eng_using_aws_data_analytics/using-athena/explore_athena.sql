SELECT * FROM "retail_db"."orders" limit 10;

SELECT COUNT(*) FROM retail_db.orders;

CREATE DATABASE myretail;


CREATE EXTERNAL TABLE `myretail`.`orders`(
  `order_id` int COMMENT 'from deserializer', 
  `order_date` string COMMENT 'from deserializer', 
  `order_customer_id` int COMMENT 'from deserializer', 
  `order_status` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'paths'='order_customer_id,order_date,order_id,order_status') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://romadv-itv-retail/myretail/orders/'
TBLPROPERTIES (
  'CRAWL_RUN_ID'='f3bbe90a-5ad2-45aa-8db2-e8cff6707044', 
  'CrawlerSchemaDeserializerVersion'='1.0', 
  'CrawlerSchemaSerializerVersion'='1.0', 
  'UPDATED_BY_CRAWLER'='Retail Crawler', 
  'averageRecordSize'='1048', 
  'classification'='json', 
  'compressionType'='none', 
  'objectCount'='1', 
  'recordCount'='7134', 
  'sizeKey'='7477339', 
  'typeOfData'='file');
 
  
  SELECT * FROM myretail.orders LIMIT 10;
  
  
INSERT INTO myretail.orders
SELECT * FROM retail_db.orders;

DROP TABLE myretail.orders;

SELECT COUNT(*) FROM myretail.orders;

CREATE TABLE myretail.order_items
AS
SELECT * FROM retail_db.order_items;

SELECT * FROM myretail.order_items LIMIT 5;

--DROP TABLE myretail.order_items

CREATE TABLE myretail.order_items
WITH (
    format = 'TEXTFILE',
    external_location = 's3://romadv-itv-retail/myretail/order_items/',
    field_delimiter = ','
)
AS
SELECT * FROM retail_db.order_items;

