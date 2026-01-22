import pdfplumber
from pathlib import Path


class PDFReader:
    def __init__(self, pdf_path: str):
        self.pdf_path = Path(pdf_path)

    def extract_text(self) -> str:
        full_text = ""

        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"

        return full_text