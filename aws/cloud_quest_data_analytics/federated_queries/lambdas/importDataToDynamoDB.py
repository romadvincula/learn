import json, boto3, os
import csv, codecs, logging

import urllib3
http = urllib3.PoolManager()
SUCCESS = "SUCCESS"
FAILED = "FAILED"

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb = boto3.resource('dynamodb')
s3 = boto3.resource('s3')

bucket = os.environ['sourceBucket']
key = os.environ['key']
tableName = os.environ['tableName']

def lambda_handler(event, context):

    logger.info(json.dumps(event))
    responseData = {'status': 'NONE'}

    if event['RequestType'] == 'Create':

        logger.info("File name is: " + key)
        
        try:
            csv_file = s3.Object(bucket, key)
            csv_content = csv_file.get()['Body'].read().decode('utf-8').splitlines(True)
            logger.info("S3 Object opened successfully")
            responseData['status'] = 'OPENED'
            send(event, context, SUCCESS, responseData ,physicalResourceId=event['LogicalResourceId'])
        except Exception as error:
            logger.info(error)
            logger.info("S3 Object could not be opened. Check environment variable.")
            responseData['status'] = f'FAILED TO Open S3. ERROR {error}'
            send(event, context, SUCCESS, responseData ,physicalResourceId=event['LogicalResourceId'])

        write_to_dynamo(csv.DictReader(csv_content))
            
        return {
            'statusCode': 200,
            'body': json.dumps('Uploaded to DynamoDB Table'),
        }

    elif event['RequestType'] == 'Delete':
        logger.info('Delete in Progress')
        responseData['status'] = f'Delete in Progress.'
        send(event, context, SUCCESS, responseData ,physicalResourceId=event['LogicalResourceId'])


def write_to_dynamo(content):
    
    # logger.info(json.dumps(event))
    responseData = {'status': 'NONE'}
    
    try:
        table = dynamodb.Table(tableName)
    except Exception as error:
        logger.info(error),
        logger.info("Error loading DynamoDB table in write to dynamo function.")
        responseData['status'] = f'Delete in Progress.'
    
    try:
        with table.batch_writer() as batch:
            for row in content:
                batch.put_item(Item={
                    'TicketNumber': row['TicketNumber'],
                    'EmailAddress': row['EmailAddress'],
                    'Prefix': row['Prefix'],
                    'Name': row['Name'],
                    'PhoneNumber': row['PhoneNumber'],
                    'Neighborhood': row['Neighborhood'],
                    'City': row['City'],
                    'RequestType': row['RequestType']
                    }
                )
    except Exception as error:
        logger.info(error)
        logger.info("Error executing batch_writer")
        responseData['status'] = f'Batch writer failed.'

def send(event, context, responseStatus, responseData, physicalResourceId=None, noEcho=False, error=None):
    responseUrl = event['ResponseURL']

    logger.info(responseUrl)

    responseBody = {}
    responseBody['Status'] = responseStatus
    if error is None: 
        responseBody['Reason'] = 'See the details in CloudWatch Log Stream: ' + context.log_stream_name + ' LogGroup: ' + context.log_group_name
    else:
        responseBody['Reason'] = error
    responseBody['PhysicalResourceId'] = physicalResourceId or context.log_stream_name
    responseBody['StackId'] = event['StackId']
    responseBody['RequestId'] = event['RequestId']
    responseBody['LogicalResourceId'] = event['LogicalResourceId']
    responseBody['NoEcho'] = noEcho
    responseBody['Data'] = responseData

    json_responseBody = json.dumps(responseBody)

    print("Response body:\n" + json_responseBody)

    headers = {
        'content-type' : '',
        'content-length' : str(len(json_responseBody))
    }
    try:
        response = http.request('PUT',responseUrl,body=json_responseBody.encode('utf-8'),headers=headers)
        print("Status code: " + response.reason)
    except Exception as e:
        print("send(..) failed executing requests.put(..): " + str(e))