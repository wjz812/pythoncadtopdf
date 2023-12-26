from pyautocad import Autocad,APoint
import os
import time


filedir = 'D:/Desktop/test/'
savedir = "D:/Desktop/result/"
dwglist = os.listdir(filedir)

for i in range(0,len(dwglist)):
	filepath = os.path.join(filedir,dwglist[i])
	pdffile = Autocad(filepath)
	filename = os.path.splitext(dwglist[i])[0]
	print('processing file:',filename)
	pdffile.doc.Application.Documents.Open(filepath)
	pdffile.doc.ActiveLayout.ConfigName = "DWG to PDF.pc3"
	savename = os.path.join(savedir,filename)
	pdffile.doc.Plot.PlotToFile(savename)
	#pdffile.doc.SaveAs(savename)
	if i == 0:
		time.sleep(90)
	else:
		time.sleep(60)
		pdffile.doc.Close(False)
