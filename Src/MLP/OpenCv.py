# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import os

import wx
import wx.xrc

from Config.Init import *

import Src.MLA.CV_CasCade as cvcc

###########################################################################
## Class MyPanel1
###########################################################################

class P19 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 270,400 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsp19 = wx.BoxSizer( wx.VERTICAL )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl1 = wx.StaticText( self, wx.ID_ANY, u"Neg No.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl1.Wrap( -1 )

		Hsz1.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_READONLY )
		Hsz1.Add( self.fld1, 0, wx.ALL, 5 )

		self.lbl2 = wx.StaticText( self, wx.ID_ANY, u"Pos. No.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl2.Wrap( -1 )

		Hsz1.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.fld2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_READONLY )
		Hsz1.Add( self.fld2, 0, wx.ALL, 5 )


		Vsp19.Add( Hsz1, 0, wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl3 = wx.StaticText( self, wx.ID_ANY, u"Image File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl3.Wrap( -1 )

		Hsz2.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.imgfil = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
		Hsz2.Add( self.imgfil, 1, wx.ALL, 5 )


		Vsp19.Add( Hsz2, 0, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.lblx = wx.StaticText( self, wx.ID_ANY, u"X", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblx.Wrap( -1 )

		Hsz3.Add( self.lblx, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.MXa = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0.5, 0.1 )
		self.MXa.SetDigits( 3 )
		self.MXa.SetToolTip( u"Maximum X Angle" )

		Hsz3.Add( self.MXa, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lbly = wx.StaticText( self, wx.ID_ANY, u"Y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbly.Wrap( -1 )

		Hsz3.Add( self.lbly, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.MYa = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, -10, 10, -0.5, 0.1 )
		self.MYa.SetDigits( 3 )
		self.MYa.SetToolTip( u"Maximum Y Angle" )

		Hsz3.Add( self.MYa, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.lblz = wx.StaticText( self, wx.ID_ANY, u"Z", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblz.Wrap( -1 )

		Hsz3.Add( self.lblz, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.MZa = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, -10, 10, 0.5, 0.1 )
		self.MZa.SetDigits( 3 )
		self.MZa.SetToolTip( u"Maximum Z Angle" )

		Hsz3.Add( self.MZa, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsp19.Add( Hsz3, 0, wx.EXPAND, 5 )

		Hsz4 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnStp1 = wx.Button( self, wx.ID_ANY, u"Make png OutPut", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz4.Add( self.btnStp1, 1, wx.ALL, 5 )


		Vsp19.Add( Hsz4, 0, wx.EXPAND, 5 )

		Hsz5 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl4 = wx.StaticText( self, wx.ID_ANY, u"Info File List name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl4.Wrap( -1 )

		Hsz5.Add( self.lbl4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Infolst = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_SMALL )
		Hsz5.Add( self.Infolst, 0, wx.ALL, 5 )


		Vsp19.Add( Hsz5, 0, wx.EXPAND, 5 )

		Hsz6 = wx.BoxSizer( wx.HORIZONTAL )

		self.lblw = wx.StaticText( self, wx.ID_ANY, u"Width", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblw.Wrap( -1 )

		Hsz6.Add( self.lblw, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Wid = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 1000, 24 )
		Hsz6.Add( self.Wid, 0, wx.ALL, 5 )

		self.lblh = wx.StaticText( self, wx.ID_ANY, u"Height", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblh.Wrap( -1 )

		Hsz6.Add( self.lblh, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Hei = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 0, 1000, 24 )
		Hsz6.Add( self.Hei, 0, wx.ALL, 5 )


		Vsp19.Add( Hsz6, 0, wx.EXPAND, 5 )

		Hsz7 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl5 = wx.StaticText( self, wx.ID_ANY, u"Vector File name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lbl5.Wrap( -1 )

		self.lbl5.SetToolTip( u"*.vec" )

		Hsz7.Add( self.lbl5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.vecfil = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz7.Add( self.vecfil, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsp19.Add( Hsz7, 0, wx.EXPAND, 5 )

		Hsz8 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnStp2 = wx.Button( self, wx.ID_ANY, u"Create Positiv Vector", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz8.Add( self.btnStp2, 1, wx.ALL, 5 )


		Vsp19.Add( Hsz8, 0, wx.EXPAND, 5 )

		Hsz9 = wx.BoxSizer( wx.HORIZONTAL )

		self.nPos = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 100, 10000, 1800 )
		self.nPos.SetToolTip( u"-numPos" )

		Hsz9.Add( self.nPos, 0, wx.ALL, 5 )

		self.nNeg = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 100, 10000, 900 )
		self.nNeg.SetToolTip( u"-numNeg" )

		Hsz9.Add( self.nNeg, 0, wx.ALL, 5 )

		self.nStg = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 1, 100, 10 )
		self.nStg.SetToolTip( u"-numStage" )

		Hsz9.Add( self.nStg, 0, wx.ALL, 5 )

		self.btnchk = wx.Button( self, wx.ID_ANY, u"...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.btnchk.SetToolTip( u"Check" )

		Hsz9.Add( self.btnchk, 0, wx.ALL, 5 )


		Vsp19.Add( Hsz9, 0, wx.EXPAND, 5 )

		Hsz10 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnStp3 = wx.Button( self, wx.ID_ANY, u"train cascade", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz10.Add( self.btnStp3, 1, wx.ALL, 5 )


		Vsp19.Add( Hsz10, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsp19 )
		self.Layout()

		# Connect Events
		self.btnStp1.Bind( wx.EVT_BUTTON, self.Step1 )
		self.btnStp2.Bind( wx.EVT_BUTTON, self.Step2 )
		self.btnchk.Bind( wx.EVT_BUTTON, self.Chkit )
		self.btnStp3.Bind( wx.EVT_BUTTON, self.Step3 )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Start(self):
		dlg = wx.Dialog(self, -1)
		pnl = MyPanel2(dlg)
		dlg.SetSize((500,155))
		dlg.SetLabel("Set Path")
		dlg.ShowModal()
		self.pospth = pnl.PosPth.GetPath()
		self.negpth = pnl.NegPth.GetPath()
		self.infofl = pnl.infofil.GetPath()
		dlg.Destroy()
		self.num = len(os.listdir(self.negpth))
		#print(self.pospth,self.negpth,self.num, self.infofl)
		self.fld1.SetValue(str(self.num))
		self.fld2.SetValue('')


	def Test(self):
		pass

	def Step1( self, event ):
		imfl = self.imgfil.GetPath()
		bgtx = Src_mla+'Dataset\\'+'bg.txt'
		mxa = self.MXa.GetValue()
		mya = self.MYa.GetValue()
		mza = self.MZa.GetValue()

		cvcc.Makepngout(imfl,bgtx,self.infofl,self.pospth,mxa,mya,mza,self.num)
		wx.MessageBox("Create test samples from single image applying distortions...")
		event.Skip()

	def Step2( self, event ):
		infi = self.Infolst.GetPath()
		wdis = self.Wid.GetValue()
		heis = self.Hei.GetValue()
		if self.vecfil.GetValue()[-4:] == '.vec':
			self.vecf = Src_mla+"Dataset\\"+self.vecfil.GetValue()
		else:
			self.vecf = Src_mla+"Dataset\\"+self.vecfil.GetValue()+'.vec'
		cvcc.MakePosVector(infi,self.num,wdis,heis,self.vecf)
		wx.MessageBox("Vectore file Create ")
		event.Skip()

	def Chkit( self, event ):
		if not os.path.isdir(Src_mla+"Dataset\\"+'Data'):
			os.mkdir(Src_mla+"Dataset\\"+'Data')
		if not os.path.isfile(self.vecf):
			wx.MessageBox("Vector file not exist please create it")
			return 1

		event.Skip()

	def Step3( self, event ):
		datapth = Src_mla+'Dataset\\'+'Data'
		wdis = self.Wid.GetValue()
		heis = self.Hei.GetValue()
		bgtx = Src_mla + 'Dataset\\' + 'bg.txt'
		vecf = self.vecf
		npos = self.nPos.GetValue()
		nneg = self.nNeg.GetValue()
		nstg = self.nStg.GetValue()
		cvcc.TrainCasCade(datapth,vecf,bgtx,npos,nneg,nstg,wdis,heis)
		wx.MessageBox("Haar Training Is Craete")
		event.Skip()



###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,150 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl1 = wx.StaticText( self, wx.ID_ANY, u"Positive (Info):", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		self.lbl1.Wrap( -1 )

		Hsz1.Add( self.lbl1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.PosPth = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		Hsz1.Add( self.PosPth, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn1 = wx.Button( self, wx.ID_ANY, u"Make Dir", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz1.Add( self.btn1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )

		Hsz2 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl2 = wx.StaticText( self, wx.ID_ANY, u"Negative (BG):", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		self.lbl2.Wrap( -1 )

		Hsz2.Add( self.lbl2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.NegPth = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_SMALL )
		Hsz2.Add( self.NegPth, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn2 = wx.Button( self, wx.ID_ANY, u"Make bg.txt", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz2.Add( self.btn2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz2, 1, wx.EXPAND, 5 )

		Hsz3 = wx.BoxSizer( wx.HORIZONTAL )

		self.lbl3 = wx.StaticText( self, wx.ID_ANY, u"Info file name:", wx.DefaultPosition, wx.Size( 95,-1 ), 0 )
		self.lbl3.Wrap( -1 )

		Hsz3.Add( self.lbl3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.infofil = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Choos a file or new file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_SAVE|wx.FLP_SMALL|wx.FLP_USE_TEXTCTRL )
		Hsz3.Add( self.infofil, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.btn3 = wx.Button( self, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		Hsz3.Add( self.btn3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Vsz1.Add( Hsz3, 1, wx.EXPAND, 5 )


		self.SetSizer( Vsz1 )
		self.Layout()

		self.mkpospth = False
		self.mkbgfil = False
		self.setinffil = False

		# Connect Events
		self.btn1.Bind( wx.EVT_BUTTON, self.makpth )
		self.btn2.Bind( wx.EVT_BUTTON, self.mkbgtxt )
		self.btn3.Bind( wx.EVT_BUTTON, self.aply )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def makpth( self, event ):
		if os.path.isdir(self.PosPth.GetPath()):
			self.mkpospth = True
			print('Directory Exist')
			return 1
		if self.PosPth.GetPath() != '':
			os.mkdir(self.PosPth.GetPath())
			self.mkpospth = True
		event.Skip()

	def mkbgtxt( self, event ):
		if os.path.isfile(Src_mla+'Dataset\\bg.txt'):
			self.mkbgfil = True
			print('file exist')
			return 1
		if self.NegPth.GetPath() != '':
			bgpth = self.NegPth.GetPath()
			cvcc.MakeBGtxt(bgpth)
			self.mkbgfil = True
		event.Skip()

	def aply( self, event ):
		if self.infofil.GetPath() != '':
			self.iinfofile = self.infofil.GetPath()
			self.setinffil = True
			if self.setinffil and self.mkbgfil and self.mkpospth:
				q = self.GetParent()
				q.Close()
		event.Skip()
