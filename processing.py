from datetime import datetime, timedelta

def date_generator():
    today = datetime.now()
    delta = timedelta(days=15)
    year = today.year

    start_date = datetime(year, 1, 1)
    
    while start_date <= today:
        finish_date = start_date + delta
        if finish_date > today:
            finish_date = today

        yield start_date.strftime('%Y-%m-%d'), finish_date.strftime('%Y-%m-%d')
        start_date = finish_date + timedelta(days=1)

def processing_data(dados_api):
    processing_data = []
    for item in dados_api:
        # Processamento específico
        processing_data.append({
            'chaveAcesso': item['chaveAcesso'],
            'status': item['status'],
            'nomeEmitente': item['nomeEmitente'],
            'cnpjEmitente': item['cnpjEmitente'],
            'nomeDestinatario': item['nomeDestinatario'],
            'cnpjDestinatario': item['cnpjDestinatario'],
            'dataEmissao': item['dataEmissao'],
            'numero': item['numero'],
            'serie': item['serie'],
            'valor': item['valor'],
            'baseIcms': item['baseIcms'],
            'valorIcms': item['valorIcms'],
            'situacaoNota': item['situacaoNota']
        })
    return processing_data
