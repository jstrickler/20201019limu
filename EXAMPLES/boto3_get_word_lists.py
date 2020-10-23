#!/usr/bin/env python
import uuid
import boto3
from boto3_common import BUCKET_NAME


def main():
    s3 = boto3.resource('s3')  # <.>

    bucket = s3.Bucket(BUCKET_NAME)  # <.>

    for obj in bucket.objects.filter(Prefix='words/'):  # <.>
        print(obj.key, end=' ')  # <.>
        print("RAW OBJ:")
        print(obj.get())
        print('-' * 60)
        raw_data = obj.get()['Body'].read()  # <.>
        data = raw_data.decode()  # <.>
        print(data)

if __name__ == '__main__':
    main()

