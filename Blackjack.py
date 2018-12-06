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
somacartdeeler = 0
somacartdeelerA = 0
somacartjog = 0
somacartjogA = 0

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
    global baralho, qtdcartasdealer, qtdcartajog, somacartdeeler, somacartdeelerA, somacartjog, somacartjogA
    cls()
    print('Cartas do Dealer')
    print('')
    if dealer:
        qtdcartasdealer += 1
        for i in range(qtdcartasdealer):
            cartasdealer.append(random.choice(baralho))
    imprimecartas(cartasdealer, qtdcartasdealer)
    somacartdeeler, somacartdeelerA = somacartas(qtdcartasdealer, cartasdealer, False)
    print('')
    print('')
    print('')
    print('Cartas do Jogador')
    print('')
    if jog:
        qtdcartajog += 1
        for i in range(inijog, qtdcartajog):
            cartasjog.append(random.choice(baralho))
    imprimecartas(cartasjog, qtdcartajog)
    somacartjog, somacartjogA = somacartas(qtdcartajog, cartasjog, True)
    resultado()

###################################################################################################################################################

def resultado():
    if somacartjog > 21 and somacartjogA > 21:
        print('')
        print('O deealer ganhou')
        print('')
        while True:
            print('Deseja jogar novamente? Digite S para sim e N para não.')
            continua = input()
            if continua.upper() not in ('S','N'):
                continue
            elif continua == 'S':
                cls()
                novaaposta()
            else:
                fimdejogo()
    else:
        continuadobrafica()

###################################################################################################################################################

def continuadobrafica():
    global inijog, qtdcartasdealer, qtdcartajog
    print('')
    print('')
    print('Para Pedir mais cartas digite P, para Dobrar digite D, para Ficar digite F!')
    escolha = input()
    if escolha.upper() == 'P':
        inijog = 2
        distribuircartas(False, True)

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
    if qtdcartas == 2 and 1 in cartas and (10 in cartas or 11 in cartas or 12 in cartas or 13 in cartas):
        print('Blackjack')
        return
    else:
        somacart = 0
        somacartA = 0
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
    return somacart, somacartA

###################################################################################################################################################

def fimdejogo():
    sys.exit()


################################################################ INÍCIO DO SISTEMA! ################################################################
print('                              Bem Vindo ao Blackjack do Glauco ;D!                              ')
novaaposta()










