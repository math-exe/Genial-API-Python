import pyodbc
import json

with open ('config.json') as config_file:
    config = json.load(config_file)

server = config['server']
database = config['database']
user_db = config['user_db']
password_db = config['password_db']

def create_connection():
    return pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'f'Server={server};Database={database};UID={user_db};PWD={password_db}')

def insert_data(conexao, dados):
    cursor = conexao.cursor()

    for item in dados:
        columns = ['chaveAcesso', 'status', 'nomeEmitente', 'cnpjEmitente',
                   'nomeDestinatario', 'cnpjDestinatario', 'dataEmissao',
                   'numero', 'serie', 'valor', 'baseIcms', 'valorIcms', 'situacaoNota']

        query = f"INSERT INTO GENIAL_XML ({', '.join(columns)}) VALUES ({', '.join(['?'] * len(columns))})"

        # Obtenha os valores dos itens em uma lista na ordem correta
        values = [item[column] for column in columns]

        # Executar a query SQL
        cursor.execute(query, values)
        conexao.commit()

    conexao.commit()
