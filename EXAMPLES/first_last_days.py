from datetime import date
from dateutil.relativedelta import relativedelta  # <.>

def first_last_days(year):
    first_last_pairs = []
    for month in range(1,13):
        first_day = date(year, month, 1)
        last_day = first_day + relativedelta(day=1, months=1, days=-1)  # <.>
        first_last_pairs.append((first_day, last_day))  # <.>
    return first_last_pairs

if __name__ == '__main__':

    pairs = first_last_days(2020)

    for first, last in pairs:
        fwd = first.strftime("%A")  # <.>
        lwd = last.strftime("%A")  # <.>
        print("{} {:9s} {} {:9s}".format(first, fwd, last, lwd))
    print()
