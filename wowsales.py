#!/usr/bin/python3
# Hugo Branco
# GitHub: hugobrancowb

import csv
import json
from datetime import datetime
from models import Transaction, transactionFromJSON

allSales = []

def importingSales():
    # Vendas realizadas  =  Lucro bruto
    with open('data/Accounting_Azralon_sales.csv', newline='', encoding='utf-8') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        print('')
        for i, row in enumerate(reader):
            if i == 0: continue
            if i >= 5: break

            print(', '.join(row))

            # itemString = row[0]
            itemName = row[1]
            # stackSize = row[2]
            quantity = row[3]
            price = row[4]
            # otherPlayer = row[5]
            player = row[6]

            time = datetime.utcfromtimestamp(int(row[7]))
            
            # filter only 2019 transactions
            if (time.year == 2019):
                time = time.isoformat()
                time = time.split("T")
                time = time[0]
                source = row[8]
            else: continue

            transaction = Transaction(
                    itemName,
                    quantity,
                    price,
                    player,
                    time,
                    source
                )
            exists = False
            for sale in allSales:
                if exists           == True:                 break
                if sale.itemName    != transaction.itemName: continue
                if sale.quantity    != transaction.quantity: continue
                if sale.price       != transaction.price:    continue
                if sale.player      != transaction.player:   continue
                if sale.time        != transaction.time:     continue
                if sale.source      != transaction.source:   continue
                exists = True
            
            if not exists:
                allSales.append(transaction)

def saveJSONfile():
    with open('allsales.json', 'w') as jsonFile:
        data = {}
        data["Transactions"] = []
        for operation in allSales:
            data["Transactions"].append(operation.serialize())
        
        json.dump(data, jsonFile, sort_keys=True, indent=4)

def main():
    try:
        with open('allsales.json') as jsonFile:
            data = json.load(jsonFile)
            for info in data["Transactions"]:
                allSales.append(transactionFromJSON(info))
    except:
        print("A NEW JSON FILE WILL BE CREATED FROM SCRATCH.")
        
    importingSales()
    saveJSONfile()

main()