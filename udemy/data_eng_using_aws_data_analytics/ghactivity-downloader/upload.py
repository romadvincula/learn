import os
import boto3
import requests


def get_client():
    environ = os.environ.get('ENVIRON')
    client = boto3.client('s3', verify=False) if environ == 'DEV' else boto3.client('s3')
    return client

def upload_to_s3(body, bucket, file):
    s3_client = get_client()
    res = s3_client.put_object(
        Bucket=bucket,
        Key=file,
        Body=body
    )
    return res

if __name__ == '__main__':
    os.environ.setdefault('AWS_DEFAULT', 'itvgithub')
    file = '2021-01-29-0.json.gz'
    res = requests.get(f"https://data.gharchive.org/{file}", verify=False)

    upload_res = upload_to_s3(
        body=res.content,
        bucket='romadv-itv-github',
        file='2021-01-29-0.json.gz'
    )
    print(upload_res)


