# Hugo Branco
# GitHub: hugobrancowb

import csv
import json
from datetime import datetime
from models import Transaction, transactionFromJSON
from models import Data
from plotdata import plot

# maxItems DEVE sair após o programa ficar pronto
def importing_sales(data: Data, maxItems: int):
    # Vendas realizadas  =  Lucro bruto
    with open('data/Accounting_Azralon_sales.csv', newline='', encoding='utf-8') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        print('')
        counter = 0
        for row in reader:
            if counter == 0:
                counter = counter + 1
                continue

            # itemString = row[0]
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

            transaction = Transaction(
                    itemName,
                    stackSize,
                    quantity,
                    price,
                    otherPlayer,
                    player,
                    time,
                    source
                )

            data.add_sales(transaction)
            
            if (counter >= maxItems): break
            else: counter = counter + 1
    
    data.add_products()

    return data

def saveJSONfile(data: Data):
    with open('allsales.json', 'w', encoding='utf-8') as jsonFile:
        data_to_save = {}
        data_to_save["Transactions"] = []
        data_to_save["Products"] = data.products
        for operation in data.sales:
            data_to_save["Transactions"].append(operation.serialize())
        
        json.dump(data_to_save, jsonFile, sort_keys=True, indent=4)

def main():
    data = Data()

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
                    with open('allsales.json', encoding='utf-8') as jsonFile:
                        data_from_file = json.load(jsonFile)
                        data = Data()
                        data.products = data_from_file["Products"]
                        for info in data_from_file["Transactions"]:
                            data.sales.append(transactionFromJSON(info))           
                except:
                    print("", end="")

                importing_sales(data, 100)
                saveJSONfile(data)
            
            if int(option) == 2:
                try:
                    with open('allsales.json', encoding='utf-8') as jsonFile:
                        data_from_file = json.load(jsonFile)
                        data = Data()
                        data.products = data_from_file["Products"]
                        for info in data_from_file["Transactions"]:
                            data.sales.append(transactionFromJSON(info)) 
                except:
                    print("Couldnt find JSON file.")
                    exit()
                
                plot(data)
            
            if int(option) == 3:
                try:
                    with open('allsales.json', encoding='utf-8') as jsonFile:
                        data_from_file = json.load(jsonFile)
                        data = Data()
                        data.products = data_from_file["Products"]
                        for info in data_from_file["Transactions"]:
                            data.sales.append(transactionFromJSON(info))
                        for row in data.sales:
                            print("{}\t {}\t{}\t{}\t{}".format(row.itemName[0:15],row.quantity,row.price,row.time,row.source))
                except:
                    print("Couldnt find JSON file.")
                    exit()
            
            if int(option) == 4:
                try:
                    open('allsales.json', 'w', encoding='utf-8').close()
                    print("\tjson file deleted.")
                except:
                    print("\tcouldnt find json file.")        
            
            if int(option) == 5:
                try:
                    with open('allsales.json', encoding='utf-8') as jsonFile:
                        data_from_file = json.load(jsonFile)
                        data = Data()
                        data.products = data_from_file["Products"]
                        for info in data_from_file["Transactions"]:
                            data.sales.append(transactionFromJSON(info))
                except:
                    print("Couldnt find JSON file.")
                    exit()
                
                # Access test for dictionary
                for product_name, product_sales in data.products.items():
                    print(product_name)
                    for date, income in product_sales.items():
                        print("\t{}  {}".format(date, income))
                    print("")

            if int(option) == 0:
                break
######
main()