import matplotlib.pyplot as plt
from datefunctions import create_list_of_days, str_to_day
# import numpy as np

def plot(allSales):
    calendar = create_list_of_days(allSales)
    income = count_balance(allSales, calendar)
    plt.figure()
    plt.plot(calendar, income) 
    plt.show()

def count_balance(allSales, calendar):
    balance = [0] * len(calendar)

    for each_sale in allSales:
        i = calendar.index(str_to_day(each_sale.time))
        balance[i] += int(each_sale.quantity) * int(each_sale.price)
    
    print("BALANCE:")
    for i in range(0, len(calendar)):
        print("{}\t{}".format(calendar[i].isoformat(), balance[i]))
    
    return balance