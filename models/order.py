from models.inventories.customer import *
from models.inventories.saler import *
from models.inventories.order_line import *


class Order():

    def __init__(self, row):
        if row:
            SalerInv = SalerInventory()
            CustomerInv = CustomerInventory()
            self.id = row[0]
            self.total = row[1]
            self.tax = row[2]
            self.fee = row[3]
            self.status = row[4]
            self.customer_id = CustomerInv.getOneWhere(["id", "=", row[5]])
            self.saler_id = SalerInv.getOneWhere(["id", "=", row[6]])
            self.created_at = row[7]
    
    def getOrderLines(self):
        OrderLineInv = OrderLineInventory()
        self.order_lines = OrderLineInv.getWhere(["order_id", "=", self.id])
        return self.order_lines