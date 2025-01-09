import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    name = filename.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=name, ln=1)

    # Read the content of the file
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
    # Add the content to the pdf
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=10, txt=content)

pdf.output("output.pdf")
