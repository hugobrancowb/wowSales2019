from datefunctions import create_list_of_days, str_to_day
from models import Data
#import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot(data: Data):
    calendar = create_list_of_days(data.sales)
    [income, purchases] = count_balance(data.sales, calendar)
    
    plt.figure()
    plt.plot(calendar, income, 'b', linewidth = 1) 
    plt.plot(calendar, purchases, 'r', linewidth = 1) 
    plt.show()

    plt.figure()
    plt.plot(calendar, np.add(income, purchases), 'k', linewidth = 1, alpha = 0.6) 
    plt.show()

    acumulado = np.add(income, purchases)
    for i in range(len(acumulado)):
        if i != 0:
            acumulado[i] += acumulado[i - 1]
    plt.figure()
    plt.plot(calendar, acumulado, 'k', linewidth = 1, alpha = 0.6) 
    plt.show()


def count_balance(sales, calendar):
    income = [0] * len(calendar)
    purchases = [0] * len(calendar)

    for each_sale in sales:
        i = calendar.index(str_to_day(each_sale.time))
        if int(each_sale.price) > 0:
            income[i] += int(each_sale.quantity) * int(each_sale.price)
        else:
            purchases[i] += int(each_sale.quantity) * int(each_sale.price) * (1)
    
    return [income, purchases]