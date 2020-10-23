import json
import boto3

DEST_BUCKET = "cja-tech-demo2"

s3 = boto3.client('s3')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))

    # get the object from the event
    s3_info = event['Records'][0]['s3']

    bucket = s3_info['bucket']['name']
    obj_key = s3_info['object']['key']

    try:
        response = s3.get_object(Bucket=bucket, Key=obj_key)
        # print("response:", response)
        obj_data = response['Body'].read()

        s3.put_object(Bucket=DEST_BUCKET, Key=obj_key, Body=obj_data.upper())
    except Exception as e:
        print(e)
        raise e

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from CopyWordList',
        })
    }
