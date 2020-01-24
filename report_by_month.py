from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt
import datefunctions as df
import pandas as pd
from models import Data

def report_by_month(data: Data):
    # make a list with every month in range
    calendar = df.create_list_of_months(data.sales)
    item = []
    month = []
    total = []

    # builds a dataframe
    for i, entry in data.products.items():
        for m, t in entry.items():
            m = df.str_to_month(m)
            item.append(i)
            month.append(m)
            total.append(int(t))

    df_imt = {"item": item, "month": month, "total": total}
    dataframe_imt = pd.DataFrame(df_imt)
    
    # ver x com mais lucros em cada mes
    print("")

    # imprimir para cada mes da lista


    return ""