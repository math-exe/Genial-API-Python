from db import create_connection, insert_data
from api import api_consult
from processing import date_generator, processing_data

def main():

    # Crie a conexão com o SQL Server
    conexao = create_connection()

    # Gere as datas de início e término em intervalos de 15 dias até a data atual
    for start_date, finish_date in date_generator():
        # Formate as datas como strings no formato desejado
        start_date = start_date
        finish_date = finish_date

        # Consultar a API para o intervalo de datas atual
        dados_api = api_consult(start_date, finish_date)

        if dados_api:
            # Processar os dados da API
            dados_processados = processing_data(dados_api)

            # Inserir os dados no SQL Server
            insert_data(conexao, dados_processados)

    conexao.close()

if __name__ == '__main__':
    main()
