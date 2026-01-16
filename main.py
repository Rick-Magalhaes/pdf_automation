from batch_processor import BatchProcessor
from exporter import ExcelExporter

def main():
    processor = BatchProcessor("data/pdfs")
    data = processor.process()

    exporter = ExcelExporter("output/habite_se.xlsx")
    exporter.export(data)

    print(f"{len(data)} arquivos processados com sucesso.")

if __name__ == "__main__":
    main()
