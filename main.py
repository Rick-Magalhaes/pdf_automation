from batch_processor import BatchProcessor
from exporter import ExcelExporter

def main():
    processor = BatchProcessor("data")
    data = processor.process()

    exporter = ExcelExporter("output/processados.xlsx")
    exporter.export(data)

    print(f"{len(data)} arquivos processados com sucesso.")

if __name__ == "__main__":
    main()
