import webbrowser
import os
from fpdf import FPDF
from filestack import Client
from dotenv import dotenv_values

class PdfReport:
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay_str = str(flatmate1.pays(bill=bill, co_flatmate=flatmate2))
        flatmate2_pay_str = str(flatmate2.pays(bill=bill, co_flatmate=flatmate1))
        # Create a PDF document
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("./files/house.png", w=30, h=30)

        # Set font and size
        pdf.set_font("Times", size=24, style='B')

        # Add text to the PDF
        pdf.cell(0, 60, border=1, txt="Flatmates Bill Calculator", ln=True, align='C')

        pdf.set_font("Times", size=15, style='')
        pdf.cell(120, 30, border=1, txt="Period:")
        pdf.cell(0, 30, border=1, txt=bill.period, ln=True)

        pdf.cell(120, 30, border=1, txt=flatmate1.name)
        pdf.cell(0, 30, border=1, txt=flatmate1_pay_str, ln=True)

        pdf.cell(120, 30, border=1, txt=flatmate2.name)
        pdf.cell(0, 30, border=1, txt=flatmate2_pay_str, ln=True)

        # Save the PDF to a file
        output_path = os.path.join(os.getcwd(), 'output', self.filename)
        pdf.output(output_path)

        webbrowser.open(output_path)
        return output_path





class FileSharer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.api_key = dotenv_values('./.env')['FILESTACK_API_KEY']

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url