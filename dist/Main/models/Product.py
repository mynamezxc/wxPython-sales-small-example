
from models.database import *

class ProductModel(Database):

    def DanhSach(self):
        chuoiSQL = "select ID, product_code,product_name, unit_id,product_type_id,amount,cost,price,tax,made_in,description from products"
        cursor = Database.getALL(self,chuoiSQL)
        if cursor != None:    
            recordList = []
            for row in cursor:
                TT = {'ID':row[0], 'product_code': row[1], 'product_name':row[2], 'unit_id': row[3],'product_type_id': row[4],'amount':row[5],'cost': row[6],'price': row[7],'tax': row[8],'made_in': row[9],'description': row[10]}
                recordList.append(TT)
        return recordList

    def GetHangHoa(self, id):
        chuoiSQL = "select ID, product_code,product_name, unit_id,product_type_id,amount,cost,price,tax,made_in,description from products where ID =  "+ id +""
        cursor = Database.getALL(self,chuoiSQL)
        if cursor != None:    
            recordList = []
            for row in cursor:
                TT = {'ID':row[0], 'product_code': row[1], 'product_name':row[2], 'unit_id': row[3],'product_type_id': row[4],'amount':row[5],'cost': row[6],'price': row[7],'tax': row[8],'made_in': row[9],'description': row[10]}
                recordList.append(TT)
        return recordList
    

    def Insert(self, product_code,product_name, unit_id,product_type_id,amount,cost,price,tax,made_in,description):
        chuoiSQL = "insert into products (product_code,product_name, unit_id,product_type_id,amount,cost,price,tax,made_in,description) values(?,?,?,?,?,?,?,?,?,?)"
        kq = Database.execute(self,chuoiSQL,(product_code,product_name, unit_id,product_type_id,amount,cost,price,tax,made_in,description))
        return kq

    def Update(self,ID, product_code,product_name, unit_id,product_type_id,amount,cost,price,tax,made_in,description):
        chuoiSQL = "update products set product_code = ?, product_name = ? , unit_id = ?,product_type_id = ?,amount = ?,cost = ?,price = ?,tax = ?,made_in = ?,description = ? where ID = ?"
        kq = Database.execute(self,chuoiSQL,(product_code,product_name, unit_id,product_type_id,amount,cost,price,tax,made_in,description, ID))
        return kq

    def Delete(self,id):
        chuoiSQL = "delete from products where ID =  ? " 
        kq = Database.execute(self,chuoiSQL,(id,))
        return kq
