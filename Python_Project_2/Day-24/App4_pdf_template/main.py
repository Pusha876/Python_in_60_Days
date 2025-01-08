from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Sets the header
    pdf.set_font("Arial", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 20, 200, 20)

    # Sets the footer
    pdf.ln(262)
    pdf.set_font("Arial", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Sets the footer
        pdf.ln(274)
        pdf.set_font("Arial", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

pdf.output("output.pdf")
