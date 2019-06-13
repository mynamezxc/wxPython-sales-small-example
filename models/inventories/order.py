from models.inventories.database_connector import *
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
        Database.create(self, data)