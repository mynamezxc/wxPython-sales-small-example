from models.database import *

class CustomerModel(Database):

    def DanhSach(self):
        chuoiSQL = "select ID, customer_code,customer_name,address,email,phone_number from customers"
        cursor = Database.getALL(self,chuoiSQL)
        if cursor != None:    
            recordList = []
            for row in cursor:
                TT = {'ID':row[0], 'customer_code': row[1], 'customer_name':row[2],'address': row[3],'email': row[4],'phone_number': row[5]}
                recordList.append(TT)
        return recordList

    def Insert(self, Ma,Ten,address,email, phone_number):
        chuoiSQL = "insert into customers (customer_code,customer_name,address,email,phone_number) values(?,?,?,?,?)"
        kq = Database.execute(self,chuoiSQL,(Ma,Ten,address,email, phone_number))
        return kq

    def Update(self,Id, Ma,Ten,address,email, phone_number):
        chuoiSQL = "update customers set customer_code = ?, customer_name = ?,address = ?,email = ?,phone_number = ? where ID = ?"
        kq = Database.execute(self,chuoiSQL,(Ma,Ten,address,email, phone_number,Id))
        return kq

    def Delete(self,Id):
        chuoiSQL = "delete from customers where ID =  ? " 
        kq = Database.execute(self,chuoiSQL,(Id,))
        return kq
