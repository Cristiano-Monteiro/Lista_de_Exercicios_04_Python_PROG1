def simulador_de_consumo(bandeira, icms, dados_equipamento):
    consumo_estimado_total = 0
    for equip in dados_equipamento.items():
        consumo_estimado_por_equip_em_KWH = (equip[1] * potencia_dos_equipamentos[equip[0]])/1000
        consumo_estimado_total += consumo_estimado_por_equip_em_KWH
    calculo_bandeira = custo_da_bandeira[bandeira] * consumo_estimado_total
    valor_final_estimado = (calculo_bandeira * icms) + calculo_bandeira
    return valor_final_estimado

potencia_dos_equipamentos = {
    'ar-condicionado': 1600,
    'computador': 350,
    'chuveiro': 5000,
    'ferro': 1000,
    'lampada': 32,
    'lavadora-roupas': 600,
    'refrigerador': 350,
    'tv': 200
}

custo_da_bandeira = {
    'verde' : 0.50,
    'amarela' : 0.53,
    'vermelha' : 0.56
}

# Dados usados do exemplo no pdf:
bandeira = 'verde'
icms = 0.25
quantidade = 3
dados_equipamentos = {'chuveiro': 1, 'ferro': 0.2, 'tv': 4}

print('Valor estimado da conta de energia: R$ {:.2f}'.format(simulador_de_consumo(bandeira, icms, dados_equipamentos)))

# Dados enviados por um usuário:
print('---'*30)
bandeira = str(input('Bandeira utilizada no mês (verde, amarela ou vermelha): '))
icms = float(input('Valor do ICMS cobrado: '))
quantidade = int(input('Quantidade de equipamentos: '))
dados_equipamentos = {}
for cont in range(quantidade):
    nome_equipamento = str(input('Nome do equipamento: '))
    dados_equipamentos[nome_equipamento] = float(input('Tempo de uso médio diário (em horas): '))
print('---'*30)
print('Valor estimado da conta de energia: R$ {:.2f}'.format(simulador_de_consumo(bandeira, icms, dados_equipamentos)))
