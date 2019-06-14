from models.inventories.database_connector import *
from models.inventories.order_line import *
from models.order import *

class OrderInventory(Database):

    table = "orders"

    def __init__(self):
        Database.__init__(self)

    def getAll(self):
        results = Database.getAll(self)
        datas = []
        for result in results:
            temp = Order(result)
            datas.append(temp)
        return datas

    def getWhere(self, condition):
        results = Database.getWhere(self, condition)
        datas = []
        for result in results:
            temp = Order(result)
            datas.append(temp)
        return datas

    def create(self, data):
        return Database.create(self, data)

    def delete(self, orderID):
        OrderLineINV = OrderLineInventory()
        OrderLineINV.deleteWhere(["order_id", "=", orderID])
        query = "DELETE FROM orders WHERE id = {}".format(orderID)
        Database.execute(self, query)
        return True

    def deleteWhere(self, condition):
        results = Database.getWhere(self, condition, "id")
        for result in results:
            self.delete(result[0])

    def getOneWhere(self, condition, cols="*"):
        result = Database.getOneWhere(self, condition, cols)
        if result:
            temp = Order(result)
        return temp