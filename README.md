PDF Automation – Extração de Dados para Excel

Este projeto é uma automação em Python para processar grandes volumes de arquivos PDF, extrair informações específicas por meio de expressões regulares e exportar os dados consolidados para uma planilha Excel.

O foco do projeto é resolver problemas reais de trabalho manual repetitivo, especialmente em contextos administrativos, imobiliários e públicos.
--------------------------------------------------------------------------------------------------------------------------------------------------------
 Funcionalidades

Leitura automática de múltiplos PDFs em lote

Extração de texto de PDFs digitais

Identificação e extração de campos específicos:

Tipo do documento (ex: Habite-se ou Alvará)

Número do documento

Data de conclusão

Número de inscrição cadastral

Processamento tolerante a falhas (um PDF com erro não interrompe o lote)

Exportação dos dados para arquivo Excel (.xlsx)

Estrutura de código modular e organizada
----------------------------------------------------------------------------
 Estrutura do Projeto
pdf_automation/
│
├── data/                   # Pasta onde ficam os PDFs
├── batch_processor.py      # Processamento em lote dos arquivos
├── pdf_reader.py           # Leitura e extração de texto dos PDFs
├── habite_se_parser.py     # Extração dos campos via regex
├── exporter.py             # Exportação dos dados para Excel
├── main.py                 # Arquivo principal de execução
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação
----------------------------------------------------------------------------
 Como funciona

O sistema percorre automaticamente a pasta data/

Apenas arquivos .pdf são processados

Cada PDF é:

lido

convertido em texto

analisado para extração dos campos necessários

Os dados são armazenados em memória

Ao final, é gerado um arquivo Excel consolidado

Arquivos inválidos ou com erro são ignorados sem interromper o processo
----------------------------------------------------------------------------
 Requisitos

Python 3.10+

Bibliotecas listadas em requirements.txt

Instalação das dependências:

pip install -r requirements.txt
----------------------------------------------------------------------------
 Como executar

Coloque todos os arquivos PDF na pasta data/

Execute o script principal:

python main.py


Ao final do processamento, o arquivo Excel será gerado automaticamente na pasta do projeto.
----------------------------------------------------------------------------
 Tratamento de erros

Arquivos que não são PDF são ignorados

PDFs corrompidos ou fora do padrão esperado não interrompem o lote

O processamento continua normalmente mesmo em caso de falha individual

 Possíveis melhorias futuras

Log detalhado de arquivos com erro

Barra ou contador de progresso

Suporte a outros tipos de documentos

Interface gráfica simples

Parametrização dinâmica dos campos extraídos
----------------------------------------------------------------------------
 Contexto

Este projeto foi desenvolvido como uma solução prática para automação de tarefas administrativas que envolvem a leitura manual de centenas ou milhares de documentos em PDF.

Ele também serve como projeto de portfólio, demonstrando:

Programação orientada a objetos

Processamento em lote

Uso de expressões regulares

Organização de código para produção
----------------------------------------------------------------------------
 Autor

Henrique Magalhães
GitHub
