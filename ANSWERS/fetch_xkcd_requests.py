#!/usr/bin/env python

import sys

import requests

url = 'https://imgs.xkcd.com/comics/python.png'
saved_pdf_file = 'xkcd.png'

try:
    response = requests.get(url, verify=False)
except requests.HTTPError as err:
    print("Unable to open URL:", err)
    sys.exit(1)

if response.status_code == requests.codes.OK:
    with open(saved_pdf_file, 'wb') as xkcd_out:
        xkcd_out.write(response.content)

