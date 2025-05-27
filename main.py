from fpdf import FPDF
import pandas as pd

# Importing the FPDF method
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Importing the pandas read csv file
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():

    # Add pdf file or page
    pdf.add_page()

    # Setting the font of the pdf file or page
    pdf.set_font(family="Times", style="B", size=24)

    # Setting the text color
    pdf.set_text_color(100, 100, 100)

    # Adding a title using a cell
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # adding a line
    pdf.line(10, 21, 200, 21)

    # Adding a multipage of the pdf reading from the csv file
    for i in range(row["Pages"] - 1):
        pdf.add_page()

# printing the output pdf file
pdf.output("output.pdf")