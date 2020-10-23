#!/usr/bin/env python
import random
import boto3
from boto3_common import BUCKET_NAME

FOLDERS_LEVEL_1 = ['spam', 'ham', 'toast']
FOLDERS_LEVEL_2 = ['foo', 'bar']
FOLDERS_LEVEL_3 = ['Nellie', 'Andy']


def main():
    s3 = boto3.resource('s3')  # <1>

    data_gen = get_data()

    for l1 in FOLDERS_LEVEL_1:
        for i in range(2):
            for l2 in FOLDERS_LEVEL_2:
                for j in range(2):
                    for l3 in FOLDERS_LEVEL_3:
                        for k in range(2):
                            key = '/'.join([l1, l2, l3])
                            data = next(data_gen)
                            print(key, data)
                            obj = s3.Object(BUCKET_NAME, key)
                            obj.put(Body=data)

def get_data():
    word_lists = {}  # <3>
    with open('../DATA/words.txt') as words_in:
        for raw_line in words_in:
            word = raw_line.rstrip()  # <4>
            first_letter = word[0]
            if first_letter not in word_lists:  # <5>
                word_lists[first_letter] = []  # <6>
            word_lists[first_letter].append(word)

    while True:
        for letter, all_words in word_lists.items():
            data = ':'.join(sorted(random.sample(all_words, 10 )))
            yield data


if __name__ == '__main__':
    main()
