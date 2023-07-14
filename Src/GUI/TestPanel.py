#In the name of GOD
#please put your code under here
############ Description ############
##  This is a Sample Demo File
##  Only four line you can use for
##  Description
##
############### End ###############
# -*- coding: utf-8 -*-
#!usr/bin/env python

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview as dv

from Config.Init import *

###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 587,500 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.Cam1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_RAISED )
		Vsz2.Add( self.Cam1, 1, wx.ALL|wx.EXPAND, 5 )


		Hsz1.Add( Vsz2, 1, wx.EXPAND, 5 )

		Vsz3 = wx.BoxSizer( wx.VERTICAL )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt1 = wx.StaticText( self, wx.ID_ANY, u"←Cam1         ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt1.Wrap( -1 )

		Hsz2.Add( self.txt1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txt2 = wx.StaticText( self, wx.ID_ANY, u"Cam2 ↓      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt2.Wrap( -1 )

		Hsz2.Add( self.txt2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.txt3 = wx.StaticText( self, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt3.Wrap( -1 )

		Hsz2.Add( self.txt3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lamp1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( ICON32_PATH+u"ledoff.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.lamp1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txt4 = wx.StaticText( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt4.Wrap( -1 )

		Hsz2.Add( self.txt4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lamp2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( ICON32_PATH+u"ledoff.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.lamp2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz3.Add( Hsz2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		Vsz4 = wx.BoxSizer( wx.VERTICAL )

		self.Cam2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SUNKEN )
		Vsz4.Add( self.Cam2, 1, wx.ALL|wx.EXPAND, 5 )


		Vsz3.Add( Vsz4, 1, wx.EXPAND, 5 )


		Hsz1.Add( Vsz3, 1, wx.EXPAND, 5 )


		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.ejct = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.ejct.SetBitmap( wx.Bitmap(ICON32_PATH+ u"ejct.bmp", wx.BITMAP_TYPE_ANY ) )
		Hsz3.Add( self.ejct, 0, wx.ALL, 5 )

		self.play = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.play.SetBitmap( wx.Bitmap(ICON32_PATH+ u"play.bmp", wx.BITMAP_TYPE_ANY ) )
		Hsz3.Add( self.play, 0, wx.ALL, 5 )

		self.stop = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.stop.SetBitmap( wx.Bitmap(ICON32_PATH+ u"stop.bmp", wx.BITMAP_TYPE_ANY ) )
		Hsz3.Add( self.stop, 0, wx.ALL, 5 )


		Hsz3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.ejct2 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.ejct2.SetBitmap( wx.Bitmap(ICON32_PATH+ u"ejct.bmp", wx.BITMAP_TYPE_ANY ) )
		Hsz3.Add( self.ejct2, 0, wx.ALL, 5 )

		self.play2 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.play2.SetBitmap( wx.Bitmap(ICON32_PATH+ u"play.bmp", wx.BITMAP_TYPE_ANY ) )
		Hsz3.Add( self.play2, 0, wx.ALL, 5 )

		self.stop2 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.stop2.SetBitmap( wx.Bitmap(ICON32_PATH+ u"stop.bmp", wx.BITMAP_TYPE_ANY ) )
		Hsz3.Add( self.stop2, 0, wx.ALL, 5 )


		Vsz1.Add( Hsz3, 0, wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.DVLC1 = dv.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.COl1 = self.DVLC1.AppendTextColumn( u"Date", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVLC1.AppendTextColumn( u"timeOpen", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		self.Col3 = self.DVLC1.AppendTextColumn( u"timeStop", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		self.Col4 = self.DVLC1.AppendTextColumn( u"pic", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		self.Col5 = self.DVLC1.AppendTextColumn( u"counter", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		self.Col6 = self.DVLC1.AppendTextColumn( u"Camera No.", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		Hsz4.Add( self.DVLC1, 1, wx.ALL|wx.EXPAND, 5 )


		Vsz1.Add( Hsz4, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		# Connect Events
		self.ejct.Bind( wx.EVT_BUTTON, self.load )
		self.play.Bind( wx.EVT_BUTTON, self.plyvido )
		self.stop.Bind( wx.EVT_BUTTON, self.stpvido )
		self.ejct2.Bind( wx.EVT_BUTTON, self.load2 )
		self.play2.Bind( wx.EVT_BUTTON, self.plyvido2 )
		self.stop2.Bind( wx.EVT_BUTTON, self.stpvido2 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def load( self, event ):
		event.Skip()

	def plyvido( self, event ):
		event.Skip()

	def stpvido( self, event ):
		event.Skip()

	def load2( self, event ):
		event.Skip()

	def plyvido2( self, event ):
		event.Skip()

	def stpvido2( self, event ):
		event.Skip()
