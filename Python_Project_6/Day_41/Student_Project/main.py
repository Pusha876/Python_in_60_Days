from fpdf import FPDF
import pandas

df = pandas.read_csv("articles.csv", dtype={"id": str, "price": str})


class Equipment:
    def __init__(self, equipment_id):
        self.equipment_id = equipment_id
        self.name = df.loc[df["id"] == self.equipment_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.equipment_id, "price"].squeeze()

    def available_equipment(self):
        """Check if the equipment is available for purchase."""
        in_stock = df.loc[df["id"] == self.equipment_id, "in stock"].squeeze()
        return in_stock


class PurchaseTicket:
    def __init__(self, equipment):
        self.equipment = equipment

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.equipment}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Equipment: {self.equipment.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.equipment.price}", ln=1)

        pdf.output("receipt.pdf")


print(df)
equipment_id = input("Enter the equipment id: ")
equipment = Equipment(equipment_id)
if equipment.available_equipment():
    receipt = PurchaseTicket(equipment)
    receipt.generate()
else:
    print("The equipment is not available.")
