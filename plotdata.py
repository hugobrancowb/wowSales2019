from datetime import datetime, date, timedelta
# import numpy as np

def plot(allSales):
    calendar = create_list_of_days(allSales)

def create_list_of_days(allSales):
    calendar_full = [datetime.today()] * len(allSales)
    print("")
    for i,entry in enumerate(allSales):
        calendar_full[i] = which_day(entry.time)

    calendar_full.sort()
    calendar = fill_list_of_days(calendar_full)

    for calendar_day in calendar:
        print("{}".format(calendar_day.isoformat()))
    
    return calendar

def fill_list_of_days(calendar_full):
    start = calendar_full[0]
    end = calendar_full[len(calendar_full) - 1]
    dia = start
    calendar = []

    while(dia != end):
        calendar.append(dia)
        dia = dia + timedelta(days=1)
    
    return calendar

def which_day(string):
    t = string.split("-")
    for j in range(0,3):
            t[j] = int(t[j])
    return date(t[0], t[1], t[2])