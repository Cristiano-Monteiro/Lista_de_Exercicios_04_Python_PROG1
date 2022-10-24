def calculo_pesagem(dados_lutadores):
    lutadores_aprovados = 0
    lutadores_reprovados = 0
    lutador_mais_leve = (0,0)
    for lutador in dados_lutadores.items():
        if(lutador[1] > peso_limite_inferior):
            peso_maximo_permitido = (peso_limite_superior * 0.08) + peso_limite_superior
            if(lutador[1] < peso_maximo_permitido):
                lutadores_aprovados += 1
                if(lutador[1] < lutador_mais_leve[1] or lutador_mais_leve == (0,0)):
                    lutador_mais_leve = lutador
    lutadores_reprovados = quantidade_lutadores - lutadores_aprovados
    if(lutadores_reprovados == quantidade_lutadores):
        lutador_mais_leve = ('vazio', 0)
    porcentagem_reprovados = (lutadores_reprovados * 100) / quantidade_lutadores
    print('---'*30)
    print('Quantidade de lutadores aprovados no dia da pesagem:', lutadores_aprovados)
    print('Porcentagem de lutadores reprovados no dia da pesagem:', porcentagem_reprovados)
    print('Nome do lutador mais leve (entre os aprovados):', lutador_mais_leve[0])
    print('---'*30)

# Dados fornecidos pelo "exemplo de entrada 1" no pdf:
peso_limite_inferior = 84
peso_limite_superior = 93
quantidade_lutadores = 4
dados_lutadores = {
    'Jon': 98,
    'Cornier': 86,
    'Jack': 112,
    'Spider': 89
}
calculo_pesagem(dados_lutadores)

# Dados fornecidos pelo "exemplo de entrada 2" no pdf:
peso_limite_inferior = 106
peso_limite_superior = 114
quantidade_lutadores = 5
dados_lutadores = {
    'Brucutu': 105,
    'Crapper': 124,
    'Hamer': 102,
    'Squizer': 129,
    'Gorilla': 99
}
calculo_pesagem(dados_lutadores)

# Dados fornecidos por um usuário:
peso_limite_inferior = int(input('Peso limite inferior da categoria: '))
peso_limite_superior = int(input('Peso limite superior da categoria: '))
quantidade_lutadores = int(input('Quantidade de lutadores: '))
dados_lutadores = {}
for cont in range(quantidade_lutadores):
    nome_lutador = str(input('- Nome do lutador: '))
    dados_lutadores[nome_lutador] = int(input('- Peso do lutador: '))
calculo_pesagem(dados_lutadores)