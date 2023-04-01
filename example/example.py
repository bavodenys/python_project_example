import argparse
import sys

sys.path.append("..")

from bade.speedconversion import kph_to_knots

def read_arguments():
    parser = argparse.ArgumentParser(description='''Windspeed conversion''', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--windspeed",
                        type=str,
                        required=True,
                        help="windspeed")
    return parser


# Main section
if __name__ == "__main__":
    parser = read_arguments()
    args = parser.parse_args()
    windspeed_kph = float(args.windspeed)
    windspeed_knots = kph_to_knots(windspeed_kph)
    print(f"{windspeed_kph} kph = {windspeed_knots} kt")