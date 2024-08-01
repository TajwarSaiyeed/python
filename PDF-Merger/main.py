import PyPDF2

merger = PyPDF2.PdfWriter()
pdfs = ['1.pdf', '2.pdf', '3.pdf']
for pdf in pdfs:
    merger.append(pdf)

merger.write('result.pdf')
merger.close()

