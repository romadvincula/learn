from datetime import datetime as dt
from datetime import timedelta as td
import requests, os, boto3
from botocore.errorfactory import ClientError


def _get_client():
    client = boto3.client('s3', verify=False) if os.environ.get('ENVIRON') == 'DEV' else boto3.client('s3')
    return client

def get_prev_file_name(bucket_name, file_prefix, bookmark_file, baseline_file):
    environ = os.environ.get('ENVIRON')
    if environ == 'DEV':
        os.environ.setdefault('AWS_PROFILE', 'itvgithub')
    s3_client = _get_client()
    try:
        bookmark_file = s3_client.get_object(
            Bucket=bucket_name,
            Key=f'{file_prefix}/{bookmark_file}'
        )
        prev_file = bookmark_file['Body'].read().decode('utf-8')
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            prev_file = baseline_file
        else:
            raise
    return prev_file

def get_next_file_name(prev_file):
    dt_part = prev_file.split('.')[0]
    next_file = f"{dt.strftime(dt.strptime(dt_part, '%Y-%M-%d-%H') + td(hours=1), '%Y-%M-%d-%-H')}.json.gz"
    return next_file

def upload_bookmark(bucket, file_prefix, bookmark_file, file_name):
    client = _get_client()
    client.put_object(
        Bucket=bucket,
        Key=f"{file_prefix}/{bookmark_file}",
        Body=file_name.encode('utf-8')
    )

if __name__ == "__main__":
    next_file = '2025-12-17-20.json.gz'
    # for i in range(24):
    while True:
        res = requests.get(f"https://data.gharchive.org/{next_file}", verify=False)
        if res.status_code != 200:
            break
        print(f"Status code for {next_file} is {res.status_code}")
        dt_part = next_file.split('.')[0]
        next_file = f"{dt.strftime(dt.strptime(dt_part, '%Y-%M-%d-%H') + td(hours=1), '%Y-%M-%d-%-H')}.json.gz"
        # print(next_file)

