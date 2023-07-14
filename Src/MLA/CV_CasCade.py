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

import os
import sys
from Config.Init import *


def MakeBGtxt(bgpath):
	lstfil = os.listdir(bgpath)
	with open(Src_mla+'Dataset\\'+'bg.txt', 'a+', encoding='utf-8') as f:
		for bgf in lstfil:
			f.write(bgpath.replace(Src_mla+'Dataset','')+"\\"+bgf+'\n')


def Makepngout(image, bgfil, infofil, pngoutpth, maxxa, maxya, maxza, num):
	arguman1 = " -img "+image+" -bg "+bgfil+" -info "+infofil+" -pngoutput "+pngoutpth
	arguman2 = " -maxxangle "+str(maxxa)+" -maxyangle "+str(maxya)+" -maxzangle "+str(maxza)+" -num "+str(num)
	command = 'cmd /c "%sHaarTraining\\bin\\createsamples.exe" '%Src_api
	#print(command+arguman1+arguman2)
	os.system(command+arguman1+arguman2)

def MakePosVector(infofil, num, width, height, vecfil):
	arguman1 = " -info "+infofil+" -num "+str(num)+" -w "+str(width)+" -h "+str(height)+" -vec "+vecfil
	command = 'cmd /c "%sHaarTraining\\bin\\createsamples.exe" ' % Src_api
	os.system(command+arguman1)

def TrainCasCade(datapth , vecfil, bgfil, numpos, numneg, numstg, width, height):
	arguman1 = " -data "+datapth+" -vec "+vecfil+" -bg "+bgfil
	arguman2 = " -npos "+str(numpos)+" -nneg "+str(numneg)+" -nstages "+str(numstg)+" -w "+str(width)+" -h "+str(height)
	command = 'cmd /c "%sHaarTraining\\bin\\haartraining.exe" ' %Src_api
	os.system(command + arguman1 + arguman2)
