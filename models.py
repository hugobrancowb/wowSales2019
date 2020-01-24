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

class Data:
    def __init__(self, sales = [], products = {}):
        self.sales = sales
        self.products = products

    def add_sales(self, transaction: Transaction):
        exists = False
        if self.sales:
            for sale in self.sales:
                if sale.itemName == transaction.itemName:
                    if sale.stackSize == transaction.stackSize:
                        if sale.quantity == transaction.quantity:
                            if sale.price == transaction.price:
                                if sale.otherPlayer == transaction.otherPlayer:
                                    if sale.player == transaction.player:
                                        if sale.time == transaction.time:
                                            if sale.source == transaction.source:
                                                exists = True
            
            if exists == False: self.sales.append(transaction)
        else:
            self.sales.append(transaction)

        return self

    def add_products(self):
        allSales = self.sales
        lista = self.products

        for sale in allSales:
            date = sale.time.split("-")
            date = date[0]+"-"+date[1]

            if sale.itemName in lista:
                if date in lista[sale.itemName]:
                    lista[sale.itemName][date] += int(sale.price) * int(sale.quantity)
                else:
                    lista[sale.itemName][date] = int(sale.price) * int(sale.quantity)
            else:
                lista[sale.itemName] = {}
                lista[sale.itemName][date] = int(sale.price) * int(sale.quantity)
        
        return self