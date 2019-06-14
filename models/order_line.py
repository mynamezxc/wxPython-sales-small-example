class OrderLine():

    def __init__(self, row):
        if row:
            OrderInv = OrderInventory()
            ProductInv = ProductInventory()
            self.id = row[0]
            self.order_id = OrderInv.getOneWhere(["id", "=", row[1]])
            self.product_id = ProductInv.getOneWhere(["id", "=", row[2]])
            self.amount = row[3]
            self.quantity = row[4]
            self.sub_total = row[5]
            self.created_at = row[6]