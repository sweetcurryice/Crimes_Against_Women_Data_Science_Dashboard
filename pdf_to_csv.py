import tabula

#lets read the data from pdf into DataFrame
pdf_file = (r"Victims of Rape under Different Age-Groups During 2015 (StateUT-Wise).pdf")

output_csv = (r"Victims of Rape under Different Age-Groups During 2015.csv")

df = tabula.read_pdf(input_path = pdf_file, pages = 'all')
tabula.convert_into(input_path = pdf_file, output_path = output_csv, output_format = 'csv', pages = 'all', stream = True)