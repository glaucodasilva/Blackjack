class sal:
    def __init__(self, saldo = 1000):
        self.saldo = saldo

    def val(self):
        return self.saldo

import random

def inicio():
    saldo = sal()
    print('                                           Bem Vindo ao Blackjack!                                           ')
    print('')
    print('Para iniciar a partida digite o valor de sua aposta entre 1 e 25, são permitidos apenas números inteiteiros!')
    print('')
    print('O seu saldo atual é: ', saldo.val())

def criarbaralho():
    baralho = list(range(1, 14))*30
    random.shuffle(baralho)
    return baralho

def controlasaldo():
    pass
def jogadores():
    pass
def creditoinicial():
    pass
def vencedor():
    pass
def distribuircartas():
    pass
def imprimecartas():

    carta2 = ['############', '#          #', '#  ######  #', '#       #  #', '#       #  #', '#  ######  #', '#  #       #', '#  #       #', '#  ######  #', '#          #', '############']
    carta3 = ['############', '#          #', '#  ######  #', '#       #  #', '#       #  #', '#  ######  #', '#       #  #', '#       #  #', '#  ######  #', '#          #', '############']
    carta4 = ['############', '#          #', '#  #    #  #', '#  #    #  #', '#  #    #  #', '#  ######  #', '#       #  #', '#       #  #', '#       #  #', '#          #', '############']
    carta5 = ['############', '#          #', '#  ######  #', '#  #       #', '#  #       #', '#  ######  #', '#       #  #', '#       #  #', '#  ######  #', '#          #', '############']
    carta6 = ['############', '#          #', '#  ######  #', '#  #       #', '#  #       #', '#  ######  #', '#  #    #  #', '#  #    #  #', '#  ######  #', '#          #', '############']
    carta7 = ['############', '#          #', '#  ######  #', '#       #  #', '#       #  #', '#       #  #', '#       #  #', '#       #  #', '#       #  #', '#          #', '############']
    carta8 = ['############', '#          #', '#  ######  #', '#  #    #  #', '#  #    #  #', '#  ######  #', '#  #    #  #', '#  #    #  #', '#  ######  #', '#          #', '############']
    carta9 = ['############', '#          #', '#  ######  #', '#  #    #  #', '#  #    #  #', '#  ######  #', '#       #  #', '#       #  #', '#       #  #', '#          #', '############']
    carta10 = ['############', '#          #', '# # ###### #', '# # #    # #', '# # #    # #', '# # #    # #', '# # #    # #', '# # #    # #', '# # ###### #', '#          #', '############']
    cartaJ = ['############', '#          #', '#       #  #', '#       #  #', '#       #  #', '#       #  #', '#  #    #  #', '#  #    #  #', '#  ######  #', '#          #', '############']
    cartaQ = ['############', '#          #', '#  ######  #', '#  #    #  #', '#  #    #  #', '#  #    #  #', '#  #  # #  #', '#  #   ##  #', '#  ######  #', '#        # #', '############']
    cartaK = ['############', '#          #', '#  #    #  #', '#  #   #   #', '#  # #     #', '#  #####   #', '#  #    #  #', '#  #    #  #', '#  #    #  #', '#          #', '############']
    cartaA = ['############', '#          #', '#  ######  #', '#  #    #  #', '#  #    #  #', '#  ######  #', '#  #    #  #', '#  #    #  #', '#  #    #  #', '#          #', '############']

    cartas = [carta2, carta3, carta4, carta5, carta6, carta7, carta8, carta9, carta10, cartaJ, cartaQ, cartaK, cartaA]
    qtcartas = 13

    for i in range(11):
        linha = ''
        for j in range(qtcartas):
                linha += cartas[j][i] + '    '
        print(linha)

inicio()
criarbaralho()










