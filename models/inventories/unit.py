from models.inventories.database_connector import *
from models.inventories.product import *
from models.unit import *

class UnitInventory(Database):

    table = "units"

    def __init__(self):
        Database.__init__(self)

    def getAll(self):
        results = Database.getAll(self)
        datas = []
        for result in results:
            temp = Unit(result)
            datas.append(temp)
        return datas
    
    def getWhere(self, condition):
        results = Database.getWhere(self, condition)
        datas = []
        for result in results:
            temp = Unit(result)
            datas.append(temp)
        return datas
    
    def create(self, data):
        return Database.create(self, data)
    
    def delete(self, unitID):
        ProductInv = ProductInventory()
        ProductInv.deleteWhere(["unit_id", "=", unitID])
        query = "DELETE FROM units WHERE id = {}".format(unitID)
        Database.execute(self, query)
        return True
    
    def deleteWhere(self, condition):
        results = Database.getWhere(self, condition, "id")
        for result in results:
            self.delete(result[0])