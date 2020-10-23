#!/usr/bin/env python
import random
import boto3
from boto3_common import BUCKET_NAME


def main():
    s3 = boto3.resource('s3')  # <1>

    values = 'one two three four five'.split()

    for value in values:
        obj = s3.Object(BUCKET_NAME, "dumbkey")
        obj.put(Body=value + '\n')

if __name__ == '__main__':
    main()
