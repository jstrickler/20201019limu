import boto3

def lambda_build(function_name):
  client = boto3.client('lambda')

  create_lambda_function = client.create_function(
      FunctionName=function_name,
      Runtime='python3.7',
      Role='arn:aws:iam::567917629100:role/cja_lambda_role',
      Handler='{}.lambda_handler'.format('lambda_build'),
      Description='Start a virtual machine',
      Code = {'S3Bucket':'cja-tech-demo', 'S3Key':f'lambdas/{function_name}'}
  )

if __name__ == '__main__':
    lambda_build('aws_lambda_hello.py')
