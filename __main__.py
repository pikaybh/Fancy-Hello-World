from fancy_print import FancyPrint

import argparse

# Args
parser = argparse.ArgumentParser()
parser.add_argument("--sentence", "-S", type=str, default="Hello, World!", help="Type something you'ld like to print fancy.")
parser.add_argument("--interval", "-I", type=float, default=.05, help="Time interval. (default: 0.05)")
args = parser.parse_args()

# Main
if __name__ == "__main__":
    fancy = FancyPrint(duration=args.interval)
    fancy(args.sentence)