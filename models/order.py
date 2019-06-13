class Order():

    def __init__(self, row):
        self.id = row[0]
        self.total = row[1]
        self.tax = row[2]
        self.fee = row[3]
        self.status = row[4]
        self.customer_id = row[5]
        self.saler_id = row[6]
        self.created_at = row[7]