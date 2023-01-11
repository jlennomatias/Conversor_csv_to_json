import csv, json
from formatador_json import *

def csv_para_dados(caminho):
    dados = []

    with open(caminho, "r") as arquivo_csv:
        csv_file = csv.reader(arquivo_csv)
        for marca, nome_da_sociedade, cnpj_sociedade, nome_prestador, cnpj_prestador, code_product, name_product, coverages, endereco_completo, complemento, bairro, municipio, codigo_IBGE_municipio, sigla_unidade_federacao, cep, pais, codigo_pais, latitude, longitude, horario_abertura, horario_funcionamento, horario_encerramento, dias_funcionamento, indicador_resstricao_acesso, tipo_telefone, ddi, ddd, numero_telefone, tipo_prestacao_servicos, nome_servicos_prestados, descricao_servicos_prestados, *resto in csv_file:

            if not dados:
                dados.append(criar_json(marca, nome_da_sociedade, cnpj_sociedade, nome_prestador, cnpj_prestador, code_product, name_product, coverages, endereco_completo, complemento, bairro, municipio, codigo_IBGE_municipio, sigla_unidade_federacao, cep, pais, codigo_pais, latitude, longitude, horario_abertura, horario_funcionamento, horario_encerramento, dias_funcionamento, indicador_resstricao_acesso, tipo_telefone, ddi, ddd, numero_telefone, tipo_prestacao_servicos, nome_servicos_prestados, descricao_servicos_prestados))
            else:
                dados = inserir_json(marca, nome_da_sociedade, cnpj_sociedade, nome_prestador, cnpj_prestador, code_product, name_product, coverages, endereco_completo, complemento, bairro, municipio, codigo_IBGE_municipio, sigla_unidade_federacao, cep, pais, codigo_pais, latitude, longitude, horario_abertura, horario_funcionamento, horario_encerramento, dias_funcionamento, indicador_resstricao_acesso, tipo_telefone, ddi, ddd, numero_telefone, tipo_prestacao_servicos, nome_servicos_prestados, descricao_servicos_prestados, dados)

    return dados

def dados_para_json(dados, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo_json:
        arquivo_json.write(json.dumps(dados, ensure_ascii=False, indent=4))
