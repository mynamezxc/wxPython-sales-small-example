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
## Class Product
###########################################################################

class ProductPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 391,384 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		gbSizer1111 = wx.GridBagSizer( 0, 0 )
		gbSizer1111.SetFlexibleDirection( wx.BOTH )
		gbSizer1111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2111 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.m_staticText2111.Wrap( -1 )
		gbSizer1111.Add( self.m_staticText2111, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 305,-1 ), 0 )
		gbSizer1111.Add( self.m_name, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer3.Add( gbSizer1111, 1, wx.EXPAND, 5 )
		
		gbSizer7 = wx.GridBagSizer( 0, 0 )
		gbSizer7.SetFlexibleDirection( wx.BOTH )
		gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Price", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.m_staticText7.Wrap( -1 )
		gbSizer7.Add( self.m_staticText7, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_price = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer7.Add( self.m_price, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"VND", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		gbSizer7.Add( self.m_staticText20, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer3.Add( gbSizer7, 1, wx.EXPAND, 5 )
		
		gbSizer20 = wx.GridBagSizer( 0, 0 )
		gbSizer20.SetFlexibleDirection( wx.BOTH )
		gbSizer20.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Unit", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.m_staticText21.Wrap( -1 )
		gbSizer20.Add( self.m_staticText21, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice6Choices = []
		self.m_choice6 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 305,-1 ), m_choice6Choices, 0 )
		self.m_choice6.SetSelection( 0 )
		gbSizer20.Add( self.m_choice6, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer3.Add( gbSizer20, 1, wx.EXPAND, 5 )
		
		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer7.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button8.SetDefault() 
		fgSizer7.Add( self.m_button8, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( fgSizer7, 1, wx.EXPAND, 5 )
		
		gbSizer111 = wx.GridBagSizer( 0, 0 )
		gbSizer111.SetFlexibleDirection( wx.BOTH )
		gbSizer111.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText211 = wx.StaticText( self, wx.ID_ANY, u"Product", wx.DefaultPosition, wx.Size( 55,-1 ), 0 )
		self.m_staticText211.Wrap( -1 )
		gbSizer111.Add( self.m_staticText211, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 210,-1 ), m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		gbSizer111.Add( self.m_choice1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_delete = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer111.Add( self.m_delete, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer3.Add( gbSizer111, 1, wx.EXPAND, 5 )
		
		
		gbSizer1.Add( bSizer3, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		
		bSizer1.Add( gbSizer1, 1, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid1.CreateGrid( 10, 2 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid1.SetColSize( 0, 80 )
		self.m_grid1.SetColSize( 1, 292 )
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelValue( 0, u"ID" )
		self.m_grid1.SetColLabelValue( 1, u"Unit name" )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 1 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer3.Add( self.m_grid1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
	
	def __del__( self ):
		pass
	

