import argparse
import sys

sys.path.append("..")

from bade.speedconversion import kph_to_mph

# Adding comment in BitBucket to do a git pull
def read_arguments():
    parser = argparse.ArgumentParser(description='''Speed conversion''', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--speed",
                        type=str,
                        required=True,
                        help="speed")
    return parser


# Main section
if __name__ == "__main__":
    parser = read_arguments()
    args = parser.parse_args()
    speed_kph = float(args.speed)
    speed_mph = kph_to_mph(speed_kph)
    print(f"{speed_kph} kph = {speed_mph} mph")