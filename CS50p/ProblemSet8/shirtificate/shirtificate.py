from PIL import Image
from fpdf import FPDF
import sys


shirt_path = "shirtificate.png"
shirt = Image.open(shirt_path)
image_width = shirt.size[0] * 0.25  # Adjust the factor as per your requirement
image_height = shirt.size[1] * 0.25  # Adjust the factor as per your requirement


class PDF(FPDF):
    def header(self):
        # Calculate x position to center image
        x = (210 - image_width) / 2  # 210 is the width of an A4 page in mm
        self.image(shirt_path, x, 110, image_width, image_height)
        self.set_font("helvetica", "B", 50)
        # Printing title:
        self.cell(0, 60, "CS50 Shirtificate", align="C")





# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.set_margins(1,1)


# Get the text from the command-line argument
text = sys.argv[1] if len(sys.argv) > 1 else ""
text = "{} took CS50".format(text)
# Add the text to the PDF
pdf.set_font("Times", size=30)
pdf.set_text_color(255,255,255)
pdf.cell(20, 250, text,align="C", ln=True)
pdf.output("shirtificate.pdf")


