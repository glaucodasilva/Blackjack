def inicio():
    pass
def jogadores():
    pass
def vencedor():
    pass
def distribuircartas():
    pass
def imprimecartas():

    carta2 = ['############', '#          #', '#  ######  #', '#       #  #', '#       #  #', '#  ######  #', '#  #       #', '#  #       #', '#  ######  #', '#          #', '############']
    carta3 = ['############', '#          #', '#  ######  #', '#       #  #', '#       #  #', '#  ######  #', '#       #  #', '#       #  #', '#  ######  #', '#          #', '############']
    cartas = [carta2, carta3]
    qtcartas = 2

    for i in range(11):
        linha = ''
        for j in range(qtcartas):
                linha += cartas[j][i] + '    '
        print(linha)


imprimecartas()










