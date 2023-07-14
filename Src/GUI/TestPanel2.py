#In the name of GOD
#please put your code under here
########## Description ############
#  This is a Sample Demo File
#  Only four line you can use for
#  Description
#
############# End ###############
# -*- coding: utf-8 -*-
#!usr/bin/env python

#########################################################################
# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
#
# PLEASE DO *NOT* EDIT THIS FILE!
#########################################################################

import wx
import wx.xrc
import wx.dataview as dv

import cv2

import time
import threading
import os

from Config.Init import *

import Src.API.CatDogMv1 as CDM

#########################################################################
# Class MyPanel2
#########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 420,550 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		Vsz2 = wx.BoxSizer( wx.VERTICAL )

		self.Cam1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_RAISED )
		Vsz2.Add( self.Cam1, 1, wx.ALL|wx.EXPAND, 5 )


		Hsz1.Add( Vsz2, 1, wx.EXPAND, 5 )


		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.ejct = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.ejct.SetBitmap( wx.Bitmap( ICON32_PATH+u"ejct.bmp", wx.BITMAP_TYPE_ANY ) )
		Hsz2.Add( self.ejct, 0, wx.ALL, 5 )

		self.play = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.play.SetBitmap( wx.Bitmap( ICON32_PATH+u"play.bmp", wx.BITMAP_TYPE_ANY ) )
		Hsz2.Add( self.play, 0, wx.ALL, 5 )

		self.stop = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.stop.SetBitmap( wx.Bitmap( ICON32_PATH+u"stop.bmp", wx.BITMAP_TYPE_ANY ) )
		Hsz2.Add( self.stop, 0, wx.ALL, 5 )


		Hsz2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.txt3 = wx.StaticText( self, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt3.Wrap( -1 )

		Hsz2.Add( self.txt3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lamp1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( ICON32_PATH+u"ledoff.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.lamp1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txt4 = wx.StaticText( self, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt4.Wrap( -1 )

		Hsz2.Add( self.txt4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lamp2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( ICON32_PATH+ u"ledoff.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.lamp2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz2, 0, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer(wx.HORIZONTAL)

		self.txt5 = wx.StaticText(self, wx.ID_ANY, u"Model", wx.DefaultPosition, wx.DefaultSize, 0)
		self.txt5.Wrap(-1)

		Hsz3.Add(self.txt5, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		chs1Choices = [m for m in os.listdir(Src_api) if '.xml' in m]
		self.chs1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chs1Choices, 0)
		self.chs1.SetSelection(0)
		Hsz3.Add(self.chs1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.txt6 = wx.StaticText(self, wx.ID_ANY, u"F", wx.DefaultPosition, wx.DefaultSize, 0)
		self.txt6.Wrap(-1)

		Hsz3.Add(self.txt6, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.Sp1 = wx.SpinCtrlDouble(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(60, -1),
									 wx.SP_ARROW_KEYS, 1, 100, 1.01, 0.1)
		self.Sp1.SetDigits(2)
		Hsz3.Add(self.Sp1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.txt7 = wx.StaticText(self, wx.ID_ANY, u"N", wx.DefaultPosition, wx.DefaultSize, 0)
		self.txt7.Wrap(-1)

		Hsz3.Add(self.txt7, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.Sp2 = wx.SpinCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(60, -1), wx.SP_ARROW_KEYS,
							   1, 100, 1)
		Hsz3.Add(self.Sp2, 0, wx.ALL, 5)

		self.txt8 = wx.StaticText(self, wx.ID_ANY, u"mSize", wx.DefaultPosition, wx.DefaultSize, 0)
		self.txt8.Wrap(-1)

		Hsz3.Add(self.txt8, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		self.fld1 = wx.TextCtrl(self, wx.ID_ANY, u"(55,55)", wx.DefaultPosition, wx.Size(50, -1), 0)
		Hsz3.Add(self.fld1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

		Vsz1.Add(Hsz3, 0, wx.EXPAND, 5)

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.DVLC1 = dv.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,150 ), 0 )
		self.COl1 = self.DVLC1.AppendTextColumn( u"Date", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		self.Col2 = self.DVLC1.AppendTextColumn( u"timeOpen", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		self.Col3 = self.DVLC1.AppendTextColumn( u"timeStop", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		self.Col4 = self.DVLC1.AppendTextColumn( u"pic", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		self.Col5 = self.DVLC1.AppendTextColumn( u"counter", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		self.Col6 = self.DVLC1.AppendTextColumn( u"Camera No.", dv.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, dv.DATAVIEW_COL_RESIZABLE )
		Hsz4.Add( self.DVLC1, 1, wx.ALL|wx.EXPAND, 5 )


		Vsz1.Add( Hsz4, 0, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		self.plypus = 1

		self.timer = wx.Timer(self)
		self.Bind(wx.EVT_TIMER, self.OnTimer)

		#self.cat_cascade = cv2.CascadeClassifier(Src_api+self.chs1.GetStringSelection())



		# Connect Events
		self.ejct.Bind( wx.EVT_BUTTON, self.load )
		self.play.Bind( wx.EVT_BUTTON, self.plyvido )
		self.stop.Bind( wx.EVT_BUTTON, self.stpvido )

	def __del__( self ):
		pass

	# Virtual event handlers, overide them in your derived class
	def ChngIcon(self, buton):
		#print(buton)
		if buton == 'Pus':
			self.play.SetBitmap(wx.Bitmap( ICON32_PATH+u"pase.bmp", wx.BITMAP_TYPE_ANY ))
		elif buton == 'Ply':
			self.play.SetBitmap(wx.Bitmap(ICON32_PATH + u"play.bmp", wx.BITMAP_TYPE_ANY))
		if buton == 'OpnOn':
			self.lamp1.SetBitmap(wx.Bitmap(ICON32_PATH + u"ledon.bmp", wx.BITMAP_TYPE_ANY))
			time.sleep(2)
			self.lamp1.SetBitmap(wx.Bitmap(ICON32_PATH + u"ledoff.bmp", wx.BITMAP_TYPE_ANY))


		elif buton == 'StpOn':
			#self.lamp1.SetBitmap(wx.Bitmap(ICON32_PATH + u"ledoff.bmp", wx.BITMAP_TYPE_ANY))
			self.lamp2.SetBitmap(wx.Bitmap(ICON32_PATH + u"ledon.bmp", wx.BITMAP_TYPE_ANY))

			time.sleep(1)
			self.lamp2.SetBitmap(wx.Bitmap(ICON32_PATH + u"ledoff.bmp", wx.BITMAP_TYPE_ANY))


	def load( self, event ):
		self.cat_cascade = cv2.CascadeClassifier(Src_api + self.chs1.GetStringSelection())
		#self.t = threading.Timer(interval=1.0, function=self.ChngIcon, args=('OpnOn'))
		#self.t = threading.Thread(target=self.ChngIcon, args=('OpnOn'))
		with wx.FileDialog(self, "Open Video file", wildcard="Mpg files (*.mp4)|*.mp4",
			style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return  1 # the user changed their mind

				# Proceed loading the file chosen by the user
			videoname = fileDialog.GetPath()

			self.capture = cv2.VideoCapture(videoname)
			self.ret, self.frame = self.capture.read()

			height, width = self.frame.shape[:2]
			self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

			self.bmp = wx.Bitmap.FromBuffer(width, height, self.frame)
			self.Cam1.SetBitmap(self.bmp)

			self.nFrame = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
			self.fps = int(self.capture.get(cv2.CAP_PROP_FPS))

			#print(self.nFrame,self.fps)

			event.Skip()

	def plyvido( self, event ):
		#print(self.plypus)
		if self.plypus == 1:
			alltims = round(self.nFrame / self.fps)
			self.timer.Start(1000 / self.fps)

			self.ChngIcon('Pus')
			self.plypus = 2
		elif self.plypus == 2:
			self.timer.Stop()

			self.ChngIcon('Ply')
			self.plypus = 1
		else:
			pass

		event.Skip()

	def stpvido( self, event ):
		self.timer.Stop()
		self.ChngIcon('Ply')
		self.plypus = 1

		event.Skip()

	def OnTimer(self, event):
		ret, frame = self.capture.read()
		if ret:
			frame.flags.writeable = False
			frame = self.show_rect(frame)

			height, width = frame.shape[:2]
			frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			self.bmp.CopyFromBuffer(frame)
			numframe = self.capture.get(cv2.CAP_PROP_POS_FRAMES)
			#self.frmcount.SetLabel(str(numframe))

			self.Refresh()
			self.Layout()
		else:
			self.timer.Stop()
			self.ChngIcon('Ply')
			self.plypus = 1

	# self.Video1.SetBitmap(wx.NullBitmap)

	def show_rect(self, frames):
		gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
		sF = self.Sp1.GetValue()
		mN = self.Sp2.GetValue()
		fld = self.fld1.GetValue()
		mS = wx.Size(eval(fld))
		#print(mS, fld)
		# Detects cars of different sizes in the input image
		# cars = self.car_cascade.detectMultiScale(gray, 1.8, 4)
		cats = self.cat_cascade.detectMultiScale(gray, scaleFactor=sF, minNeighbors=mN, minSize=mS)
		if len(cats) > 0:
			for (x, y, w, h) in cats:
				cv2.rectangle(frames, (x, y), (x + w, y + h), (225, 0, 0), 2)
				t = threading.Timer(interval=1, function=self.ChngIcon, args=['OpnOn'])
				t.start()

				#carcropped = self.cropImage(frames, (int(x), int(y), int(w), int(h)))

		return frames

	def cropImage(self, image, rect):
		x, y, w, h = self.computeSafeRegion(image.shape, rect)
		return image[y:y + h, x:x + w]

	def computeSafeRegion(self, shape, bounding_rect):
		top = bounding_rect[1]  # y
		bottom = bounding_rect[1] + bounding_rect[3]  # y +  h
		left = bounding_rect[0]  # x
		right = bounding_rect[0] + bounding_rect[2]  # x +  w
		min_top = 0
		max_bottom = shape[0]
		min_left = 0
		max_right = shape[1]

		if top < min_top:
			top = min_top
		if left < min_left:
			left = min_left
		if bottom > max_bottom:
			bottom = max_bottom
		if right > max_right:
			right = max_right
		return [left, top, right - left, bottom - top]






