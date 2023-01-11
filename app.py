from convertApi import *

caminho_csv = 'csv/referenced.csv'
caminho_json = 'json/referenced.json'

dados_para_json(csv_para_dados(caminho_csv), caminho_json)