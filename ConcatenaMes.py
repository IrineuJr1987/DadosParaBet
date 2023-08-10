import os
import pandas as pd
from datetime import datetime, timedelta

def obter_ano_mes_anterior():
    data_atual = datetime.now()
    primeiro_dia_do_mes_atual = data_atual.replace(day=1)
    ultimo_dia_do_mes_anterior = primeiro_dia_do_mes_atual - timedelta(days=1)
    ano_mes_anterior = ultimo_dia_do_mes_anterior.strftime('%Y-%m')
    return ano_mes_anterior

def verificar_e_concatenar_arquivos_xlsx(pasta_origem, pasta_destino):
    ano_mes_anterior = obter_ano_mes_anterior()

    arquivos_xlsx = [arquivo for arquivo in os.listdir(pasta_origem) if arquivo.endswith('.xlsx') and arquivo.startswith('2023-07')]

    if not arquivos_xlsx:
        print("Nenhum arquivo encontrado para o ano e mês anterior.")
        return

    dados_concatenados = pd.DataFrame()

    for arquivo in arquivos_xlsx:
        caminho_arquivo = os.path.join(pasta_origem, arquivo)
        dados = pd.read_excel(caminho_arquivo)
        dados_concatenados = pd.concat([dados_concatenados, dados], ignore_index=True)

    caminho_arquivo_concatenado = os.path.join(pasta_destino, f'{ano_mes_anterior}_dados_concatenados.xlsx')
    dados_concatenados.to_excel(caminho_arquivo_concatenado, index=False)

    print(f"Dados dos arquivos do mês anterior foram concatenados e salvos em '{caminho_arquivo_concatenado}'.")

# Pasta que contém os arquivos XLSX
pasta_origem = f'ApostasGeradas'

# Pasta onde será salvo o arquivo XLSX concatenado
pasta_destino = f'ApostasGeradas\\MesFechado'

verificar_e_concatenar_arquivos_xlsx(pasta_origem, pasta_destino)
