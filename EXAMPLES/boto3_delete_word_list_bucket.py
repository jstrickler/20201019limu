#!/usr/bin/env python
import boto3
from boto3_common import BUCKET_NAME


def main():
    s3 = boto3.client('s3')  # <.>

    try:
        client_response = s3.delete_bucket(Bucket=BUCKET_NAME)  # <.>
    except Exception as err:
        print(err)
    else:
        print(client_response)

if __name__ == '__main__':
    main()
