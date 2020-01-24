# Hugo Branco
# GitHub: hugobrancowb

import csv
from datetime import datetime
from jsonfiles import load_json, saveJSONfile
from models import Data, Transaction
from plotdata import plot
from report_by_month import report_by_month

def importing_sales(data: Data):
    # Vendas realizadas  =  Lucro bruto
    with open('data/Accounting_Azralon_sales.csv', newline='', encoding='utf-8') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        print('')
        counter = 0
        for row in reader:
            if counter == 0:
                counter = counter + 1
                continue

            itemName = row[1]
            stackSize = row[2]
            quantity = row[3]
            price = row[4]
            otherPlayer = row[5]
            player = row[6]            
            source = row[8]

            time = datetime.utcfromtimestamp(int(row[7]))
            
            # filter only auctions
            if source != "Auction": continue

            # filter invalid product name
            if itemName == "?": continue

            # filter only 2019 transactions
            if (time.year == 2019):
                time = time.isoformat()
                time = time.split("T")
                time = time[0]
            else: continue

            transaction = Transaction(itemName, stackSize, quantity, price, otherPlayer, player, time, source)

            data.add_sales(transaction)
    
    data.add_products()

    return data

def main():
    while(True):
        print("")
        print("1. Update sales data.")
        print("2. Plot data.")
        print("3. Print sales record.")
        print("4. Delete existing data.")
        print("5. Report for each month.")
        print("0. Exit.")

        option = input()

        if (int(option) > 5) | ((int(option) < 0)):
            print("Entrada invalida")
        else:            
            if int(option) == 1:
                try:
                    data = load_json()           
                except:
                    data = Data()
                    print("", end="")
                    
                importing_sales(data)
                saveJSONfile(data)
            
            if int(option) == 2:
                try:
                    data = load_json() 
                except:
                    print("Couldnt find JSON file.")
                    exit()
                
                plot(data)
            
            if int(option) == 3:
                try:
                    data = load_json()
                    for row in data.sales:
                        print("{}\t {}\t{}\t{}\t{}".format(row.itemName[0:15],row.quantity,row.price,row.time,row.source))
                except:
                    print("Couldnt find JSON file.")
                    exit()
            
            if int(option) == 4:
                try:
                    data = Data()
                    open('allsales.json', 'w', encoding='utf-8').close()
                    print("\tjson file deleted.")
                except:
                    print("\tcouldnt find json file.")        
            
            if int(option) == 5:
                try:
                    data = load_json()
                except:
                    print("Couldnt find JSON file.")
                    exit()
                    
                report_by_month(data)

            if int(option) == 0:
                break

main()