#!/usr/bin/env python
import boto3
from boto3_common import BUCKET_NAME  # <.>


def main():
    session = boto3.session.Session() # <.>
    region = session.region_name  # <.>

    s3 = boto3.client('s3')  # <.>

    config = {'LocationConstraint': region}  # <.>

    try:
        client_response = s3.create_bucket(  # <.>
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration=config
        )
    except Exception as err:
        print(err)
    else:
        print(client_response)

if __name__ == '__main__':
    main()
