from fpdf import FPDF
import os


class PDF(FPDF):
    def header(self):
        # Optional: add a header or set font for the title if you need
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Mask out result from RAG system", 0, 1, "C")

    def chapter_title(self, title):
        # Add a chapter title
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, 0, 1, "C")

    def chapter_body(self, body):
        # Add the body text
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, body)
        self.ln()  # Line break


def pdf_gen(response):

    # File path
    file_path = "result.pdf"
    # Check if the file exists
    if os.path.exists(file_path):
        # If it exists, delete it
        os.remove(file_path)
    # Create instance of FPDF class
    pdf = PDF()

    # Add a page
    pdf.add_page()

    # Set title
    pdf.chapter_title("Mask out result from RAG system")

    # Example response from your query function
    # response = "Your response text from the RAG system would be displayed here."

    # Adding the response to the PDF
    pdf.chapter_body(response)

    # Save the pdf with name .pdf
    pdf.output(file_path)

    return
