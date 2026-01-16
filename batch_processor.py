import os
from pdf_reader import PDFReader
from habite_se_parser import HabiteSeParser

class BatchProcessor:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path

    def process(self) -> list[dict]:
        results = []

        for file in os.listdir(self.folder_path):
            if not file.lower().endswith(".pdf"):
                continue

            path = os.path.join(self.folder_path, file)

            try:
                reader = PDFReader(path)
                text = reader.extract_text()

                parser = HabiteSeParser(text)
                data = parser.extract()
                data["arquivo"] = file  # rastreabilidade

                results.append(data)

            except Exception as e:
                print(f"Erro no arquivo {file}: {e}")

        return results
