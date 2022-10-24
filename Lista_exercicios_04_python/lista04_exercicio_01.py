agenda_de_telefones = {}

def incluirNovoNome(nome, telefone):
    if(type(telefone) != list):
        telefone = [telefone]
    agenda_de_telefones[nome] = telefone

def incluirTelefone(nome, telefone):
    if(nome in agenda_de_telefones):
        agenda_de_telefones[nome].append(telefone)
    else:
        while(True):
            resposta = int(input('Nome não existe na agenda. Deseja incluí-lo? SIM[1] - NÃO[2]  '))
            if(resposta == 1 or resposta == 2):
                break
        if(resposta == 1):
            incluirNovoNome(nome, telefone)

def excluirTelefone(nome, telefone):
    if(len(agenda_de_telefones[nome]) == 1):
        agenda_de_telefones.pop(nome)
    else:
        agenda_de_telefones[nome].remove(telefone)

def excluirNome(nome):
    agenda_de_telefones.pop(nome)
    print('---'*30)
    print('O nome "{}" foi excluído da agenda.'.format(nome))
    print('---'*30)

def consultarTelefone(nome):
    print('---'*30)
    print('Nome:', nome)
    print('Telefones: ', end='')
    for numero in agenda_de_telefones[nome]:
        print(numero,'; ', end='')
    print()
    print('---'*30)

# ------------ TESTANDO AS FUNÇÕES ------------ 
# OBS: REMOVER AS ASPAS TRIPLAS(""") PARA VER O FUNCIONAMENTO DO PROGRAMA

# ADICIONANDO NOVAS PESSOAS E NOVOS TELEFONES
incluirNovoNome('Carlos', [12345691, 38827156, 90812037])
incluirNovoNome('João', 38692454)
incluirNovoNome('Marcelo', [48933458, 11223373, 12849016, 55566721])
incluirNovoNome('Ana', [58531134, 48172956])

print(agenda_de_telefones)

# INCLUINDO UM NOVO TELEFONE DE UM CONTATO EXISTENTE
""" incluirTelefone('João', 55554444)

print(agenda_de_telefones) """

# INCLUINDO UM NOVO TELEFONE DE UM CONTATO NÃO EXISTENTE
""" incluirTelefone('Luiza', 11119999)

print(agenda_de_telefones) """

# EXCLUINDO O TELEFONE DE UMA PESSOA COM MAIS DE 1 TELEFONE
""" excluirTelefone('Ana', 58531134)

print(agenda_de_telefones) """

# EXCLUINDO O TELEFONE DE UMA PESSOA COM APENAS 1 TELEFONE
""" excluirTelefone('João', 38692454)

print(agenda_de_telefones) """

# EXCLUINDO UMA PESSOA DA AGENDA
""" excluirNome('Carlos')
excluirNome('Marcelo')

print(agenda_de_telefones) """

# CONSULTANDO O(S) TELEFONE(S) DE UMA PESSOA NA AGENDA
""" consultarTelefone('Marcelo') """