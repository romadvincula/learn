def to_files(df, target_dir, file_format):
    df.coalesce(16) \
        .write \
        .partitionBy('year', 'month', 'dayofmonth') \
        .mode('append') \
        .format(file_format) \
        .save(target_dir)