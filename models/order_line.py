class OrderLine():

    def __init__(self, row):
        self.id = row[0]
        self.order_id = row[1]
        self.product_id = row[2]
        self.amount = row[3]
        self.quantity = row[4]
        self.sub_total = row[5]
        self.created_at = row[6]