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
from models.inventories.saler import *

###########################################################################
## Class Saler
###########################################################################

class SalerPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 843,387 ), style = wx.TAB_TRAVERSAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Fullname", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer1.Add( self.m_staticText5, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		self.m_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_name, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Address", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_address = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 730,-1 ), 0 )
		fgSizer1.Add( self.m_address, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Contact phone", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		fgSizer1.Add( self.m_staticText26, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_phone = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_phone, 0, wx.ALL, 5 )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Identity number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		fgSizer1.Add( self.m_staticText27, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_identity_num = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer1.Add( self.m_identity_num, 0, wx.ALL, 5 )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		fgSizer1.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		self.m_create_saler = wx.Button( self, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_create_saler.SetDefault() 
		fgSizer1.Add( self.m_create_saler, 0, wx.ALL, 5 )
		
		
		bSizer31.Add( fgSizer1, 0, wx.EXPAND, 5 )
		
		self.m_saler_list = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,500 ), 0 )
		
		# Grid
		self.m_saler_list.CreateGrid( 0, 6 )
		self.m_saler_list.EnableEditing( False )
		self.m_saler_list.EnableGridLines( True )
		self.m_saler_list.EnableDragGridSize( False )
		self.m_saler_list.SetMargins( 0, 0 )
		
		# Columns
		self.m_saler_list.SetColSize( 0, 44 )
		self.m_saler_list.SetColSize( 1, 200 )
		self.m_saler_list.SetColSize( 2, 240 )
		self.m_saler_list.SetColSize( 3, 102 )
		self.m_saler_list.SetColSize( 4, 125 )
		self.m_saler_list.SetColSize( 5, 110 )
		self.m_saler_list.EnableDragColMove( False )
		self.m_saler_list.EnableDragColSize( False )
		self.m_saler_list.SetColLabelSize( 30 )
		self.m_saler_list.SetColLabelValue( 0, u"ID" )
		self.m_saler_list.SetColLabelValue( 1, u"Fullname" )
		self.m_saler_list.SetColLabelValue( 2, u"Address" )
		self.m_saler_list.SetColLabelValue( 3, u"Contact phone" )
		self.m_saler_list.SetColLabelValue( 4, u"Identify number" )
		self.m_saler_list.SetColLabelValue( 5, u"active" )
		self.m_saler_list.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_saler_list.EnableDragRowSize( False )
		self.m_saler_list.SetRowLabelSize( 1 )
		self.m_saler_list.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_saler_list.SetDefaultCellBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_saler_list.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer31.Add( self.m_saler_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer31.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		gbSizer9 = wx.GridBagSizer( 0, 0 )
		gbSizer9.SetFlexibleDirection( wx.BOTH )
		gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Saler name", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText32.Wrap( -1 )
		gbSizer9.Add( self.m_staticText32, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_saler_name_listChoices = []
		self.m_saler_name_list = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), m_saler_name_listChoices, 0 )
		self.m_saler_name_list.SetSelection( 0 )
		gbSizer9.Add( self.m_saler_name_list, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_delete_saler = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.m_delete_saler, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer31.Add( gbSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer31, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer3 )
		self.Layout()

		# Connect Events
		self.m_create_saler.Bind( wx.EVT_BUTTON, self.m_createSaler )
		self.m_delete_saler.Bind( wx.EVT_BUTTON, self.m_delSaler )
	
	def __del__( self ):
		pass
	
	def m_createSaler( self, event ):
		res = {}
		res.update({"name": self.m_name.GetValue()})
		res.update({"address":self.m_address.GetValue()})
		res.update({"phone":self.m_phone.GetValue()})
		res.update({"identity_num":self.m_identity_num.GetValue()})
		res.update({"status": 1})

		error = False

		if len(res['name']) <= 5 or len(res['address']) <= 5:
			error = "Ten va dia chi phai lon hon 5 ky tu"

		regex = r'^[0-9]{9,13}$'
		matches = re.match(regex, res['identity_num'], re.M|re.I)
		if not matches:
		    error = "Chung minh thu khong hop le"
		
		regex = r'^[0-9+]{10,13}$'
		matches = re.match(regex, res['phone'], re.M|re.I)
		if not matches:
		    error = "So dien thoai khong hop le"
		
		if error:
			wx.MessageBox(error, "Message" ,wx.OK | wx.ICON_ERROR)
		else:
			SalerInv = SalerInventory()
			res.update({"id": SalerInv.create(data=res)})
			wx.MessageBox("Create success", "Message" ,wx.OK | wx.ICON_INFORMATION)

			maxRow = self.m_saler_list.GetNumberRows()
			self.m_saler_list.AppendRows(numRows=1)
			self.m_saler_list.SetCellValue(maxRow, 0, str(res['id']))
			self.m_saler_list.SetCellValue(maxRow, 1, str(res['name']))
			self.m_saler_list.SetCellValue(maxRow, 2, str(res['address']))
			self.m_saler_list.SetCellValue(maxRow, 3, str(res['phone']))
			self.m_saler_list.SetCellValue(maxRow, 4, str(res['identity_num']))
			self.m_saler_list.SetCellValue(maxRow, 5, "True" if res['status'] == 1 else "False")
			self.m_saler_list.AutoSizeRow(maxRow)
			self.m_saler_name_list.Append(str(res['id']) + " " + str(res['name']))
	
	def m_delSaler( self, event ):
		selected = self.m_saler_name_list.GetString(self.m_saler_name_list.GetSelection())
		regex = r'([0-9]+)(.*)'
		matches = re.match(regex, selected, re.M|re.I)
		if matches:
			salerID = matches.groups()[0]
			answer = wx.MessageBox("What happens when you delete customer? All orders of that customer will be deleted. Are you sure?", "Message" ,wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
			if answer == wx.YES:
				SalerInv = SalerInventory()
				SalerInv.delete(salerID)
				wx.MessageBox("Delete success!", "Message" ,wx.OK | wx.ICON_INFORMATION)
		else:
			wx.MessageBox("Error when removing this value", "Message" ,wx.OK | wx.ICON_ERROR)