from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io
def pdftotxt(inPDFfile,outtxtFile):
    inFile = open(inPDFfile,'rb')
    resMgr = PDFResourceManager()
    retData = io.StringIO()
    TxtConverter = TextConverter(resMgr,retData,laparams=LAParams())
    interpreter = PDFPageInterpreter(resMgr,TxtConverter)

    #To transform each page in pdf file
    for page in PDFPage.get_pages(inFile):
        interpreter.process_page(page)

    txt = retData.getvalue()
    #To Save output data as text
    with open(outtxtFile, 'w') as f:
        f.write(txt)
#main call
inPDFfile = "inpuPDFfilename" #type your input filename with .pdf extension example '123.txt'
outtxtFile =  "outputfilename" #Put you output you want file with .txt extension example '123.txt'
pdftotxt(inPDFfile, outtxtFile)