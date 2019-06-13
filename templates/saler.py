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
		
		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetDefault() 
		fgSizer1.Add( self.m_button9, 0, wx.ALL, 5 )
		
		
		bSizer31.Add( fgSizer1, 0, wx.EXPAND, 5 )
		
		self.m_grid4 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid4.CreateGrid( 5, 6 )
		self.m_grid4.EnableEditing( True )
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
		self.m_grid4.SetColLabelValue( 1, u"Fullname" )
		self.m_grid4.SetColLabelValue( 2, u"Address" )
		self.m_grid4.SetColLabelValue( 3, u"Contact phone" )
		self.m_grid4.SetColLabelValue( 4, u"Identify number" )
		self.m_grid4.SetColLabelValue( 5, u"active" )
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
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer31.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		gbSizer9 = wx.GridBagSizer( 0, 0 )
		gbSizer9.SetFlexibleDirection( wx.BOTH )
		gbSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Saler name", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.m_staticText32.Wrap( -1 )
		gbSizer9.Add( self.m_staticText32, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		m_choice21Choices = []
		self.m_choice21 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), m_choice21Choices, 0 )
		self.m_choice21.SetSelection( 0 )
		gbSizer9.Add( self.m_choice21, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer9.Add( self.m_button12, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		bSizer31.Add( gbSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer31, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
	
	def __del__( self ):
		pass
	

