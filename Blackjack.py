############################################################ DECLARAÇÃO DE CLASSES! ############################################################
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
import sys

######################################################## DECLARAÇÃO DE VARIAVEIS GLOBAIS! ########################################################
saldo = sal()
baralho = []
cartasjog = []
cartasdealer = []
inijog = 0
qtdcartasdealer = 0
qtdcartajog = 1
somacartdealer = 0
somacartdealerA = 0
somacartjog = 0
somacartjogA = 0
fimjogada = False

############################################################# DECLARAÇÃO DE FUNÇÕES!! #############################################################
def cls(): print("\n" * 100)

###################################################################################################################################################

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
        criarbaralho()
        distribuircartas(True, True)
    elif aposta > 100 or aposta < 1:
        novaaposta()
    elif aposta > saldo.val():
        print('O valor da sua aposta não pode ultrapassar o seu saldo!')
    else:
        saldo.menos(aposta)
        criarbaralho()
        distribuircartas(True, True)

###################################################################################################################################################

def criarbaralho():
    global  baralho
    baralho = list(range(1, 14))*30
    random.shuffle(baralho)

###################################################################################################################################################

def distribuircartas(dealer, jog):
    global baralho, qtdcartasdealer, qtdcartajog, somacartdealer, somacartdealerA, somacartjog, somacartjogA, inijog
    cls()
    print('Cartas do Dealer')
    print('')
    if dealer:
        qtdcartasdealer += 1
        cartasdealer.append(random.choice(baralho))
    imprimecartas(cartasdealer, qtdcartasdealer)
    somacartdealer, somacartdealerA = somacartas(qtdcartasdealer, cartasdealer, False)
    print('')
    print('')
    print('')
    print('Cartas do Jogador')
    print('')
    if jog:
        qtdcartajog += 1
        for i in range(inijog, qtdcartajog):
            inijog += 1
            cartasjog.append(random.choice(baralho))
    imprimecartas(cartasjog, qtdcartajog)
    somacartjog, somacartjogA = somacartas(qtdcartajog, cartasjog, True)
    resultado(dealer, jog)

###################################################################################################################################################

def jogarnovamente():
    while True:
        print('')
        print('Deseja jogar novamente? Digite S para sim e N para não.')
        continua = input()
        if continua.upper() not in ('S', 'N'):
            continue
        elif continua == 'S':
            cls()
            novaaposta()
        else:
            fimdejogo()

###################################################################################################################################################

def resultado(dealer, jog):
    global somacartjog, somacartjogA, fimjogada, qtdcartajog, qtdcartajog, qtdcartasdealer, cartasdealer
    if qtdcartajog == 2 and 1 in cartasjog and (10 in cartasjog or 11 in cartasjog or 12 in cartasjog or 13 in cartasjog):
        if 1 not in cartasdealer and 10 not in cartasdealer and 11 not in cartasdealer and 12 not in cartasdealer and 13 not in cartasdealer:
            print('Blackjack! O jogador Ganhou!')
            jogarnovamente()
        elif qtdcartasdealer == 2 and 1 in cartasdealer and (10 in cartasdealer or 11 in cartasdealer or 12 in cartasdealer or 13 in cartasdealer):
            print('Isso é um empate!')
            jogarnovamente()
        elif qtdcartasdealer == 1:
            fimjogada = True
            distribuircartas(True, False)
        else:
            print('Blackjack! O Jogador Ganhou!')
            jogarnovamente()

    elif somacartjog > 21 and somacartjogA > 21:
        print('')
        print('O Jogador Estourou! O Dealer Ganhou!')
        jogarnovamente()
    elif dealer and fimjogada:
        if qtdcartasdealer == 2 and 1 in cartasdealer and (10 in cartasdealer or 11 in cartasdealer or 12 in cartasdealer or 13 in cartasdealer):
            print('Blackjack! O Dealer Ganhou!')
            jogarnovamente()
        elif somacartdealer < 17 and somacartdealerA < 17:
            distribuircartas(True, False)
        elif 17 <= (somacartdealer and somacartdealer) <= 21 and somacartdealer > (somacartjog and somacartjogA):
            print('')
            print('O Dealer Ganhou')
            jogarnovamente()
        elif somacartdealer > 21 and somacartdealerA > 21:
            print('')
            print('O Dealer Estourou! O Jogador Ganhou!')
            jogarnovamente()
    else:
        continuadobrafica()

###################################################################################################################################################

def continuadobrafica():
    global qtdcartajog, fimjogada
    print('')
    print('')
    if qtdcartajog == 2:
        while True:
            print('Para Pedir mais cartas digite P, para Dobrar digite D, para Ficar digite F!')
            escolha = input().upper()
            if escolha == 'P' or escolha == 'D' or escolha == 'F':
                break
    else:
        while True:
            print('Para Pedir mais cartas digite P, para Ficar digite F!')
            escolha = input()
            if escolha == 'P' or escolha == 'F':
                break

    if escolha == 'P':
        distribuircartas(False, True)
    elif escolha == 'F':
        fimjogada = True
        distribuircartas(True, False)

###################################################################################################################################################

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

###################################################################################################################################################

def somacartas(qtdcartas, cartas, jog):

    somacart = 0
    somacartA = 0
    if 1 in cartas:
        az = True
    else:
        az = False
    for i in range(qtdcartas):
        if 1 < cartas[i] <= 10:
            somacart += cartas[i]
            somacartA += cartas[i]
        elif cartas[i] > 10:
            somacart += 10
            somacartA += 10
        else:
            somacart += 11
            somacartA += 1
            az = True
    print('')
    print('')
    if jog:
        if az:
            print('Aposta atual: ', saldo.aposta, '          Total pontos:', somacart, '/', somacartA)
        else:
            print('Aposta atual: ', saldo.aposta, '          Total pontos:', somacart)
    else:
        if az:
            print('Total pontos:', somacart, '/', somacartA)
        else:
            print('Total pontos:', somacart)
    return (somacart, somacartA)

###################################################################################################################################################

def fimdejogo():
    sys.exit()


################################################################ INÍCIO DO SISTEMA! ################################################################
print('                              Bem Vindo ao Blackjack do Glauco ;D!                              ')
novaaposta()










