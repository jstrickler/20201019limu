import boto3

from boto3_common import BUCKET_NAME

def main():
    s3 = boto3.resource('s3')  # <.>
    bucket = s3.Bucket(BUCKET_NAME)   # <.>

    print("bucket:", bucket)
    try:
        for obj in bucket.objects.filter(Prefix="words/"):  # <.>
            obj.delete()  # <.>
    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()
