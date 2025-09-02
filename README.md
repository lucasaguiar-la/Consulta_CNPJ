# Consulta CNPJ

Este projeto realiza consultas de CNPJs, extrai dados relevantes e salva os resultados em planilhas Excel.

## Estrutura do Projeto

- `main.py`: Arquivo principal para execução da aplicação.
- `src/`: Módulo com scripts de extração, manipulação e salvamento de dados.
  - `extrai_dados.py`: Funções para extrair dados dos CNPJs.
  - `inicia_app.py`: Inicializa o fluxo principal da aplicação.
  - `salva_planilha.py`: Salva os dados extraídos em planilhas Excel.
  - `utils.py`: Funções utilitárias.
- `api/`: Scripts para consulta de CNPJ via API.
- `planilhas/`: Pasta para armazenar planilhas de entrada e saída.
  - `raw/`: Planilhas originais para consulta.
  - `salvas/`: Planilhas geradas pela aplicação.
- `requirements.txt`: Dependências do projeto.

## Como executar

1. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```
2. Execute o arquivo principal:
   ```powershell
   python main.py
   ```

## Funcionalidades
- Consulta de CNPJs via API.
- Extração e tratamento dos dados consultados.
- Salvamento dos resultados em planilhas Excel.

## Requisitos
- Python 3.11+
- Pacotes listados em `requirements.txt`

## Observações
- As planilhas de entrada devem ser colocadas em `planilhas/raw/`.
- As planilhas geradas serão salvas em `planilhas/salvas/`.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.