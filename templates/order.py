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

###########################################################################
## Class order
###########################################################################

class OrderPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 847,662 ), style = wx.TAB_TRAVERSAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Customer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer1.Add( self.m_staticText5, 1, wx.ALL|wx.EXPAND, 5 )
		
		m_customer_idChoices = []
		self.m_customer_id = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_customer_idChoices, wx.CB_SORT )
		self.m_customer_id.SetSelection( 0 )
		fgSizer1.Add( self.m_customer_id, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Saler", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		m_saler_idChoices = []
		self.m_saler_id = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 730,-1 ), m_saler_idChoices, wx.CB_SORT )
		self.m_saler_id.SetSelection( 0 )
		fgSizer1.Add( self.m_saler_id, 0, wx.ALL, 5 )
		
		
		bSizer31.Add( fgSizer1, 0, wx.EXPAND, 5 )
		
		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Product", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText14.Wrap( -1 )
		gbSizer6.Add( self.m_staticText14, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_product_idChoices = []
		self.m_product_id = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), m_product_idChoices, 0 )
		self.m_product_id.SetSelection( 0 )
		gbSizer6.Add( self.m_product_id, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_quantity = wx.StaticText( self, wx.ID_ANY, u"Quantity", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_quantity.Wrap( -1 )
		gbSizer6.Add( self.m_quantity, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_product_quantity = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gbSizer6.Add( self.m_product_quantity, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_btn_add_product = wx.Button( self, wx.ID_ANY, u"Add to order", wx.DefaultPosition, wx.Size( 220,-1 ), 0 )
		gbSizer6.Add( self.m_btn_add_product, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer31.Add( gbSizer6, 0, wx.EXPAND, 5 )
		
		self.m_grid4 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid4.CreateGrid( 5, 6 )
		self.m_grid4.EnableEditing( False )
		self.m_grid4.EnableGridLines( True )
		self.m_grid4.EnableDragGridSize( False )
		self.m_grid4.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid4.SetColSize( 0, 44 )
		self.m_grid4.SetColSize( 1, 229 )
		self.m_grid4.SetColSize( 2, 129 )
		self.m_grid4.SetColSize( 3, 102 )
		self.m_grid4.SetColSize( 4, 125 )
		self.m_grid4.SetColSize( 5, 191 )
		self.m_grid4.EnableDragColMove( False )
		self.m_grid4.EnableDragColSize( True )
		self.m_grid4.SetColLabelSize( 30 )
		self.m_grid4.SetColLabelValue( 0, u"ID" )
		self.m_grid4.SetColLabelValue( 1, u"name" )
		self.m_grid4.SetColLabelValue( 2, u"price" )
		self.m_grid4.SetColLabelValue( 3, u"quantity" )
		self.m_grid4.SetColLabelValue( 4, u"tax/fee" )
		self.m_grid4.SetColLabelValue( 5, u"total" )
		self.m_grid4.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid4.EnableDragRowSize( False )
		self.m_grid4.SetRowLabelSize( 1 )
		self.m_grid4.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid4.SetDefaultCellBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_grid4.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer31.Add( self.m_grid4, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_create_order = wx.Button( self, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_create_order.SetDefault() 
		bSizer31.Add( self.m_create_order, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer31, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Order list", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 12, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer4.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 15, 6 )
		self.m_grid1.EnableEditing( False )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.SetColSize( 0, 45 )
		self.m_grid1.SetColSize( 1, 92 )
		self.m_grid1.SetColSize( 2, 122 )
		self.m_grid1.SetColSize( 3, 196 )
		self.m_grid1.SetColSize( 4, 204 )
		self.m_grid1.SetColSize( 5, 165 )
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"ID" )
		self.m_grid1.SetColLabelValue( 1, u"status" )
		self.m_grid1.SetColLabelValue( 2, u"total" )
		self.m_grid1.SetColLabelValue( 3, u"customer" )
		self.m_grid1.SetColLabelValue( 4, u"saler" )
		self.m_grid1.SetColLabelValue( 5, u"created" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 1 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer4.Add( self.m_grid1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
	
	def __del__( self ):
		pass
	

