from db import create_connection, insert_data
from api import api_consult
from processing import date_generator, processing_data

def main():

    # Crie a conexão com o SQL Server
    conexao = create_connection()

    conexao.execute('TRUNCATE TABLE GENIAL_XML')

    # Gere as datas de início e término em intervalos de 15 dias até a data atual
    for start_date, finish_date in date_generator():
        # Formate as datas como strings no formato desejado
        start_date = start_date
        finish_date = finish_date

        qtde_linhas = 0
        tentativas = 0

        while qtde_linhas == 0 and tentativas < 3:
            # Consulte a API para o intervalo de datas atual
            dados_api = api_consult(start_date, finish_date)

            print(f'Consultando dados de {start_date} até {finish_date}')

            if dados_api:
                # Processar os dados da API
                dados_processados = processing_data(dados_api)

                qtde_linhas = len(dados_processados)

                # Inserir os dados no SQL Server
                insert_data(conexao, dados_processados)

                print(f'Linhas inseridas {qtde_linhas}')

            tentativas += 1

    conexao.close()

    print('Conexão Finalizada!')

if __name__ == '__main__':
    main()
