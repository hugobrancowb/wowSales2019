from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt
import datefunctions as df
import pandas as pd
from models import Data

def report_by_month(data: Data):
    # make a list with every month in range
    calendar = df.create_list_of_months(data.sales)

    # builds a dataframe
    [dataframe_pos, dataframe_neg] = product_dataframe(data)
    
    # print for each month
    for mes in calendar:
        temp_pos = dataframe_pos[dataframe_pos['month'] == mes]
        temp_pos = temp_pos.sort_values(by = 'total', ascending = False)
        print('Most sold in {} of {}:'.format(mes.strftime('%B'), mes.strftime('%Y')))
        for x in range(0, 5):
            print('{} - {} g'.format(temp_pos.iloc[x, 0], temp_pos.iloc[x, 2]/10000))
        print('')
    
    # most sold entire year
    total_dic = {}
    for item, k in data.products.items():
        for gold in k.values():
            if item in total_dic:
                total_dic[item] += gold
            else:
                total_dic[item] = gold

    item_name = []
    item_income = []
    for name, income in total_dic.items():
        item_name.append(name)
        item_income.append(income)
    
    tot_pos = {'item': item_name, 'income': item_income}
    total_pos = pd.DataFrame(tot_pos)
    total_pos = total_pos.sort_values(by = 'income', ascending = False)
    print('Most sold: entire year')
    for x in range(0, 5):
        print('{} - {} g'.format(total_pos.iloc[x, 0], total_pos.iloc[x, 1]/10000))
    print('')
    
    #
    # #
    # # # Expenses # # #
    print('Enter "1" if you also want the expenses report: ', end='')
    expenses_key = input()
    if int(expenses_key) == 1:
        for mes in calendar:
            temp_neg = dataframe_neg[dataframe_neg['month'] == mes]
            temp_neg = temp_neg.sort_values(by = 'total')
            print('Most bought in {} of {}:'.format(mes.strftime('%B'), mes.strftime('%Y')))
            for x in range(0, 5):
                print('{} - {} g'.format(temp_neg.iloc[x, 0], (-1)*temp_neg.iloc[x, 2]/10000))
            print('')
    
    # most bought entire year
    total_dic = {}
    for item, k in data.purchases.items():
        for gold in k.values():
            if item in total_dic:
                total_dic[item] += gold
            else:
                total_dic[item] = gold

    item_name = []
    item_income = []
    for name, income in total_dic.items():
        item_name.append(name)
        item_income.append(income)

    tot_pos = {'item': item_name, 'outcome': item_income}
    total_pos = pd.DataFrame(tot_pos)
    total_pos = total_pos.sort_values(by = 'outcome')
    print('Most bought: entire year')
    for x in range(0, 5):
        print('{} - {} g'.format(total_pos.iloc[x, 0], total_pos.iloc[x, 1]/10000))
    print('')

def product_dataframe(data: Data):
    item = []
    month = []
    total = []

    for i, entry in data.products.items():
        for m, t in entry.items():
            m = df.str_to_month(m)
            item.append(i)
            month.append(m)
            total.append(int(t))

    df_pos = {'item': item, 'month': month, 'total': total}
    dataframe_pos = pd.DataFrame(df_pos)
    
    for i, entry in data.purchases.items():
        for m, t in entry.items():
            m = df.str_to_month(m)
            item.append(i)
            month.append(m)
            total.append(int(t))

    df_neg = {'item': item, 'month': month, 'total': total}
    dataframe_neg = pd.DataFrame(df_neg)

    return [dataframe_pos, dataframe_neg]