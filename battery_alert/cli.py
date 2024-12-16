import argparse
from .core import check_battery

def parse_args():
    parser = argparse.ArgumentParser(description="Battery monitoring tool")
    parser.add_argument("--low", type=int, default=20, help="Low battery level (%)")
    parser.add_argument("--high", type=int, default=82, help="High battery level (%)")
    parser.add_argument("--interval", type=int, default=60, help="Check interval in seconds")
    return parser.parse_args()

def main():
    args = parse_args()
    check_battery(args.low, args.high, args.interval)
