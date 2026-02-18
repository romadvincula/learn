from util import get_spark_session


def from_files(spark, data_dir, file_pattern, file_format):
    df = spark.read \
        .format(file_format) \
        .load(f'{data_dir}/{file_pattern}')
    return df

if __name__ == "__main__":
    spark = get_spark_session('DEV', 'Read data')
    df = from_files(spark,
                    data_dir='data/itv-github/landing/ghactivity',
                    file_pattern='*.json.gz',
                    file_format='json')
    df.show()
    spark.stop()