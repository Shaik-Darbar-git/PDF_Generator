from fpdf import FPDF
import pandas as pd

# Importing the FPDF method
pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.set_auto_page_break(auto=False, margin=0)

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

    # Adding a footer to the page or pdf file
    pdf.ln(262)

    pdf.set_font(family="Times", style="I", size=12)

    pdf.set_text_color(100, 100, 100)

    pdf.cell(w=0, h=8, txt=row["Topic"], align="R")

    # Adding a multipage of the pdf reading from the csv file
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(274)

        pdf.set_font(family="Times", style="I", size=12)

        pdf.set_text_color(100, 100, 100)

        pdf.cell(w=0, h=8, txt=row["Topic"], align="R")


# printing the output pdf file
pdf.output("output.pdf")