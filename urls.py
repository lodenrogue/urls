#! /usr/bin/env python3

# Extract urls from stdin

import re
import sys


def extract_urls(line):
    url_pattern = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    return re.findall(url_pattern, line)


def main():
    for line in sys.stdin:
        urls = extract_urls(line)
        for url in urls:
            print(url)


if __name__ == '__main__':
    main()

