def aprovados(D):
    # Um aluno é aprovado quando todas as suas notas são maiores que 7
    print('----------------ALUNOS APROVADOS----------------')
    for aluno in D.items():
        if(aluno[1][0] > 7 and aluno[1][1] > 7 and aluno[1][2] > 7):
            print('Aluno: {} --- Notas: {}'.format(aluno[0], aluno[1]))
    print('------------------------------------------------')

D = {
    'Darth Vader': (7.5,8.0,6.5),
    'Han Solo': (9.0,8.5,9.5),
    'Chewbacca':(3.5,1.0,6.5)
}

aprovados(D)