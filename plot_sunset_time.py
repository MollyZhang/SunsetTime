import pandas as pd
from datetime import datetime
import sys

DATAFILE = "sunrise_sunset_santa_cruz_2016"
Header = []


def main():
    df = pd.read_csv(DATAFILE, sep="  ")
    print df.columns

if __name__ == '__main__':
    main()