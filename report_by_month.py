from datetime import datetime, date, timedelta
import matplotlib.pyplot as plt
import datefunctions as df
from models import Data

def report_by_month(data: Data):
    # fazer lista com todos os meses
    for sales in data.products.keys():
        for date in sales.values():
            if min_date:
                if date < min_date:
                    min_date = date
            else:
                min_date = date
            if max_date:
                if date > max_date:
                    max_date = date
            else:
                max_date = date

    # ver x com mais lucros em cada mes
    print("")

    # imprimir para cada mes da lista


    return ""