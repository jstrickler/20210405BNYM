import sys
import fileinput
import re
from argparse import ArgumentParser

# parse the command line (i.e., sys.argv)
parser = ArgumentParser(description="Faux grep")
parser.add_argument('-i', action="store_true",
                    dest="ignore_case", help="ignore case")
parser.add_argument('-f', action="store_true",
                    dest="show_file_name", help="show file names")
parser.add_argument('search_term', help="Text to find",
                    metavar="search term")
parser.add_argument('files', nargs="*", help="Files to search")

args = parser.parse_args()  # parse sys.argv

re_flag = re.I if args.ignore_case else 0  # 0 is "no flags
search_pattern = re.compile(args.search_term, re_flag)

for raw_line in fileinput.input(args.files):
    if search_pattern.search(raw_line):
        if args.show_file_name:
            print(fileinput.filename(), end=' ')
        line = raw_line.rstrip()
        print(line)

