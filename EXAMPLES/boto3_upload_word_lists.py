#!/usr/bin/env python
import random
import boto3
from boto3_common import BUCKET_NAME


def main():
    s3 = boto3.resource('s3')  # <.>


    word_lists = {}  # <.>
    with open('../DATA/words.txt') as words_in:  # <.>
        for raw_line in words_in:
            word = raw_line.rstrip()
            first_letter = word[0]
            if first_letter not in word_lists:
                word_lists[first_letter] = []
            word_lists[first_letter].append(word)

    for letter, all_words in word_lists.items():
        data = ':'.join(sorted(random.sample(all_words, 100 )))  # <.>
        key = f'words/{letter}'
        obj = s3.Object(BUCKET_NAME, key)  # <.>
        obj.put(Body=data)  # <.>

if __name__ == '__main__':
    main()
