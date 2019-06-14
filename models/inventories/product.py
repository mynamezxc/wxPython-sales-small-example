from models.inventories.database_connector import *
from models.inventories.order_line import *
from models.inventories.order import OrderInventory as OrderInv
from models.product import *
from models.inventories.unit import *


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
        orderIDS = []
        OrderInv = OrderInv()
        OrderLineInv = OrderLineInventory()

        orderLines = OrderLineInv.getWhere(['product_id', '=', productID])
        for orderLine in orderLines:
            OrderInv.deleteWhere(["id", "=", orderLine.order_id.id])

        query = "DELETE FROM products WHERE id = {}".format(productID)
        Database.execute(self, query)
        return True
    
    def deleteWhere(self, condition):
        results = Database.getWhere(self, condition, "id")
        for result in results:
            self.delete(result[0])

    def getOneWhere(self, condition, cols="*"):
        result = Database.getOneWhere(self, condition, cols)
        if result:
            temp = Product(result)
            return temp
        
    def getUnit(slef, condition):
        UnitInv = UnitInventory()
        UnitInv.getOneWhere(condition)