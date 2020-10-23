import boto3

WORD_BUCKET_NAME = 'cja-tech-demo'

def main():
    s3 = boto3.resource('s3')  # <.>

    bucket = s3.Bucket(WORD_BUCKET_NAME)  # <.>

    presidents = []
    for obj in bucket.objects.filter(Prefix="president/"):  # <.>
        bin_potus = obj.get()['Body'].read()
        fields = bin_potus.decode().split(';')
        fields[0] = int(fields[0]) # make term an int for sorting
        presidents.append(fields)

    for term, first_name, last_name, party in sorted(presidents):
        print(term, first_name, last_name, party)

if __name__ == '__main__':
    main()

