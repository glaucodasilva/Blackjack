#DECLARAÇÃO DE CLASSES!
class sal:
    def __init__(self, saldo = 1000, aposta = 0):
        self.saldo = saldo
        self.aposta = aposta

    def val(self):
        return self.saldo

    def menos(self, aposta):
        self.aposta = aposta
        self.saldo -= aposta
        return self.saldo

    def aposta(self):
        return self.aposta

import random

#DECLARAÇÃO DE VARIAVEIS GLOBAIS!
saldo = sal()


#DECLARAÇÃO DE FUNÇÕES!!
def cls(): print("\n" * 100)

def novaaposta():
    aposta = 0
    entrada = ''
    print('')
    print('O seu saldo atual é: ', saldo.val())
    print("")
    print('Para iniciar a partida digite o valor de sua aposta entre 1 e 500, são permitidos apenas números inteiros!')
    try:
        entrada = input()
        aposta = int(round(float(entrada)))
    except:
        novaaposta()

    if float(entrada) // 1 != float(entrada):
        print('O valor digitado para sua aposta não é um valor inteiro, o mesmo será arredondado para %d' %aposta)
        saldo.menos(aposta)
        distribuircartas(criarbaralho())
    elif aposta > 100 or aposta < 1:
        novaaposta()
    elif aposta > saldo.val():
        print('O valor da sua aposta não pode ultrapassar o seu saldo!')
    else:
        saldo.menos(aposta)
        distribuircartas(criarbaralho())


def criarbaralho():
    baralho = list(range(1, 14))*30
    random.shuffle(baralho)
    return baralho

def distribuircartas(baralho):
    cls()
    print('Cartas do Dealer')
    print('')
    qtdcartasdealer = 1
    cartasdealer = []
    for i in range(qtdcartasdealer):
        cartasdealer.append(random.choice(baralho))
    imprimecartas(cartasdealer, qtdcartasdealer)
    print('')
    print('')
    print('')
    print('Cartas do Jogador')
    print('')
    qtdcartajog = 2
    cartasjog = []
    for i in range(qtdcartajog):
        cartasjog.append(random.choice(baralho))
    imprimecartas(cartasjog, qtdcartajog)
    print('')
    print('')
    print('Aposta atual: ', saldo.aposta)

def imprimecartas(sortcartas, qtcartas):
    cartas = []
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

    baralho = ['erro', cartaA, carta2, carta3, carta4, carta5, carta6, carta7, carta8, carta9, carta10, cartaJ, cartaQ, cartaK]

    for i in sortcartas:
            cartas.append(baralho[i])

    for i in range(11):
        linha = ''
        for j in range(qtcartas):
                linha += cartas[j][i] + '    '
        print(linha)


#INÍCIO DO SISTEMA!
print('                              Bem Vindo ao Blackjack do Glauco ;D!                              ')
novaaposta()










