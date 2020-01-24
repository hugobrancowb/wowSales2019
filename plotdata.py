import matplotlib.pyplot as plt
from datefunctions import create_list_of_days, str_to_day
from models import Data

def plot(data: Data):
    calendar = create_list_of_days(data.sales)
    income = count_balance(data.sales, calendar)
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