from models.database import *

class BillModel(Database):

    def DanhSach(self):
        chuoiSQL = "select ID, symbol, bill_date, bill_num_order,customer_id,staff_id,customer_name,staff_name,payment_method,product_total_price,total,tax_total,note,status,address,phone_number from bills"
        cursor = Database.getALL(self,chuoiSQL)
        if cursor != None:    
            recordList = []
            for row in cursor:
                TT = {'ID':row[0],'symbol':row[1], 'bill_date':row[2], 'bill_num_order':row[3],'customer_id':row[4],'staff_id':row[5],'customer_name':row[6],'staff_name':row[7],'payment_method':row[8],'product_total_price':row[9],'total':row[10],'tax_total':row[11],'note':row[12],'status':row[13],'address':row[14],'phone_number':row[15]}
                recordList.append(TT)
        return recordList

    def Insert(self, symbol, bill_date, bill_num_order,customer_id,staff_id,customer_name,staff_name,payment_method,product_total_price,total,tax_total,note,status,address,phone_number):
        chuoiSQL = "insert into bills (symbol, bill_date, bill_num_order,customer_id,staff_id,customer_name,staff_name,payment_method,product_total_price,total,tax_total,note,status,address,phone_number) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        kq = Database.execute(self,chuoiSQL,(symbol, bill_date, bill_num_order,customer_id,staff_id,customer_name,staff_name,payment_method,product_total_price,total,tax_total,note,status,address,phone_number))
        return kq

    def Update(self,Id, symbol, bill_date, bill_num_order,customer_id,staff_id,customer_name,staff_name,payment_method,product_total_price,total,tax_total,note,status,address,phone_number):
        chuoiSQL = "update bills set symbol = ?, bill_date = ?, bill_num_order = ?,customer_id = ?,staff_id = ?,customer_name = ?,staff_name = ?,payment_method = ?,product_total_price = ?,total = ?,tax_total = ?,note = ?,status = ?,address = ?,phone_number = ? where ID = ?"
        kq = Database.execute(self,chuoiSQL,(symbol, bill_date, bill_num_order,customer_id,staff_id,customer_name,staff_name,payment_method,product_total_price,total,tax_total,note,status,address,phone_number,Id))
        return kq

    def Delete(self,Id):
        chuoiSQL = "delete from bills where ID =  ? " 
        kq = Database.execute(self,chuoiSQL,(Id,))
        return kq

    def GetSTT(self):
        chuoiSQL = "select max(bill_num_order) as STT from bills"
        kq = Database.execute2(self,chuoiSQL)
        return kq

    def GetMaxID(self):
        chuoiSQL = "select max(ID) as STT from bills"
        kq = Database.execute2(self,chuoiSQL)
        return kq
