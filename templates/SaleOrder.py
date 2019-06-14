# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import datetime
from models.Bill import *
from models.BillDetail import *
from models.Unit import *
from models.Product import *
from models.Staff import *
from models.Customer import *
###########################################################################
## Class MyPanel51
###########################################################################

class SaleOrderPanel ( wx.Panel ):

	
	def __init__( self, parent ):

		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 931,545 ), style = wx.TAB_TRAVERSAL )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Ngày HD: *", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		gbSizer5.Add( self.m_staticText21, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textbill_date = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.m_textbill_date, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Ký hiệu/STT:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText32.Wrap( -1 )
		gbSizer5.Add( self.m_staticText32, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textSTT = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		gbSizer5.Add( self.m_textSTT, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		self.m_textSTT.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		self.m_textsymbol = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		gbSizer5.Add( self.m_textsymbol, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		self.m_textsymbol.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Tên Customer:* ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		gbSizer5.Add( self.m_staticText22, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Địa chỉ:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		gbSizer5.Add( self.m_staticText23, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textaddress = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.m_textaddress, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Số điện thoại:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		gbSizer5.Add( self.m_staticText24, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textphone_number = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.m_textphone_number, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Hình thức TT:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		gbSizer5.Add( self.m_staticText25, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textHTTT = wx.TextCtrl( self, wx.ID_ANY, u"Tiền mặt", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.m_textHTTT, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Tên Staff:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		gbSizer5.Add( self.m_staticText26, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choicestaff_nameChoices = []
		self.m_choicestaff_name = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choicestaff_nameChoices, 0 )
		self.m_choicestaff_name.SetSelection( 0 )
		gbSizer5.Add( self.m_choicestaff_name, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Tình trạng:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		gbSizer5.Add( self.m_staticText27, wx.GBPosition( 3, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_choicestatusChoices = []
		self.m_choicestatus = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choicestatusChoices, 0 )
		self.m_choicestatus.SetSelection( 0 )
		gbSizer5.Add( self.m_choicestatus, wx.GBPosition( 3, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Ghi chú:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		gbSizer5.Add( self.m_staticText28, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textnote = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.m_textnote, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 5 ), wx.ALL|wx.EXPAND, 5 )
		
		m_choiceHangChoices = []
		self.m_choiceHang = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceHangChoices, 0 )
		self.m_choiceHang.SetSelection( 0 )
		gbSizer5.Add( self.m_choiceHang, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_btnXoadong = wx.Button( self, wx.ID_ANY, u"Xóa dòng", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.m_btnXoadong, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Chọn Product:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		gbSizer5.Add( self.m_staticText35, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		m_cbocustomer_nameChoices = []
		self.m_cbocustomer_name = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), m_cbocustomer_nameChoices, 0 )
		gbSizer5.Add( self.m_cbocustomer_name, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer9.Add( gbSizer5, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_gridSource = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,250 ), 0 )
		
		# Grid
		self.m_gridSource.CreateGrid( 0, 10 )
		self.m_gridSource.EnableEditing( True )
		self.m_gridSource.EnableGridLines( True )
		self.m_gridSource.EnableDragGridSize( False )
		self.m_gridSource.SetMargins( 0, 0 )
		
		# Columns
		self.m_gridSource.SetColSize( 0, 80 )
		self.m_gridSource.SetColSize( 1, 200 )
		self.m_gridSource.SetColSize( 2, 80 )
		self.m_gridSource.SetColSize( 3, 80 )
		self.m_gridSource.SetColSize( 4, 80 )
		self.m_gridSource.SetColSize( 5, 80 )
		self.m_gridSource.SetColSize( 6, 80 )
		self.m_gridSource.SetColSize( 7, 80 )
		self.m_gridSource.SetColSize( 8, 80 )
		self.m_gridSource.SetColSize( 9, 200 )
		self.m_gridSource.EnableDragColMove( False )
		self.m_gridSource.EnableDragColSize( True )
		self.m_gridSource.SetColLabelSize( 30 )
		self.m_gridSource.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_gridSource.EnableDragRowSize( True )
		self.m_gridSource.SetRowLabelSize( 1 )
		self.m_gridSource.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_gridSource.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer11.Add( self.m_gridSource, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer9.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Tổng tiền hàng:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		gbSizer6.Add( self.m_staticText29, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		gbSizer6.Add( self.m_staticText33, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_textproduct_total_price = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.m_textproduct_total_price, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		self.m_textproduct_total_price.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Tiền thuế:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		gbSizer6.Add( self.m_staticText30, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_texttax_amount = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.m_texttax_amount, wx.GBPosition( 0, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		self.m_texttax_amount.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Tổng tiền:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gbSizer6.Add( self.m_staticText31, wx.GBPosition( 0, 8 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_texttotal = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer6.Add( self.m_texttotal, wx.GBPosition( 0, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		self.m_texttotal.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer9.Add( gbSizer6, 1, wx.EXPAND, 5 )
		
		gbSizer7 = wx.GridBagSizer( 0, 0 )
		gbSizer7.SetFlexibleDirection( wx.BOTH )
		gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 915,-1 ), wx.LI_HORIZONTAL )
		gbSizer7.Add( self.m_staticline1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 7 ), wx.ALL, 5 )
		
		self.m_btnDong = wx.Button( self, wx.ID_ANY, u"Đóng", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_btnDong, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"                                           ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		gbSizer7.Add( self.m_staticText36, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_btnIn = wx.Button( self, wx.ID_ANY, u"In", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_btnIn, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_btnThem = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_btnThem, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer9.Add( gbSizer7, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		
		# Connect Events
		self.m_btnDong.Bind( wx.EVT_BUTTON, self.m_btnDongOnButtonClick )
		self.m_btnIn.Bind( wx.EVT_BUTTON, self.m_btnInOnButtonClick )
		self.m_btnThem.Bind( wx.EVT_BUTTON, self.m_btnThemOnButtonClick )
		self.m_choiceHang.Bind( wx.EVT_CHOICE, self.m_choiceHangOnChoice )
		self.m_btnXoadong.Bind(wx.EVT_BUTTON, self.m_btnXoadongOnButtonClick )

	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	
	xldb_HH= ProductModel()
	xldb_NV= StaffModel()
	xldb_KH= CustomerModel()
	xldb_PX= BillModel()
	xldb_PXCT= BillModelct()

	def m_btnDongOnButtonClick( self, event ):
		frame = self.GetParent()
		frame.Close()
	
	def m_btnInOnButtonClick( self, event ):
		event.Skip()

	def CheckValid(self):
		customer_name = self.m_cbocustomer_name.GetValue().strip() 
		bill_date = self.m_textbill_date.GetValue().strip() 
		valid = True
		if len(customer_name)==0: 
			valid = False
			self.m_cbocustomer_name.SetFocus() 
		if len(bill_date)==0: 
			valid = False
			self.m_textbill_date.SetFocus() 
		return valid


	def m_btnThemOnButtonClick( self, event ):
		if self.CheckValid()==False:
			wx.MessageBox("Vui lòng không để trống dữ liệu","Thông báo",wx.OK|wx.ICON_WARNING)
			return
		tongdong= self.m_gridSource.GetNumberRows()
		if tongdong<=0:
			valid = False
			wx.MessageBox("Vui lòng nhập chi tiết Product","Thông báo",wx.OK|wx.ICON_WARNING)
			return
		symbol = self.m_textsymbol.GetValue()
		bill_date = self.m_textbill_date.GetValue()
		bill_num_order = self.m_textSTT.GetValue()
		customer_id = customer_name = self.m_cbocustomer_name.GetValue()
		staff_id = staff_name = self.m_choicestaff_name.GetString(self.m_choicestaff_name.GetSelection())
		payment_method = self.m_textHTTT.GetValue()
		product_total_price = self.m_textproduct_total_price.GetValue()
		total = self.m_texttotal.GetValue()
		tax_total = self.m_texttax_amount.GetValue()
		note = self.m_textnote.GetValue()
		status = staff_name = self.m_choicestatus.GetString(self.m_choicestatus.GetSelection())
		address = self.m_textaddress.GetValue()
		phone_number = self.m_textphone_number.GetValue()

		kq = self.xldb_PX.Insert(symbol, bill_date, bill_num_order,customer_id,staff_id,customer_name,staff_name,payment_method,product_total_price,total,tax_total,note,status,address,phone_number)
		# insert Phieu xuat chi tiết
		dsId= self.xldb_PX.GetMaxID()
		if dsId!=None:
			cell = dsId[0]
			id= int(cell)
			if id>0:
				TongDong= self.m_gridSource.GetNumberRows()
				row_value=[]
				valid = True
				for i in range(TongDong):
					row=[]
					# isValid = 0
					for j in range(10):
						cell_value = self.m_gridSource.GetCellValue(i,j)
						row.append(cell_value)
						
					product_id = str(row[0])
					product_nameHOA= str(row[1])
					unit_id = unit_code= str(row[2])
					amount = str(row[3])
					unit_price = str(row[4])
					TIENHANG= str(row[5])
					tax = str(row[6])
					tax_amount = str(row[7])
					note = str(row[9])
					ct = self.xldb_PXCT.Insert(product_id,unit_id,product_nameHOA,unit_code,amount,unit_price,TIENHANG,tax,tax_amount,note,id)
					if ct<=0:
						valid = False
						break
			else:
				valid = False

			if valid==True:
				self.OnLoadData()
				wx.MessageBox("Thêm dữ liệu thành công","Thông báo",wx.OK|wx.ICON_INFORMATION)
			else: 
				wx.MessageBox("Thêm dữ liệu không thành công","Thông báo",wx.OK|wx.ICON_WARNING)
	
	def m_btnXoadongOnButtonClick( self, event ):
		try:
			row=[]
			row_index = self.m_gridSource.GetSelectedRows()[0]
			if row_index>=0:
				for i in range(0,10):
					row.append(self.m_gridSource.GetCellValue(row_index,i))
            
				product_id = str(row[0])
				product_nameHOA= str(row[1])
				unit_id = unit_code= str(row[2])
				amount = str(row[3])
				unit_price = str(row[4])
				tienhang= self.convertToNum(str(row[5]))
				tax = str(row[6])
				tax_amount = self.convertToNum(str(row[7]))
				total = self.convertToNum(str(row[8]))

				self.TinhTongHang(tienhang,tax_amount,total,False)
				self.m_gridSource.DeleteRows(row_index)
		except Exception as e:
			wx.MessageBox("Vui lòng chọn dòng để xóa: " + e.args[0])
	
	def convertToNum(self, a):
		try:
			number = eval(a)
			return number
		except:
			return 0
	
	def TinhTongHang(self, tienhang,tax_amount,total,bAdd):
		try:
			th = self.convertToNum(self.m_textproduct_total_price.GetValue())
			tt = self.convertToNum(self.m_texttax_amount.GetValue())
			ttien = self.convertToNum(self.m_texttotal.GetValue())
			if bAdd==True:
				th+=tienhang
				tt+=tax_amount
				ttien+=total
			else:
				th-=tienhang
				tt-=tax_amount
				ttien-=total
				if th<0:
					th = 0
				if tt<0:
					tt = 0
				if ttien<0:
					ttien = 0
			self.m_textproduct_total_price.SetValue(str(th))
			self.m_texttax_amount.SetValue(str(tt))
			self.m_texttotal.SetValue(str(ttien))
		except expression as identifier:
			pass
		

	def m_choiceHangOnChoice( self, event ):
		objHang = self.m_choiceHang.GetString(self.m_choiceHang.GetSelection())
		id= objHang[0]
		dsHH= self.xldb_HH.GetHangHoa(id)
		i= self.m_gridSource.GetNumberRows()
	
		if dsHH!=None:
			# for i in range (0,len(dsHH)):
			cell = dsHH[0]
			if(str(cell['product_name'])!=None and str(cell['product_name'])!="" ):
				if cell['unit_id']==None:
					cell['unit_id']=""
				if cell['amount']==None:
					cell['amount']=""
				if cell['price']==None:
					cell['price']=""
				if cell['tax']==None:
					cell['tax']=""
				if cell['description']==None:
					cell['description']=""
				tienhang = 0
				tax_amount = 0
				total = 0
				try:
					tienhang = eval(str(cell['amount']))*eval(str(cell['price']))
				except :
					tienhang = 0
				try:
					tax = self.convertToNum(str(cell['tax']))
					tax_amount= tienhang *tax*0.01
					total = tienhang+tax_amount
				except :
					tax_amount = 0	
					total = 0
				
				self.m_gridSource.AppendRows(1)
				self.m_gridSource.SetCellValue(i,0,str(cell['ID']))
				self.m_gridSource.SetCellValue(i,1,str(cell['product_name']))
				self.m_gridSource.SetCellValue(i,2,str(cell['unit_id']))
				self.m_gridSource.SetCellValue(i,3,str(cell['amount']))
				self.m_gridSource.SetCellValue(i,4,str(cell['price']))
				self.m_gridSource.SetCellValue(i,5,str(tienhang))
				self.m_gridSource.SetCellValue(i,6,str(cell['tax']))
				self.m_gridSource.SetCellValue(i,7,str(tax_amount))
				self.m_gridSource.SetCellValue(i,8,str(total))
				self.m_gridSource.SetCellValue(i,9,str(cell['description']))
				self.TinhTongHang(tienhang,tax_amount,total,True)
	# event.Skip()

	
	def InitData(self):
		self.m_btnIn.Hide()
		self.m_gridSource.SetColLabelValue(0, "Id")
		self.m_gridSource.SetColLabelValue(1, "Tên Product")
		self.m_gridSource.SetColLabelValue(2, "Unit")
		self.m_gridSource.SetColLabelValue(3, "Số lượng")
		self.m_gridSource.SetColLabelValue(4, "Đơn giá")
		self.m_gridSource.SetColLabelValue(5, "Tiền hàng")
		self.m_gridSource.SetColLabelValue(6, "Thuế suất")
		self.m_gridSource.SetColLabelValue(7, "Tiền thuế")
		self.m_gridSource.SetColLabelValue(8, "Thành tiền")
		self.m_gridSource.SetColLabelValue(9, "Ghi chú")
		self.m_textbill_date.SetValue(datetime.datetime.now().strftime("%d/%m/%Y"))
		self.m_textsymbol.SetValue("PXBH")
		self.m_choicestatus.Append('Chưa duyệt')
		self.m_choicestatus.Append('Đã duyệt')
		self.m_choicestatus.SetSelection( 0 )
		self.m_choicestaff_name.SetSelection( 0 )
		#Disable
		
		self.m_textsymbol.Enabled = self.m_textSTT.Enabled = self.m_texttax_amount.Enabled=\
		self.m_textproduct_total_price.Enabled = self.m_texttotal.Enabled = False
		# dsAll_DVT= xldb_DVT.DanhSach()
		dsAll_HH= self.xldb_HH.DanhSach()
		dsAll_NV= self.xldb_NV.DanhSach()
		dsAll_KH= self.xldb_KH.DanhSach()
		dsAll_PX= self.xldb_PX.DanhSach()
		dsSTT= self.xldb_PX.GetSTT()
		if dsAll_KH!=None:
			for i in range (0,len(dsAll_KH)):
				cell = dsAll_KH[i]
				if(str(cell['customer_name'])!=None and str(cell['customer_name'])!=""):
					self.m_cbocustomer_name.Append(str(cell['customer_name']))

		if dsAll_NV!=None:
			for i in range (0,len(dsAll_NV)):
				cell = dsAll_NV[i]
				if(str(cell['staff_name'])!=None and str(cell['staff_name'])!=""):
					self.m_choicestaff_name.Append(str(dsAll_NV[i]['staff_name']))

		if dsAll_HH!=None:
			for i in range (0,len(dsAll_HH)):
				cell = dsAll_HH[i]
				if(str(cell['product_name'])!=None and str(cell['product_name'])!="" ):
					ma = str(dsAll_HH[i]['ID']) +'  '+  str(dsAll_HH[i]['product_name'])
					self.m_choiceHang.Append(ma)

		if dsSTT!=None:
			stt = int(dsSTT[0])
			if(stt<0):
				stt = 0
			self.m_textSTT.SetValue( str(stt+1))
		return

	def OnLoadData(self):
		self.m_textbill_date.SetValue(datetime.datetime.now().strftime("%d/%m/%Y"))
		self.m_textsymbol.SetValue("PXBH")
		self.m_choicestatus.SetSelection( 0 )
		self.m_choicestaff_name.SetSelection( 0 )
		self.m_cbocustomer_name.SetValue('')
		self.m_textHTTT.SetValue('Tiền mặt')
		self.m_textproduct_total_price.SetValue('')
		self.m_texttotal.SetValue('')
		self.m_texttax_amount.SetValue('')
		self.m_textnote.SetValue('')
		self.m_textaddress.SetValue('')
		self.m_textphone_number.SetValue('')
		tongdong= self.m_gridSource.GetNumberRows()
		self.m_gridSource.ClearGrid()
		for i in range(tongdong):
			self.m_gridSource.DeleteRows(i)
	

		# self.m_gridSource.SetRowSize(0)
		dsSTT= self.xldb_PX.GetSTT()

		if dsSTT!=None:
			stt = int(dsSTT[0])
			if(stt<0):
				stt = 0
			self.m_textSTT.SetValue( str(stt+1))

		return