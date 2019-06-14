from models.inventories.database_connector import *
from models.inventories.order import *
from models.saler import *

class SalerInventory(Database):

    table = "salers"

    def __init__(self):
        Database.__init__(self)

    def getAll(self):
        results = Database.getAll(self)
        datas = []
        for result in results:
            temp = Saler(result)
            datas.append(temp)
        return datas
    
    def getWhere(self, condition):
        results = Database.getWhere(self, condition)
        datas = []
        for result in results:
            temp = Saler(result)
            datas.append(temp)
        return datas

    def create(self, data):
        return Database.create(self, data)
    
    def delete(self, salerID):
        OrderInv = OrderInventory()
        OrderInv.deleteWhere(["saler_id", "=", salerID])
        query = "DELETE FROM salers WHERE id = {}".format(salerID)
        Database.execute(self, query)
        return True
    
    def deleteWhere(self, condition):
        results = Database.getWhere(self, condition, "id")
        for result in results:
            self.delete(result[0])
    
    def getOneWhere(self, condition, cols="*"):
        result = Database.getOneWhere(self, condition, cols)
        if result:
            temp = Saler(result)
            return temp