import pandas as pd

class ExcelExporter:
    def __init__(self, output_path: str):
        self.output_path = output_path

    def export(self, data: list[dict]):
        df = pd.DataFrame(data)
        df.to_excel(self.output_path, index=False)
