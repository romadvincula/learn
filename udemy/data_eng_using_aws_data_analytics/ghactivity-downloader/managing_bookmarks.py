from datetime import datetime as dt
from datetime import timedelta as td
import requests, boto3, os
from botocore.errorfactory import ClientError


baseline_file = '2025-12-17-21.json.gz'
os.environ.setdefault('AWS_PROFILE', 'itvgithub')
s3_client = boto3.client('s3')

while True:
   try:
       bookmark_file = s3_client.get_object(
           Bucket='romadv-itv-github',
           Key='sandbox/bookmark'
       )
       prev_file = bookmark_file['Body'].read().decode('utf-8')
   except ClientError as e:
       if e.response['Error']['Code'] == 'NoSuchKey':
           prev_file = baseline_file
       else:
           raise
 
   dt_part = prev_file.split('.')[0]
   next_file = f"{dt.strftime(dt.strptime(dt_part, '%Y-%M-%d-%H') + td(hours=1), '%Y-%M-%d-%-H')}.json.gz"
   res = requests.get(f'https://data.gharchive.org/{next_file}', verify=False)
   print(f'https://data.gharchive.org/{next_file}')
   if res.status_code != 200:
       break
   print(f'The status code for {next_file} is {res.status_code}')
   bookmark_contents = next_file
   s3_client.put_object(
       Bucket='romadv-itv-github',
       Key='sandbox/bookmark',
       Body=bookmark_contents.encode('utf-8')
   )
   
# os.environ.setdefault('AWS_PROFILE', 'itvgithub')
# s3_client = boto3.client('s3')
# bookmark_contents = '2025-12-18-0.json.gz'

# # s3_client.put_object(
# #     Bucket='romadv-itv-github',
# #     Key='sandbox/bookmark',
# #     Body=bookmark_contents.encode('utf-8')
# #     )

# try:
#     bookmark_file = s3_client.get_object(
#         Bucket='romadv-itv-github',
#         Key='sandbox/bookmark'
#     )
#     prev_file = bookmark_file['Body'].read().decode('utf-8')
#     print(prev_file)
# except ClientError as e:
#     if e.response['Error']['Code'] == 'NoSuchKey':
#         # Catch exception
#         # prev_file = baseline_file
#         print('no such file')
#         pass
#     else:
#         raise

