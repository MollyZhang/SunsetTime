import pandas as pd
from datetime import datetime
import sys
import calendar
import pickle
from pprint import pprint as pp
DATAFILE = "sunrise_sunset_santa_cruz_2016"


def main():
    time_dict = {}
    f = open(DATAFILE, "r")
    months = list(calendar.month_abbr)[1:]
    for line in f:
        if line.strip() in months:
            months.pop(0)
            month_num = 12-len(months)
            day = 1
            time_dict[month_num] = {}
        else:
            time = tuple(line.strip().split(" "))
            time_dict[month_num][day] = time
            day += 1
    f.close()
    pp(time_dict)

    # think: shouldn't I save the entire year as a list of tuples of datetime?


if __name__ == '__main__':
    main()