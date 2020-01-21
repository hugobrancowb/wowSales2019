from datetime import datetime, date, timedelta
import numpy as np

def plot(allSales):
    calendar_full = [datetime.today()] * len(allSales)
    print("")
    for i,entry in enumerate(allSales):
        t = entry.time
        t = t.split("-")
        for j in range(0,3):
            t[j] = int(t[j])
        calendar_full[i] = date(t[0], t[1], t[2])

    calendar_full.sort()
    calendar = list_of_days(calendar_full)

    # calendar = np.unique(calendar_full)
    for calendar_day in calendar:
        print("{}".format(calendar_day.isoformat()))

