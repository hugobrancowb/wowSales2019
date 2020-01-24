from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt
import datefunctions as df
import pandas as pd
from models import Data

def report_by_month(data: Data):
    # make a list with every month in range
    calendar = df.create_list_of_months(data.sales)

    # builds a dataframe
    dataframe_imt = product_dataframe(data)
    
    # print for each month
    for mes in calendar:
        temp_imt = dataframe_imt[dataframe_imt['month'] == mes]
        temp_imt = temp_imt.sort_values(by = 'total', ascending = False)
        print('Most sold in {} of {}:'.format(mes.strftime('%B'), mes.strftime('%Y')))
        for x in range(0, 5):
            print('\t{} - {} gold'.format(temp_imt.iloc[x, 0], temp_imt.iloc[x, 2]/10000))
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

    df_imt = {'item': item, 'month': month, 'total': total}
    dataframe_imt = pd.DataFrame(df_imt)

    return dataframe_imt