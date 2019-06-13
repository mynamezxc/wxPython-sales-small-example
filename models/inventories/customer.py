from models.inventories.database_connector import *
from models.inventories.order import *
from models.customer import *

class CustomerInventory(Database):

    table = "customers"

    def __init__(self):
        Database.__init__(self)

    def getAll(self):
        results = Database.getAll(self)
        datas = []
        for result in results:
            temp = Customer(result)
            datas.append(temp)
        return datas
    
    def getWhere(self, condition):
        results = Database.getWhere(self, condition)
        datas = []
        for result in results:
            temp = Customer(result)
            datas.append(temp)
        return datas
    
    def create(self, data):
        return Database.create(self, data)
    
    def delete(self, customerID):
        OrderInv = OrderInventory()
        OrderInv.deleteWhere(["customer_id", "=", customerID])
        query = "DELETE FROM customers WHERE id = {}".format(customerID)
        Database.execute(self, query)
        return True
    
    def deleteWhere(self, condition):
        results = Database.getWhere(self, condition, "id")
        for result in results:
            self.delete(result[0])