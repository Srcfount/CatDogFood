#In the name of GOD
#open source file of algorithm or panle algorithm
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.stc as stc

from Config.Init import *

import os
import sys

import keyword

_ = wx.GetTranslation

if wx.Platform == '__WXMSW__':
    faces = {'times': 'Times New Roman',
             'mono': 'Courier New',
             'helv': 'Arial', #'Tahoma', #'Arial',

             'other': 'Comic Sans MS',
             'size': 10,
             'size2': 8,
             }
elif wx.Platform == '__WXMAC__':
    faces = {'times': 'Times New Roman',
             'mono': 'Monaco',
             'helv': 'Arial',
             'other': 'Comic Sans MS',
             'size': 12,
             'size2': 10,
             }
else:
    faces = {'times': 'Times',
             'mono': 'Courier',
             'helv': 'Helvetica',
             'other': 'new century schoolbook',
             'size': 12,
             'size2': 10,
             }


class PythonSTC(stc.StyledTextCtrl):
    fold_symbols = 2

    def __init__(self, parent, PyFile):
        stc.StyledTextCtrl.__init__(self, parent)

        self.StyleClearAll()  # Reset all to be like the default

        self.CmdKeyAssign(ord('B'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMIN)
        self.CmdKeyAssign(ord('N'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMOUT)


        self.SetLexer(stc.STC_LEX_PYTHON)
        self.SetKeyWords(0, " ".join(keyword.kwlist))

        self.SetProperty("fold", "1")
        self.SetProperty("tab.timmy.whinge.level", "1")
        self.SetMargins(0, 0)

        # Indentation and tab stuff
        self.SetIndent(4)  # Proscribed indent size for wx
        self.SetIndentationGuides(True)  # Show indent guides
        self.SetBackSpaceUnIndents(True)  # Backspace unindents rather than delete 1 space
        self.SetTabIndents(True)  # Tab key indents
        self.SetTabWidth(4)  # Proscribed tab size for wx
        self.SetUseTabs(False)  # Use spaces rather than tabs, or
        # TabTimmy will complain!

        self.SetViewWhiteSpace(False)
        self.SetIndentationGuides(stc.STC_STYLE_INDENTGUIDE)

        self.SetEOLMode(stc.STC_EOL_LF)
        # self.SetBufferedDraw(False)
        #self.SetViewEOL(True)
        #self.SetEOLMode(stc.STC_EDGE_NONE)
        #self.SetUseAntiAliasing(True)
        self.SetMarginType(1, stc.STC_MARGIN_NUMBER)
        #self.SetMarginMask(1, 0)
        #self.SetMarginWidth(1, 40)

        # Global default styles for all languages
        self.StyleSetSpec(stc.STC_STYLE_DEFAULT, "face:%(helv)s,size:%(size)d" % faces)



        # Global default styles for all languages
        self.StyleSetSpec(stc.STC_STYLE_DEFAULT, "face:%(helv)s,size:%(size)d" % faces)
        self.StyleSetSpec(stc.STC_STYLE_LINENUMBER, "back:#C0C0C0,face:%(helv)s,size:%(size2)d" % faces)
        self.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR, "face:%(other)s" % faces)
        self.StyleSetSpec(stc.STC_STYLE_BRACELIGHT, "fore:#FFFFFF,back:#0000FF,bold")
        self.StyleSetSpec(stc.STC_STYLE_BRACEBAD, "fore:#000000,back:#FF0000,bold")

        # Python styles
        # Default
        self.StyleSetSpec(stc.STC_P_DEFAULT, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
        # Comments
        self.StyleSetSpec(stc.STC_P_COMMENTLINE, "fore:#007F00,face:%(other)s,size:%(size)d" % faces)
        # Number
        self.StyleSetSpec(stc.STC_P_NUMBER, "fore:#007F7F,size:%(size)d" % faces)
        # String
        self.StyleSetSpec(stc.STC_P_STRING, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
        # Single quoted string
        self.StyleSetSpec(stc.STC_P_CHARACTER, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
        # Keyword
        self.StyleSetSpec(stc.STC_P_WORD, "fore:#00007F,bold,size:%(size)d" % faces)
        # Triple quotes
        self.StyleSetSpec(stc.STC_P_TRIPLE, "fore:#7F0000,size:%(size)d" % faces)
        # Triple double quotes
        self.StyleSetSpec(stc.STC_P_TRIPLEDOUBLE, "fore:#7F0000,size:%(size)d" % faces)
        # Class name definition
        self.StyleSetSpec(stc.STC_P_CLASSNAME, "fore:#0000FF,bold,underline,size:%(size)d" % faces)
        # Function or method name definition
        self.StyleSetSpec(stc.STC_P_DEFNAME, "fore:#007F7F,bold,size:%(size)d" % faces)
        # Operators
        self.StyleSetSpec(stc.STC_P_OPERATOR, "bold,size:%(size)d" % faces)
        # Identifiers
        self.StyleSetSpec(stc.STC_P_IDENTIFIER, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
        #self.StyleSetSpec(wx.stc.STC_P_IDENTIFIER, 'fore:#000000')
        # Comment-blocks
        self.StyleSetSpec(stc.STC_P_COMMENTBLOCK, "fore:#7F7F7F,size:%(size)d" % faces)
        # End of line where string is not closed
        self.StyleSetSpec(stc.STC_P_STRINGEOL, "fore:#000000,face:%(mono)s,back:#E0C0E0,eol,size:%(size)d" % faces)

        #self.StyleSetSpec(stc.STC_TD_STRIKEOUT)
        #self.SetTabDrawMode(stc.STC_TD_STRIKEOUT)

        self.SetCaretForeground("BLUE")

        self.StyleSetFontEncoding(stc.STC_STYLE_DEFAULT,wx.FONTENCODING_CP1256)#    wx.FONTENCODING_UTF8)

        #print(self.GetCodePage())

        # register some images for use in the AutoComplete box.
        # self.RegisterImage(1, images.Smiles.GetBitmap())
        # self.RegisterImage(2,
        #    wx.ArtProvider.GetBitmap(wx.ART_NEW, size=(16,16)))
        # self.RegisterImage(3,
        #    wx.ArtProvider.GetBitmap(wx.ART_COPY, size=(16,16)))

        with open(PyFile, encoding=u'utf-8') as fobj:
            text = fobj.read()

        self.SetText(text)


    def slctal(self):
        self.SelectAll()


###########################################################################
## Class MyPanel2
###########################################################################

class SrcPanel ( wx.Panel ):

	def __init__( self, parent, pyFile, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 680,455 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		Vsz1 = wx.BoxSizer( wx.VERTICAL )

		Hsz1 = wx.BoxSizer( wx.HORIZONTAL )

		self.pyFile = pyFile
		self.ischanged = False

		self.SrcAlg = PythonSTC(self, pyFile)

		#self.SrcAlg.GetCurrentPos()

		Hsz1.Add( self.SrcAlg, 1, wx.EXPAND |wx.ALL, 5 )

		Vsz1.Add( Hsz1, 1, wx.EXPAND, 5 )

		self.SetSizer( Vsz1 )
		self.Layout()


		self.Bind(wx.stc.EVT_STC_CHARADDED, self.editfile, id=wx.ID_ANY)
		self.SrcAlg.Bind(wx.EVT_CHAR_HOOK, self.kyhok)


	def __del__( self ):
		pass


	def editfile(self, event):
		if self.SrcAlg.GetUndoCollection() and not self.ischanged:
			ilbl = self.GetParent().GetLabel()
			self.GetParent().SetLabel(u'*' + ilbl )
			self.ischanged = True

	def kyhok(self, event):
		#print(u'hook',self.ischanged)
		self.editfile(event)
		event.Skip()

	def newstc(self, pyFile):
		self.SrcAlg.ClearAll()
		with open(pyFile, encoding=u'utf-8') as fobj:
			text = fobj.read()
		self.SrcAlg.SetText(text)
		#self.SrcAlg.SetTextRaw(pyFile)

	def opnstc(self, pyFile):
		self.SrcAlg.ClearAll()
		with open(pyFile, encoding=u'utf-8') as fobj:
			text = fobj.read()
		self.SrcAlg.SetText(text)







###########################################################################
## Class MyMenuBar1
###########################################################################

class MyMenuBar1 ( wx.MenuBar ):

	def __init__( self , extmnu=u''):
		wx.MenuBar.__init__ ( self, style = 0 )

		mymnu = {_(u"File"): [(61,_(u'New'),u'',self.newsrc),(62,_(u'Open...'),u'',self.opnsrc),(63,u'',u'',u''),(64,_(u'Save'),u'',self.savsrc),
		                   (65,_(u'Save As...'),u'',self.savasit),(66,u'',u'',u''),(67,u'IDLE editor',u'',self.idlebat),
		                      (68,u'',u'',u''),(69,_(u'Close'),u'',self.closit)],
		         _(u"Edit"): [(71,_(u'Cut'),u'',self.cutit),(72,_(u'Copy'),u'',self.copyit),(73,_(u'Paste'),u'',self.pastit),
		                   (74,u'',u'',u''),(75,_(u'Select All'),u'',self.slctal)] }
		if extmnu == u'Pro':
			mymnu[_(u'Add')] = [(81,_(u'line-close'),_(u'add close code to button function'),self.clos_lin),
			                 (82,_(u'line-getdata'),_(u'get data from fields textctrl '),self.get_lin),
			                 (83,_(u'line-putdata'),_(u'put data to fields textctrl'),self.put_lin),
			                 (84,_(u'line-fillnull'),_(u'fill empty record in all data'),self.null_lin)]

		elif extmnu == u'MLA':
			mymnu[_(u'Add')] = [(91,_(u'Import Numpy'),u'',self.impnum),(92,_(u'Import matplotlib'),u'',self.impmat),
			                 (93,_(u'Import Axes 3D'),u'',self.impa3d)]
			#mymnu[_(u'MLA Dev')] = [(50,_(u'Add this file'),u'',self.toML)]
		elif extmnu == u'AL':
			mymnu[_(u'Add')] = [(91,_(u'Import Numpy'),u'',self.impnum),(92,_(u'Import matplotlib'),u'',self.impmat),
			                 (93,_(u'Import Axes 3D'),u'',self.impa3d),(94,u'',u'',u''),
			                 (95,_(u'MLA Utility(Y select)'),u'',self.impmlu),(96,_(u'MLA Utility(Show Matrix)'),u'',self.impmlu)]
			#mymnu[_(u'MLA Dev')] = [(50, _(u'Add this file'), u'', self.toML)]


		self.Itms = []
		m = 0
		self.Mnus = []
		s = 0

		for mn in mymnu:
			self.Mnus.append( wx.Menu() )
			for it in mymnu[mn]:
				if it[1] != u'':
					self.Itms.append( wx.MenuItem(self.Mnus[s], it[0], it[1], it[2], wx.ITEM_NORMAL) )
					self.Mnus[s].Append(self.Itms[m])
					self.Bind(wx.EVT_MENU, it[3], id=it[0])
					m += 1
				else:
					self.Mnus[s].AppendSeparator()
			self.Append(self.Mnus[s], mn)
			s += 1

		if extmnu == u"Pro":
			self.DfDir = SRC_PATH
		elif extmnu == u'MLA':
			self.DfDir = Src_mla #SRC_PATH+'MLA\\'
		elif extmnu == u'AL':
			self.DfDir = Src_mlp #SRC_PATH+"MLP\\"
		else:
			self.DfDir = MAP

		self.Bind(wx.EVT_MENU_OPEN, self.Doinit, id=self.GetId())



	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def Doinit(self, event):
		frm = self.GetFrame()
		#print(frm)
		self.pnl = frm.GetChildren()[0]
		self.pyfile = self.pnl.pyFile
		self.SrcTxt = self.pnl.SrcAlg

	def newsrc(self, event):
		#print(self.pyfile)
		#print(self.pnl.ischanged)
		if self.pnl.ischanged:
			iyesno = wx.MessageBox(_(u'Do you like to save change'),style=wx.YES_NO)
			#print(iyesno)
			if iyesno == 8:
				return
			else:
				#print(self.pyfile,self.pnl.pyFile)
				self.savsrc(event)
				self.pnl.ischanged = False
				self.pnl.pyFile = u'untitle'
				self.newsrc(event)
		else:
			if u'untitle' in self.pyfile.lower():
				wx.MessageBox(_(u'Please work in this file or close it then use new file'))
			else:
				#print(u'untitle file')
				if self.DfDir == Src_mlp:   #+"MLPane\\":
					self.pnl.newstc(GUI_PATH + u'Temp\\Muntitle.py')
				else:
					self.pnl.newstc(GUI_PATH+u'Temp\\untitle.py')
				self.GetParent().SetLabel(u'untitle')
		event.Skip()

	def opnsrc(self, event):
		with wx.FileDialog(self, _("Open a file"), defaultDir=self.DfDir,wildcard="Python files (*.py)|*.py",
		                   style=wx.FD_OPEN) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return
			pathname = fileDialog.GetPath()
			#self.pyfile = pathname
			self.pnl.pyFile = pathname
			self.pnl.opnstc(pathname)
			self.GetParent().SetLabel(pathname)
		event.Skip()

	def savsrc(self, event):
		if u'untitle.py' in self.pyfile:
			with wx.FileDialog(self, _("Save new file"), defaultDir=self.DfDir,wildcard="Python files (*.py)|*.py",
			                   style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
				if fileDialog.ShowModal() == wx.ID_CANCEL:
					return  # the user changed their mind
				# save the current contents in the file
				pathname = fileDialog.GetPath()
				# print(pathname)
				try:
					with open(pathname, 'w', encoding='utf-8') as f:
						f.write(self.SrcTxt.GetText())
				except IOError:
					print('file error')
				self.pnl.pyFile = pathname
				self.pnl.opnstc(pathname)
				self.GetParent().SetLabel(pathname)
		else:
			try:
				with open(self.pyfile, 'w', encoding='utf-8') as f:
					f.write(self.SrcTxt.GetText())
					#self.SrcTxt.SaveFile(self.pyfile)
			except IOError:
				print('File not write had error')
			wx.MessageBox(_(u'You save to file change successful.'))
			self.pnl.ischanged = False
			self.GetParent().SetLabel(self.pyfile)

		event.Skip()

	def savasit(self, event):
		with wx.FileDialog(self, _("Save As new file"), defaultDir=self.DfDir, wildcard="Python files (*.py)|*.py",
		                   style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
			if fileDialog.ShowModal() == wx.ID_CANCEL:
				return  # the user changed their mind
			# save the current contents in the file
			pathname = fileDialog.GetPath()
			# print(pathname)
			try:
				with open(pathname, 'w', encoding='utf-8') as f:
					f.write(self.SrcTxt.GetText())
			except IOError:
				print('file error')
			#self.SrcTxt.SaveFile(pathname)
			self.pnl.pyFile = pathname
			self.pnl.opnstc(pathname)
			self.GetParent().SetLabel(pathname)
		event.Skip()

	def closit(self, event):
		q = self.GetParent()
		q.Close()

	def cutit(self, event):
		self.SrcTxt.Cut()
		event.Skip()

	def copyit(self, event):
		self.SrcTxt.Copy()
		event.Skip()

	def pastit(self, event):
		self.SrcTxt.Paste()
		event.Skip()

	def slctal(self, event):
		self.SrcTxt.SelectAll()
		event.Skip()

	def clos_lin(self, event):
		self.SrcTxt.AddText("\t\tq = self.GetParent()\n\t\tq.Close()\n")
		event.Skip()

	def get_lin(self, event):
		self.AnalizFile()
		if self.ctltxt == [] and self.chosls == [] and self.chkbox == [] and self.rdobox == [] and self.rdobtn == [] and self.spinct==[] and self.spincd == []:
			wx.MessageBox(_(u'No any part of Panel for get data! Please use one of this object: \
		                  wx.TextCtrl wx.Choice wx.CheckBox wx.RadioBox'))
		else:
			i = 0
			for obj in self.ctltxt:
				self.SrcTxt.AddText("\t\tD%s = " % str(i) + obj + ".GetValue()\n")
				i += 1
			for obj in self.chosls:
				self.SrcTxt.AddText("\t\tD%s = " % str(i) + obj + ".GetSelection()\n")
				i += 1
			for obj in self.chkbox:
				self.SrcTxt.AddText("\t\tD%s = " % str(i) + obj + ".GetValue()\n")
				i += 1
			for obj in self.rdobox:
				self.SrcTxt.AddText("\t\tD%s = " % str(i) + obj + ".GetSelection()\n")
				i += 1
			for obj in self.rdobtn:
				self.SrcTxt.AddText("\t\tD%s = " % str(i) + obj + ".GetValue()\n")
				i += 1

			for obj in self.spinct:
				self.SrcTxt.AddText("\t\t" + obj + ".GetValue( )\n" )
				i += 1
			for obj in self.spincd:
				self.SrcTxt.AddText("\t\t" + obj + ".GetValue( )\n" )
				i += 1

		self.SrcTxt.AddText("\t\t#### you can return data in your own format here ###\n")
		event.Skip()

	def put_lin(self, event):
		self.AnalizFile()
		if self.ctltxt == [] and self.chosls == [] and self.chkbox == [] and self.rdobox == [] and self.rdobtn == [] and self.spinct==[] and self.spincd == []:
			wx.MessageBox(_(u'No any part of Panel for Put data! Please use one of this object: \
				                  wx.TextCtrl wx.Choice wx.CheckBox wx.RadioBox wx.RadioButton'))
		else:

			self.SrcTxt.AddText("\t\t#Data = [] #Put your data in list or use at argumant in function\n")
			i = 0
			for obj in self.ctltxt:
				self.SrcTxt.AddText("\t\t"  + obj + ".SetValue( Data[%s] )\n" % str(i) )
				i += 1
			for obj in self.chosls:
				self.SrcTxt.AddText("\t\t"  + obj + ".SetSelection( Data[%s] )\n" % str(i) )
				i += 1
			for obj in self.chkbox:
				self.SrcTxt.AddText("\t\t"  + obj + ".SetValue( Data[%s] )\n" % str(i) )
				i += 1
			for obj in self.rdobox:
				self.SrcTxt.AddText("\t\t"  + obj + ".SetSelection( Data[%s] )\n" % str(i) )
				i += 1
			for obj in self.rdobtn:
				self.SrcTxt.AddText("\t\t"  + obj + ".SetValue( Data[%s] )\n" % str(i) )
				i += 1
			for obj in self.spinct:
				self.SrcTxt.AddText("\t\t" + obj + ".SetValue( Data[%s] )\n" % str(i) )
				i += 1
			for obj in self.spincd:
				self.SrcTxt.AddText("\t\t" + obj + ".SetValue( Data[%s] )\n" % str(i) )
				i += 1


		event.Skip()

	def null_lin(self, event):
		self.AnalizFile()
		if self.ctltxt == [] and self.chosls == [] and self.chkbox == [] and self.rdobox == []:
			wx.MessageBox(_(u'No any part of Panel for Put data! Please use one of this object: \
						                  wx.TextCtrl wx.Choice wx.CheckBox wx.RadioBox'))
		else:
			self.SrcTxt.AddText("\t\t#Data = [u'',u'',...] #Put empty data in list\n")
			self.SrcTxt.AddText("\t\t#self.PutData( Data ) #Send empty data to Put Data Function\n")

		event.Skip()

	def AnalizFile(self):
		self.ctltxt = []
		self.chkbox = []
		self.rdobox = []
		self.rdobtn = []
		self.chosls = []
		self.spinct = []
		self.spincd = []
		lins = self.SrcTxt.GetLineCount()
		for l in range(lins):
			if u'wx.TextCtrl' in self.SrcTxt.GetLine(l):
				self.ctltxt.append(self.SrcTxt.GetLineText(l).split('=')[0].lstrip('\t').rstrip(' '))
			if u'wx.Choice' in self.SrcTxt.GetLine(l):
				self.chosls.append(self.SrcTxt.GetLineText(l).split('=')[0].lstrip('\t').rstrip(' '))
			if u'wx.CheckBox' in self.SrcTxt.GetLine(l):
				self.chkbox.append(self.SrcTxt.GetLineText(l).split('=')[0].lstrip('\t').rstrip(' '))
			if u'wx.RadioBox' in self.SrcTxt.GetLine(l):
				self.rdobox.append(self.SrcTxt.GetLineText(l).split('=')[0].lstrip('\t').rstrip(' '))
			if u'wx.RadioButton' in self.SrcTxt.GetLine(l):
				self.rdobtn.append(self.SrcTxt.GetLineText(l).split('=')[0].lstrip('\t').rstrip(' '))
			if u'wx.SpinCtrl' in self.SrcTxt.GetLine(l):
				self.spinct.append(self.SrcTxt.GetLineText(l).split('=')[0].lstrip('\t').rstrip(' '))
			if u'wx.SpinCtrlDouble' in self.SrcTxt.GetLine(l):
				self.spincd.append(self.SrcTxt.GetLineText(l).split('=')[0].lstrip('\t').rstrip(' '))

	def impnum(self, event):
		self.SrcTxt.AddText(u"import numpy as np \n")

	def impmat(self, event):
		self.SrcTxt.AddText(u"from matplotlib import pyplot as plot \n")

	def impa3d(self, event):
		self.SrcTxt.AddText(u"from mpl_toolkits.mplot3d import Axes3D \n")


	def impmlu(self, event):
		pass

	def getCurntLineNumber(self):
		print(self.SrcTxt.gtcurLine())

	def idlebat(self, event):
		for pth in sys.path:
			if 'lib' in pth[-3:]:
				os.system(pth + "\\idlelib\\" + "idle.bat")

# def toML(self, event):
	# 	print(self.pnl.pyFile)
	# 	ifil = self.pnl.pyFile.split('\\')[-1].replace(u'.py',u'')
	# 	print(ifil)
	# 	if self.pnl.pyFile == GUI_PATH+u'Temp\\untitle.py':
	# 		wx.MessageBox(_(u'Please save your work then Do this perosse.'))
	# 		self.savasit(event)
	# 	elif self.pnl.pyFile == GUI_PATH+u'Temp\\Muntitle.py':
	# 		wx.MessageBox(_(u'Please save your work then Do this perosse.'))
	# 		self.savasit(event)
	# 	else:
	# 		print(self.DfDir)
	# 		MLpnl = self.GetGrandParent()
	# 		if self.DfDir == Src_mlp: #SRC_PATH+u'mlp\\':
	# 			mylstml = MLpnl.getMData.AllML(u'join MLPane on MLinfo.MLPid = MLPane.MLPid')
	# 			print(mylstml)
	# 			tclslct = MLpnl.TLC1.GetSelection()
	# 			if MLpnl.getMData.MLPansFils(u" where MLPane.MLPfile = '%s' " %ifil ) != []:
	# 				wx.MessageBox(_(u'File is exist please change it'))
	# 			else:
	# 				lebls = [u'Par. Pane Name', u'Par. Pane code', u'Par. Pane file']
	# 				data = [ifil]
	# 				dlg = wx.Dialog(self.GetFrame(), -1)
	# 				pnl = MyPanel4(dlg, lebls, data)
	# 				dlg.SetSize((480, 190))
	# 				dlg.SetLabel(_(u'Add MLA to List'))
	# 				dlg.ShowModal()
	# 				if pnl.acpt:
	# 					algnm = pnl.fld1.GetValue()
	# 					algcd = pnl.fld2.GetValue()
	# 					algid = pnl.fld4.GetValue()
	# 				dlg.Destroy()
	# 				#print(algid, algnm, algcd)
	# 				#print(MLpnl.codings)
	# 				if algnm != u'' or algcd != u'' or algid != u'':
	# 					if int(algid) > MLpnl.codings[0] and int(algid) < MLpnl.codings[1]:
	# 						#print(u'to database')
	# 						#MLpnl.setMDate.Table = u'MLinfo'
	# 						#MLpnl.setMDate.Additem(u' MLPid, MLname, MLcod', [int(algid), algnm, algcd])
	# 						MLpnl.setMDate.Table = u'MLPane'
	# 						MLpnl.setMDate.Additem(u' MLPid, MLPfile', [algid, ifil])
	# 						wx.MessageBox(_(u'Your source Add to list Successfully.'))
	# 					else:
	# 						wx.MessageBox(_(u'Please attend to coding range!'))
	# 				else:
	# 					wx.MessageBox(_(u'Some fields is empty or wrong ! try again!'))
	#
	#
	# 		if self.DfDir == Src_mla: #SRC_PATH+u'mla\\':
	# 			mylstml = MLpnl.getMData.AllML(u'join MLAlgo on MLAlgo.MLcod = MLinfo.MLcod')
	# 			print(mylstml)
	# 			tclslct = MLpnl.TLC1.GetSelection()
	# 			#algnm = MLpnl.TLC1.GetItemText(tclslct, 0)
	# 			#algcd = MLpnl.TLC1.GetItemText(tclslct, 1)
	# 			if MLpnl.getMData.MLAlgoFils(u" where MLAlgo.MLAsrc = '%s' " %ifil ) != []:
	# 				wx.MessageBox(_(u'File is exist please change it'))
	# 			else:
	# 				lebls = [u'Algorithm Name', u'Algorithm Code', u'Algorithm file']
	# 				data = [ifil]
	# 				dlg = wx.Dialog(self.GetFrame(), -1)
	# 				pnl = MyPanel4(dlg, lebls, data)
	# 				dlg.SetSize((480, 190))
	# 				dlg.SetLabel(_(u'Add MLA to List'))
	# 				dlg.ShowModal()
	# 				if pnl.acpt:
	# 					algnm = pnl.fld1.GetValue()
	# 					algcd = pnl.fld2.GetValue()
	# 					algid = pnl.fld4.GetValue()
	# 				dlg.Destroy()
	# 				#print(algid,algnm,algcd)
	# 				#print(MLpnl.codings)
	# 				if algnm != u'' or algcd != u'' or algid != u'':
	# 					if int(algid) > MLpnl.codings[0] and int(algid) < MLpnl.codings[1]:
	# 						#print(u'to database')
	# 						MLpnl.setMDate.Table = u'MLinfo'
	# 						MLpnl.setMDate.Additem(u' MLPid, MLname, MLcod',[int(algid), algnm, algcd])
	# 						MLpnl.setMDate.Table = u'MLAlgo'
	# 						MLpnl.setMDate.Additem(u' MLcod, MLAsrc',[algcd, ifil])
	# 						wx.MessageBox(_(u'Your source Add to list Successfully.'))
	# 					else:
	# 						wx.MessageBox(_(u'Please attend to coding range!'))
	# 				else:
	# 					wx.MessageBox(_(u'Some fields is empty or wrong ! try again!'))



			#print(MLpnl.getMData.AllML(u' join MLPane on MLinfo.MLPid = MLPane.MLPid join MLAlgo on MLAlgo.MLcod = MLinfo.MLcod'))
			#print(MLpnl.TLC1.GetSelection())
			#tclslct = MLpnl.TLC1.GetSelection()
			#print(MLpnl.TLC1.GetItemText(tclslct,0))
			#print(MLpnl.TLC1.GetItemText(tclslct, 1))
			#print(MLpnl.ChsBok.GetChoiceCtrl())

			#lebls = [u'Par. Pane Name',u'Par. Pane code',u'Par. Pane file']
			#lebls = [u'Algorithm Name',u'Algorithm Code',u'Algorithm file']
			#data = []
			#dlg = wx.Dialog(self.GetFrame(), -1)
			#pnl = MyPanel4(dlg,lebls,data)
			#dlg.SetSize((480,190))
			#dlg.SetLabel(u'Add MLA to List')
			#dlg.ShowModal()
			#dlg.Destroy()

	# def tst(self, event):
	# 	event.Skip()
