from models.inventories.database_connector import *
from models.inventories.order import *
from models.product import *

class ProductInventory(Database):

    table = "products"

    def __init__(self):
        Database.__init__(self)

    def getAll(self):
        results = Database.getAll(self)
        datas = []
        for result in results:
            temp = Product(result)
            datas.append(temp)
        return datas
    
    def getWhere(self, condition):
        results = Database.getWhere(self, condition)
        datas = []
        for result in results:
            temp = Product(result)
            datas.append(temp)
        return datas

    def create(self, data):
        return Database.create(self, data)
    
    def delete(self, productID):
        OrderInv = OrderInventory()
        OrderInv.deleteWhere(["product_id", "=", productID])
        query = "DELETE FROM products WHERE id = {}".format(productID)
        Database.execute(self, query)
        return True
    
    def deleteWhere(self, condition):
        results = Database.getWhere(self, condition, "id")
        for result in results:
            self.delete(result[0])