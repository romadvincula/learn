from pyspark.sql import functions as f


def transform(df):
    new_df = df.withColumn('year', f.year('created_at')) \
        .withColumn('month', f.month('created_at')) \
        .withColumn('dayofmonth', f.dayofmonth('created_at'))
    return new_df