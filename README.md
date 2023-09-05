# Genial API Data Fetcher

Este é um projeto em Python que automatiza a consulta à API do Sistema Genial para coletar e processar dados em formato XML, em seguida, inserindo esses dados em um banco de dados SQL Server. O projeto é composto por vários módulos.

## Funcionalidades Principais

### `main.py`

Este módulo principal coordena todo o processo de coleta e inserção de dados. Ele realiza o seguinte:

1. Cria uma conexão com o SQL Server.
2. Gera datas de início e término em intervalos de 15 dias até a data atual.
3. Consulta a API do Sistema Genial para cada intervalo de datas.
4. Processa os dados da API.
5. Insere os dados processados no SQL Server.

### `api.py`

Este módulo lida com a consulta à API do Sistema Genial. Ele inclui:

- Autenticação com base em informações fornecidas no arquivo `config.json`.
- Consulta à API com datas de início e término.

### `processing.py`

Este módulo contém funções para processar os dados da API. Ele inclui:

- Geração de datas em intervalos de 15 dias.
- Processamento específico dos dados da API, selecionando apenas os campos necessários.

### `db.py`

Este módulo é responsável pela conexão e inserção de dados no banco de dados SQL Server. Ele inclui:

- Criação de uma conexão com o SQL Server com base nas informações fornecidas no arquivo `config.json`.
- Inserção dos dados processados no banco de dados.

## Configuração

Antes de executar o projeto, certifique-se de configurar as informações necessárias no arquivo `config.json`, incluindo a chave da API, informações de conexão do SQL Server e outras configurações relevantes.

## Uso

Para executar o projeto, siga os passos abaixo:

1. Clone o repositório.
2. Certifique-se de que todas as dependências estejam instaladas.
3. Configure o arquivo `config.json` com suas informações.
4. Execute o arquivo `main.py`.

## Dependências

O projeto depende das seguintes bibliotecas Python:

- `requests`
- `pyodbc`

## Contribuição

Se você deseja contribuir para este projeto, sinta-se à vontade para abrir problemas (issues) ou enviar pull requests com melhorias.

## Licença

Este projeto está sob a licença [MIT](LICENSE).
