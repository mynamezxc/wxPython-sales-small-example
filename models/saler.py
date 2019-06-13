class Saler():

    def __init__(self, row):
        self.id = row[0]
        self.name = row[1]
        self.address = row[2]
        self.phone = row[3]
        self.identity_num = row[4]
        self.status = row[5]
        self.created_at = row[6]