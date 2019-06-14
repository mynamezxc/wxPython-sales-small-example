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
import re
from models.inventories.product import *

###########################################################################
## Class ProductPanel
###########################################################################

class ProductPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 504,745 ), style = wx.TAB_TRAVERSAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer1.Add( self.m_staticText5, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.m_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 395,-1 ), 0 )
		fgSizer1.Add( self.m_name, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Price", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_price = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 395,-1 ), 0 )
		fgSizer1.Add( self.m_price, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Unit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		fgSizer1.Add( self.m_staticText26, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_unit_listChoices = []
		self.m_unit_list = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 395,-1 ), m_unit_listChoices, 0 )
		self.m_unit_list.SetSelection( 0 )
		fgSizer1.Add( self.m_unit_list, 0, wx.ALL, 5 )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		fgSizer1.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		self.m_create_product = wx.Button( self, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_create_product.SetDefault() 
		fgSizer1.Add( self.m_create_product, 0, wx.ALL, 5 )
		
		
		bSizer31.Add( fgSizer1, 0, wx.EXPAND, 5 )
		
		self.m_product_list = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,500 ), 0 )
		
		# Grid
		self.m_product_list.CreateGrid( 0, 4 )
		self.m_product_list.EnableEditing( True )
		self.m_product_list.EnableGridLines( True )
		self.m_product_list.EnableDragGridSize( False )
		self.m_product_list.SetMargins( 0, 0 )
		
		# Columns
		self.m_product_list.SetColSize( 0, 44 )
		self.m_product_list.SetColSize( 1, 194 )
		self.m_product_list.SetColSize( 2, 92 )
		self.m_product_list.SetColSize( 3, 152 )
		self.m_product_list.EnableDragColMove( False )
		self.m_product_list.EnableDragColSize( True )
		self.m_product_list.SetColLabelSize( 30 )
		self.m_product_list.SetColLabelValue( 0, u"ID" )
		self.m_product_list.SetColLabelValue( 1, u"Name" )
		self.m_product_list.SetColLabelValue( 2, u"Price" )
		self.m_product_list.SetColLabelValue( 3, u"Unit" )
		self.m_product_list.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_product_list.EnableDragRowSize( False )
		self.m_product_list.SetRowLabelSize( 1 )
		self.m_product_list.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_product_list.SetDefaultCellBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_product_list.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer31.Add( self.m_product_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer31.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		gbSizer9 = wx.GridBagSizer( 0, 0 )
		gbSizer9.SetFlexibleDirection( wx.BOTH )
		gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Customer name", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText32.Wrap( -1 )
		gbSizer9.Add( self.m_staticText32, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_product_name_listChoices = []
		self.m_product_name_list = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), m_product_name_listChoices, 0 )
		self.m_product_name_list.SetSelection( 0 )
		gbSizer9.Add( self.m_product_name_list, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_delete_product = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.m_delete_product, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer31.Add( gbSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer31, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		# Connect Events
		self.m_create_product.Bind( wx.EVT_BUTTON, self.m_createProduct )
		self.m_delete_product.Bind( wx.EVT_BUTTON, self.m_delProduct )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_createProduct( self, event ):
		error = False
		res = {}
		selected = self.m_unit_list.GetString(self.m_unit_list.GetSelection())
		regex = r'([0-9]+)(.*)'
		matches = re.match(regex, selected, re.M|re.I)
		
		try:
			var = int(self.m_price.GetValue())
		except:
			error = "Price must be integer"
		
		error = "Unit is invalid" if not matches else error
		error = "Product name too short" if len(self.m_name.GetValue()) < 3 else error

		if error:
			wx.MessageBox(error, "Message" ,wx.OK | wx.ICON_ERROR)
		else:
			res["unit_id"] = matches.groups()[0]
			res["name"] = self.m_name.GetValue()
			res["price"] = self.m_price.GetValue()
			ProductInv = ProductInventory()
			res["id"] = ProductInv.create(data=res)

			maxRow = self.m_product_list.GetNumberRows()
			self.m_product_list.AppendRows(numRows=1)
			self.m_product_list.SetCellValue(maxRow, 0, str(res['id']))
			self.m_product_list.SetCellValue(maxRow, 1, str(res['name']))
			self.m_product_list.SetCellValue(maxRow, 2, str(res['price']))
			self.m_product_list.SetCellValue(maxRow, 3, str(matches.groups()[1]).replace(" - ", "", 1))
			self.m_product_list.AutoSizeRow(maxRow)
			self.m_product_name_list.Append(str(res['id']) + " " + str(res['name']))
			
	def m_delProduct( self, event ):
		selected = self.m_product_name_list.GetString(self.m_product_name_list.GetSelection())
		regex = r'([0-9]+)(.*)'
		matches = re.match(regex, selected, re.M|re.I)
		if matches:
			productID = matches.groups()[0]
			answer = wx.MessageBox("What happens when you delete product? All orders of that product will be deleted. Are you want to delete?", "Message" ,wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
			if answer == wx.YES:
				ProductInv = ProductInventory()
				ProductInv.delete(productID)
				wx.MessageBox("Delete success!", "Message" ,wx.OK | wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Error when removing this value", "Message" ,wx.OK | wx.ICON_ERROR)
