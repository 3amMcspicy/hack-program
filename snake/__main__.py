#!/usr/bin/env python3


"""
Command line argparser for snake
"""

import argparse
from snake import isit_snakes
from snake import snakeSensei

def parse_arguments():
    """
    parses command line arguments using argparse
    """

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--today",
        action="store_true",
        help="print if today is the anniversay of snakes game"
    )
    parser.add_argument(
        "--yet",
        action="store_true",
        help="print if it is the anniversay of snakes game yet"
    )
    parser.add_argument(
        "--celeb",
        action="store_true",
        help="Returns a dataframe of celebrity and whether they could've played the game"
    )
    args = parser.parse_args()
    if args.today and args.yet:
        raise SystemExit("please choose one option only")

    return args

def run_program():
    args = parse_arguments()
    if args.today:
        isit_snakes("today")
    elif args.yet:
        isit_snakes("yet")
    elif args.celeb:
         p = snakeSensei()
         p.run()
    else:
        print("Please enter either one of the options: --today, --yet, --celeb after snake" )

