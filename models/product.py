class Product():

    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.price = row[2]
        self.unit_id = row[3]
        self.created_at = row[4]