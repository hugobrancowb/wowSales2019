#!/usr/bin/python3
# Hugo Branco
# GitHub: hugobrancowb

import csv
import json
from datetime import datetime
from models import Transaction, transactionFromJSON

allSales = []

def importingSales(maxItems):
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
            price = row[4] # preço, em cobres, por UNIDADE vendida. para total tem que multiplicar pela quantidade
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

            exists = False
            for sale in allSales:
                if sale.itemName == transaction.itemName:
                    if sale.stackSize == transaction.stackSize:
                        if sale.quantity == transaction.quantity:
                            if sale.price == transaction.price:
                                if sale.otherPlayer == transaction.otherPlayer:
                                    if sale.player == transaction.player:
                                        if sale.time == transaction.time:
                                            if sale.source == transaction.source:
                                                exists = True
            
            if exists == False: allSales.append(transaction)
            
            if (counter >= maxItems): break
            else: counter = counter + 1

def saveJSONfile():
    with open('allsales.json', 'w', encoding='utf-8') as jsonFile:
        data = {}
        data["Transactions"] = []
        for operation in allSales:
            data["Transactions"].append(operation.serialize())
        
        json.dump(data, jsonFile, sort_keys=True, indent=4)

def main(allSales):
    while(True):
        print("")
        print("1. Update sales data.")
        print("2. Plot data.")
        print("3. Print sales record.")
        print("4. Delete existing data.")
        print("0. Exit.")

        option = input()

        if (int(option) > 4) | ((int(option) < 0)):
            print("Entrada invalida")
        else:            
            if int(option) == 1:
                try:
                    with open('allsales.json', encoding='utf-8') as jsonFile:
                        data = json.load(jsonFile)
                        allSales = []
                        for info in data["Transactions"]:
                            allSales.append(transactionFromJSON(info))                
                except:
                    print("", end="")
                importingSales(2)
                saveJSONfile()
            if int(option) == 2:
                print("", end="")
            if int(option) == 3:
                try:
                    with open('allsales.json', encoding='utf-8') as jsonFile:
                        data = json.load(jsonFile)
                        allSales = []
                        for info in data["Transactions"]:
                            allSales.append(transactionFromJSON(info))

                        print("")
                        for row in allSales:
                            print("{}\t {}\t{}\t{}\t{}".format(row.itemName[0:15],row.quantity,row.price,row.time,row.source))
                except:
                    print("Couldnt find JSON file.")
            if int(option) == 4:
                try:
                    open('allsales.json', 'w', encoding='utf-8').close()
                    print("\tjson file deleted.")
                except:
                    print("\tcouldnt find json file.")                
            if int(option) == 0:
                break
######
main(allSales)