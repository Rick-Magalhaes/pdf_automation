import os
from readers.pdf_reader import PDFReader
from habite_se_parser import HabiteSeParser
from readers.docx_reader import DocxReader

class BatchProcessor:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path

    def process(self) -> list[dict]:
        results = []

        for file in os.listdir(self.folder_path):
            file_lower = file.lower()
            path = os.path.join(self.folder_path, file)

            try:
                if file_lower.endswith(".pdf"):
                    reader = PDFReader(path)
                elif file_lower.endswith(".docx"):
                    reader = DocxReader(path)
                else:
                    continue

                text = reader.extract_text()
                # TESTE DE SANIDADE (comentado):
                # Detecta documentos sem camada de texto (provável scan)
                # if not text.strip():
                #     print("Documento sem camada de texto (provável scan)")
                """print("ARQUIVO:", file)
                print("TAMANHO TEXTO:", len(text))
                print(text[:300])
                print("-" * 40)
                if not text.strip():
                    print("Documento sem camada de texto (provável scan)")"""

                parser = HabiteSeParser(text)
                data = parser.extract()
                data["arquivo"] = file

                results.append(data)

            except Exception as e:
                print(f"Erro no arquivo {file}: {e}")

        return results
