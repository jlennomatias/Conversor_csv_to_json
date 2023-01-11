def criar_json(marca, nome_da_sociedade, cnpj_sociedade, nome_prestador, cnpj_prestador, code_product, name_product, coverages, endereco_completo, complemento, bairro, municipio, codigo_IBGE_municipio, sigla_unidade_federacao, cep, pais, codigo_pais, latitude, longitude, horario_abertura, horario_funcionamento, horario_encerramento, dias_funcionamento, indicador_resstricao_acesso, tipo_telefone, ddi, ddd, numero_telefone, tipo_prestacao_servicos, nome_servicos_prestados, descricao_servicos_prestados, *resto):
    return {
        "brand": {
            "name": marca,
            "companies": [
                {
                    "name": nome_da_sociedade,
                    "cnpjNumber": cnpj_sociedade,
                    "identification": [
                        {
                            "name": nome_prestador,
                            "cnpjNumber": cnpj_prestador,
                            "products": [
                                {
                                    "code": code_product,
                                    "name": name_product,
                                    "coverage": [
                                        coverages
                                    ]
                                }
                            ],
                            "postalAddress": [
                                {
                                    "address": endereco_completo,
                                    "additionalInfo": complemento,
                                    "districtName": bairro,
                                    "townName": municipio,
                                    "ibgeCode": codigo_IBGE_municipio,
                                    "countrySubDivision": sigla_unidade_federacao,
                                    "postCode": cep,
                                    "country": pais,
                                    "countryCode": codigo_pais,
                                    "geographicCoordinates": {
                                        "latitude": latitude,
                                        "longitude": longitude
                                        
                                    }
                                }
                            ],
                            "access": [
                                {
                                    "standards": [
                                    {
                                        "openingTime": horario_abertura,
                                        "closingTime": horario_encerramento,
                                        "weekday": dias_funcionamento
                                    }
                                    ],
                                    "restrictionIndicator": indicador_resstricao_acesso,
                                    "phones": [
                                    {
                                        "type": tipo_telefone,
                                        "countryCallingCode": ddi,
                                        "areaCode": ddd,
                                        "number": numero_telefone
                                    }
                                    ]
                                }
                            ],
                            "services": [
                                {
                                    "type": tipo_prestacao_servicos,
                                    "typeOthers": "string",
                                    "name": [
                                        nome_servicos_prestados
                                    ],
                                    "description": descricao_servicos_prestados
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }


def inserir_json(marca, nome_da_sociedade, cnpj_sociedade, nome_prestador, cnpj_prestador, code_product, name_product, coverages, endereco_completo, complemento, bairro, municipio, codigo_IBGE_municipio, sigla_unidade_federacao, cep, pais, codigo_pais, latitude, longitude, horario_abertura, horario_funcionamento, horario_encerramento, dias_funcionamento, indicador_resstricao_acesso, tipo_telefone, ddi, ddd, numero_telefone, tipo_prestacao_servicos, nome_servicos_prestados, descricao_servicos_prestados, arquivo):
    empresa_lista = []
    for empresa in arquivo:
        empresa_lista.append(empresa['brand']['name'])
    if marca in empresa_lista:
        for empresa in arquivo:
            if marca == empresa['brand']['name']:
                companie_lista = []
                for companie in empresa['brand']['companies']:
                    companie_lista.append(companie['name'])
                if nome_da_sociedade in companie_lista:
                    for companie in empresa['brand']['companies']:
                        if nome_da_sociedade == companie['name']:
                            identificate_lista = []
                            for identificate in companie['identification']:
                                identificate_lista.append(identificate['name'])
                            if nome_prestador in identificate_lista:
                                for identificate in companie['identification']:
                                    if nome_prestador == identificate['name']:
                                        products_lista = []
                                        for product in identificate['products']:
                                            products_lista.append(product['name'])
                                        if name_product in products_lista:
                                            for product in identificate['products']:
                                                if name_product == product['name']:
                                                    coverages_lista = []
                                                    for coverage in product['coverage']:
                                                        coverages_lista.append(coverage)
                                                    if coverages not in coverages_lista:
                                                        product['coverage'].append(coverages)
                                        else:
                                            identificate['products'].append(
                                                {
                                                    "code": code_product,
                                                    "name": name_product,
                                                    "coverage": [
                                                        coverages
                                                    ]
                                                }
                                            )
                            else:
                                companie['identification'].append(
                                    {
                                        "name": nome_prestador,
                                        "cnpjNumber": cnpj_prestador,
                                        "products": [
                                            {
                                                "code": code_product,
                                                "name": name_product,
                                                "coverage": [
                                                    coverages
                                                ]
                                            }
                                        ],
                                        "postalAddress": [
                                            {
                                                "address": "Avenida Senador Quintino, 178",
                                                "additionalInfo": "",
                                                "districtName": "Olhos Dagua",
                                                "townName": "Feira de Santana",
                                                "ibgeCode": 2910800,
                                                "countrySubDivision": "BA",
                                                "postCode": 44003677,
                                                "country": "BRASIL",
                                                "countryCode": "BRA"
                                            }
                                        ],
                                        "access": [
                                            {
                                                "standards": [],
                                                "restrictionIndicator": False,
                                                "phones": []
                                            }
                                        ],
                                        "services": [
                                            {
                                                "type": "SERVICO_DE_MANUTENCAO",
                                                "typeOthers": "string",
                                                "name": [
                                                    "CONSERTO_DE_ELETROELETRONICO_LINHA_MARROM"
                                                ],
                                                "description": "Conserto De Eletroeletrônico - Linha Marrom"
                                            }
                                        ]
                                    }
                                )

                else:
                    empresa['companies'].append(
                        {
                            "name": nome_da_sociedade,
                            "cnpjNumber": cnpj_sociedade,
                            "identification": [
                                {
                                    "name": nome_prestador,
                                    "cnpjNumber": cnpj_prestador,
                                    "products": [
                                        {
                                            "code": code_product,
                                            "name": name_product,
                                            "coverage": [
                                                coverages
                                            ]
                                        }
                                    ],
                                    "postalAddress": [
                                        {
                                            "address": "Avenida Senador Quintino, 178",
                                            "additionalInfo": "",
                                            "districtName": "Olhos Dagua",
                                            "townName": "Feira de Santana",
                                            "ibgeCode": 2910800,
                                            "countrySubDivision": "BA",
                                            "postCode": 44003677,
                                            "country": "BRASIL",
                                            "countryCode": "BRA"
                                        }
                                    ],
                                    "access": [
                                        {
                                            "standards": [],
                                            "restrictionIndicator": False,
                                            "phones": []
                                        }
                                    ],
                                    "services": [
                                        {
                                            "type": "SERVICO_DE_MANUTENCAO",
                                            "typeOthers": "string",
                                            "name": [
                                                "CONSERTO_DE_ELETROELETRONICO_LINHA_MARROM"
                                            ],
                                            "description": "Conserto De Eletroeletrônico - Linha Marrom"
                                        }
                                    ]
                                }
                            ]
                        }
                    )

    else:
        arquivo.append(criar_json(marca, nome_da_sociedade, cnpj_sociedade, nome_prestador, cnpj_prestador, code_product, name_product, coverages, endereco_completo, complemento, bairro, municipio, codigo_IBGE_municipio, sigla_unidade_federacao, cep, pais, codigo_pais, latitude, longitude, horario_abertura, horario_funcionamento, horario_encerramento, dias_funcionamento, indicador_resstricao_acesso, tipo_telefone, ddi, ddd, numero_telefone, tipo_prestacao_servicos, nome_servicos_prestados, descricao_servicos_prestados))
            
    return arquivo