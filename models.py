class Transaction:
    def __init__(self, itemName, stackSize, quantity, price, otherPlayer, player, time, source):
        self.itemName = itemName
        self.stackSize = stackSize
        self.quantity = quantity
        self.price = price
        self.otherPlayer = otherPlayer
        self.player = player
        self.time = time
        self.source = source

    def serialize(self):
        return {
            "itemName": self.itemName,
            "stackSize": self.stackSize,
            "quantity": self.quantity,
            "price": self.price,
            "otherPlayer": self.otherPlayer,
            "player": self.player,
            "time": str(self.time),
            "source": self.source
        }

def transactionFromJSON(json):
    return Transaction(
        json["itemName"],
        json["stackSize"],
        json["quantity"],
        json["price"],
        json["otherPlayer"],
        json["player"],
        json["time"],
        json["source"]
    )

def add_sales(allSales):
    lista = {}
    date = sale.time.split("-")
    date = date[0]+"-"+date[1]
    
    for sale in allSales:
        if sale.itemName in lista:
            if date in lista[sale.itemName]:
                lista[sale.itemName][date] += int(sale.price) * int(sale.quantity)
            else:
                lista[sale.itemName][date] = int(sale.price) * int(sale.quantity)
        else:
            lista[sale.itemName] = {}
            lista[sale.itemName][date] = int(sale.price) * int(sale.quantity)
    
    return lista