from util import get_spark_session
from read import from_files
import os
from process import transform
from write import to_files


def main():
    env = os.environ.get('ENVIRON')
    src_dir = os.environ.get('SRC_DIR')
    src_file_pattern = f"{os.environ.get('SRC_FILE_PATTERN')}-*"
    src_file_format = os.environ.get('SRC_FILE_FORMAT')
    target_dir = os.environ.get('TARGET_DIR')
    target_file_format = os.environ.get('TARGET_FILE_FORMAT')

    spark = get_spark_session(env, 'Github Activity - Getting Started')
    df = from_files(spark,
                    data_dir=src_dir,
                    file_pattern=src_file_pattern,
                    file_format=src_file_format)
    df_transformed = transform(df)
    to_files(df_transformed, target_dir, target_file_format)
    df_transformed.printSchema()
    df_transformed.select('repo.*',
                          'created_at',
                          'year',
                          'month',
                          'dayofmonth').show()

    spark.stop()

if __name__ == '__main__':
    main()

