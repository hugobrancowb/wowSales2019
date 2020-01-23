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

class Product:
    def __init__(self, name: str):
        self.name = name
        self.sales = []

    def new_sale(self, date, income: int):
        self.sales.append([date, income])
    
    def get_sales(self):
        return self.sales

def add_Product(List: Product, name: str, date, income: int):
    exists = False
    i = 0
    for product in List:
        if product.name == name:
            exists = True
        else:
            i += 1
    
    if exists == False:
        List.append(Product(name))

    List[i].new_sale(date, income)
    
    return List