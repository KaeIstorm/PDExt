import PyPDF2

#Open the pdf file, and create the txt file in append mode
f=open('file.pdf', 'rb')
file=open('file.txt', 'a+')

#Read PDF content and copy into a list
PDFReader=PyPDF2.PdfReader(f)
pdfContent=[]
for i in range(len(PDFReader.pages)):
    page=PDFReader.pages[i]
    pdfContent.append(page.extract_text())

#Append PDF content to TXT file
for p in pdfContent:
    file.write(p)

f.close()
file.close()