import pandas
from fpdf import FPDF

df=pandas.read_excel('data.xlsx')
print(df)

for index, row in df.iterrows():
  pdf=FPDF(orientation='P', unit='pt', format='A4')
  pdf.add_page()

  pdf.set_font(family='Times', style='B', size=24)
  pdf.cell(w=0, h=20, txt=row['name'], align='L', ln=1)

  for column in df.columns[1:]:
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100, h=30, txt=f"{column.title()}:")
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100, h=30, txt=row[column], ln=1)

  pdf.output(f"{row['name']}.pdf")
