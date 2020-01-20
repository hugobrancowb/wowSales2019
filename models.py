class Transaction:
    def __init__(self, itemName, quantity, price, player, time, source):
        self.itemName   = itemName
        self.quantity   = quantity
        self.price      = price
        self.player     = player
        self.time       = time
        self.source     = source

    def serialize(self):
        return {
            "itemName": self.itemName,
            "quantity": self.quantity,
            "price":    self.price,
            "player":   self.player,
            "time": str(self.time),
            "source":   self.source
        }


def transactionFromJSON(json):
    return Transaction(
        json["itemName"],
        json["quantity"],
        json["price"],
        json["player"],
        json["time"],
        json["source"]
    )
