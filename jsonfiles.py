from models import Data
from models import transactionFromJSON
import json

def saveJSONfile(data: Data):
    with open('allsales.json', 'w', encoding='utf-8') as jsonFile:
        data_to_save = {}
        data_to_save["Transactions"] = []
        data_to_save["Products"] = data.products
        data_to_save["Purchases"] = data.purchases
        for operation in data.sales:
            data_to_save["Transactions"].append(operation.serialize())
        
        json.dump(data_to_save, jsonFile, sort_keys=True, indent=4)

def load_json():
    with open('allsales.json', encoding='utf-8') as jsonFile:
        data_from_file = json.load(jsonFile)
        data = Data()
        data.products = data_from_file["Products"]
        data.purchases = data_from_file["Purchases"]
        for info in data_from_file["Transactions"]:
            data.sales.append(transactionFromJSON(info))
    return data