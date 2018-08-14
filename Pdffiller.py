from PyPDF2 import PdfFileWriter, PdfFileReader

datas = {'name':'Sudhichai'}
generated_pdf = pypdftk.fill_form('/Users/sudhichaiungsuthornrungsi/Downloads/f1040re.pdf', datas)
out_pdf = pypdftk.concat(['/path/to/cover.pdf', generated_pdf])