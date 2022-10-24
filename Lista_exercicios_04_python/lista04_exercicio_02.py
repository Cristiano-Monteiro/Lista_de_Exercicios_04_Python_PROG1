corrida_cirio = {}

for i in range(0, 6):
    print('---'*30)
    nome = str(input('Nome do corredor: '))
    tempos = []
    for j in range(0, 10):
        print('Tempo na {} volta'.format(j+1), end='')
        tempo = float(input(': '))
        tempos.append(tempo)
    corrida_cirio[nome] = tempos

medias_corredores = []
melhor_corredor = ''
melhor_volta = 0

for i in corrida_cirio.items():
    desempenho_corredor = []
    media = sum(i[1]) / len(i[1])
    desempenho_corredor.append(media)
    desempenho_corredor.append(i[0])
    volta = max(i[1])
    if(volta <= melhor_volta or melhor_volta == 0):
        melhor_volta = volta
        melhor_corredor = i[0]
    medias_corredores.append(desempenho_corredor)

print('-----------------RESULTADOS-----------------')
print('Melhor volta da prova:  corredor {} --> {}s'.format(melhor_corredor, melhor_volta))
print('----------CLASSIFICAÇÃO DA CORRIDA----------')
medias_corredores.sort()
for i in range(0, 6):
    print('- {}º Lugar: {} ---- média de tempos: {:.1f}s'.format(i+1, medias_corredores[i][1], medias_corredores[i][0]))
print('--------------------------------------------')
print('# CAMPEÃO: ', medias_corredores[0][1])