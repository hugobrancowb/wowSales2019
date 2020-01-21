from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt
# import numpy as np

def plot(allSales):
    calendar = create_list_of_days(allSales)
    income = count_balance(allSales, calendar)
    plt.figure()
    plt.plot(calendar, income) 
    plt.show()

def create_list_of_days(allSales):
    calendar_full = [datetime.today()] * len(allSales)
    print("")
    for i,entry in enumerate(allSales):
        calendar_full[i] = which_day(entry.time)

    calendar_full.sort()
    calendar = fill_list_of_days(calendar_full)
    
    return calendar

def fill_list_of_days(calendar_full):
    start = calendar_full[0]
    end = calendar_full[len(calendar_full) - 1]
    dia = start
    calendar = []

    while(dia <= end):
        calendar.append(dia)
        dia = dia + timedelta(days=1)
    
    return calendar

def which_day(string):
    t = string.split("-")
    for j in range(0,3):
            t[j] = int(t[j])
    return date(t[0], t[1], t[2])

def count_balance(allSales, calendar):
    balance = [0] * len(calendar)

    for each_sale in allSales:
        i = calendar.index(which_day(each_sale.time))
        balance[i] += int(each_sale.quantity) * int(each_sale.price)
    
    print("BALANCE:")
    for i in range(0, len(calendar)):
        print("{}\t{}".format(calendar[i].isoformat(), balance[i]))
    
    return balance