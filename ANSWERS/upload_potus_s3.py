import boto3
import pickle
from president import President

WORD_BUCKET_NAME = 'cja-tech-demo'

def main():
    s3 = boto3.resource('s3')  # <1>

    for i in range(1, 46):
        p = President(i)
        data = f"{i};{p.first_name};{p.last_name};{p.party}"
        bindata = data.encode()

        obj = s3.Object(WORD_BUCKET_NAME, f"president/{i}")
        obj.put(Body=bindata)

if __name__ == '__main__':
    main()
