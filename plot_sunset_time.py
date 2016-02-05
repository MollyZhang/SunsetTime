import pandas as pd
from datetime import datetime
import sys
import calendar
import pickle
from pprint import pprint as pp
import time
from matplotlib import pyplot as plt



DATAFILE = "sunrise_sunset_santa_cruz_2016"


def main():
    year_2016 = get_data()
    df = pd.DataFrame(year_2016, columns = ["Sunrise", "Sunset"])
    sunrise_y = df["Sunrise"]
    sunset_y = df['Sunset']
    plt.plot(range(1,367), list(sunrise_y))
    plt.plot(range(1,367), list(sunset_y))
    plt.show()

def get_data():
    time_dict = {}
    f = open(DATAFILE, "r")
    months = list(calendar.month_abbr)[1:]
    for line in f:
        if line.strip() in months:
            this_month_abbrev = line.strip()
            months.pop(0)
            month_num = 12-len(months)
            day = 1
            time_dict[month_num] = {}
        else:
            [sunrise, sunset] = line.strip().split(" ")
            sunrise_in_minute = int(sunrise[0:2]) * 60 + int(sunrise[2:])
            sunset_in_minute = int(sunset[0:2]) * 60 + int(sunset[2:])
            time_dict[month_num][day] = (sunrise_in_minute, sunset_in_minute)
            day += 1
    f.close()
    # think: shouldn't I save the entire year as a list of tuples of datetime?
    year_2016 = []
    for month in sorted(time_dict.keys()):
        for key in sorted(time_dict[month]):
            year_2016.append(time_dict[month][key])

    return year_2016



if __name__ == '__main__':
    main()