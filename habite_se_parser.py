import re

class HabiteSeParser:
    def __init__(self, text: str):
        self.text = text

    def extract(self) -> dict:
        return {
            "tipo_documento": self._tipo_documento(),
            "numero_documento": self._numero_documento(),
            "data_conclusao": self._data_conclusao(),
            "inscricao_cadastral": self._inscricao_cadastral(),
        }

    def _tipo_documento(self):
        if re.search(r"HABITE-SE", self.text, re.IGNORECASE):
            return "HABITE-SE"
        if re.search(r"ALVAR[ÁA]", self.text, re.IGNORECASE):
            return "ALVARÁ"
        return None

    def _numero_documento(self):
        match = re.search(
        r"(HABITE-SE|ALVAR[ÁA](?: DE CONSTRUÇÃO)?)\s+N[º°]?\s*([\d/]+)",
        self.text,
        re.IGNORECASE
    )
        return match.group(2) if match else None

    def _data_conclusao(self):
        match = re.search(r"(?:foi conclu[ií]da em|projeto aprovado em)\s*(\d{2}/\d{2}/\d{4})", self.text, re.IGNORECASE)
        return match.group(1) if match else None

    def _inscricao_cadastral(self):
        match = re.search(
        r"Inscri[cç][aã]o Cadastral\s*n[º°]?\s*([\d\.\-]+)",
        self.text,
        re.IGNORECASE
    )
        return match.group(1) if match else None
