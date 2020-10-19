#  Copyright (c) 2020. CJ Associates
import fileinput
import sys
from argparse import ArgumentParser
import re

parser = ArgumentParser(description="Faux grep")

parser.add_argument('-i', action="store_true", dest="ignore_case", help="ignore case")

parser.add_argument('-n', action="store_true", dest="display_name", help="display file name")

parser.add_argument('-v', action="store_true", dest="non_match", help="print non-matching lines")


parser.add_argument('search_term', help="search term (can be REGEX)")

parser.add_argument('files', nargs="*", help="files to search")

args = parser.parse_args()

search_term = re.compile(args.search_term, re.IGNORECASE if args.ignore_case else 0)
#  A ? B : C   C, Java, C#, etc
#  B if A else C  Python

print(args)

for line in fileinput.input(args.files):
    if search_term.search(line):
        if args.display_name:
            print(fileinput.filename(), end=' ')
        print(line.rstrip())
