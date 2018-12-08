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

    def soma(self, ganhou):
        self.ganhou = ganhou
        self.saldo += ganhou
        return self.saldo

    def aposta(self):
        return self.aposta

    def dobra(self):
        self.saldo -= self.aposta
        self.aposta *= 2

import random
import sys
import time

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
resultjog = 0
dobra = False

############################################################# DECLARAÇÃO DE FUNÇÕES!! #############################################################
def cls(): print("\n" * 100)

###################################################################################################################################################

def novaaposta():
    global cartasjog, cartasdealer, inijog, qtdcartasdealer, qtdcartajog, fimjogada, dobra
    fimjogada = False
    dobra = False
    qtdcartasdealer = 0
    qtdcartajog = 1
    cartasjog = []
    cartasdealer = []
    inijog = 0
    aposta = 0
    entrada = ''
    print('')
    print('O seu saldo atual é: ', saldo.val())
    print("")
    print('Para iniciar a partida digite o valor de sua aposta entre 1 e 500, são permitidos apenas números inteiros!')
    try:
        entrada = 10#input()
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
    resultado()

###################################################################################################################################################

def jogarnovamente():
    while True:
        print('')
        print('Deseja jogar novamente? Digite S para sim e N para não.')
        continua = input().upper()
        if continua not in ('S', 'N'):
            continue
        elif continua == 'S':
            cls()
            novaaposta()
        else:
            fimdejogo()

###################################################################################################################################################

def continuadobrafica():
    global qtdcartajog, fimjogada, dobra
    print('')
    print('')
    if dobra:
        fimjogada = True
        distribuircartas(True, False)
    else:
        if qtdcartajog == 2:
            while True:
                print('Para Pedir mais cartas digite P, para Dobrar digite D, para Ficar digite F!')
                escolha = input().upper()
                if escolha == 'P' or escolha == 'D' or escolha == 'F':
                    break
        else:
            while True:
                print('Para Pedir mais cartas digite P, para Ficar digite F!')
                escolha = input().upper()
                if escolha == 'P' or escolha == 'F':
                    break
        if escolha == 'P':
            distribuircartas(False, True)
        elif escolha == 'F':
            fimjogada = True
            distribuircartas(True, False)
        elif escolha == 'D':
            saldo.dobra()
            dobra = True
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
    if az:
        if somacart > 21:
            print('Pontos:', somacartA)
        else:
            print('Pontos:', somacart, '/', somacartA)
    else:
        print('Pontos:', somacart)
    return (somacart, somacartA)

###################################################################################################################################################

def fimdejogo():
    sys.exit()

###################################################################################################################################################

def empate():
    print('')
    print('Isso é um Empate!')
    saldo.soma(saldo.aposta)
    print('Saldo:', saldo.val(), '                 Aposta:', saldo.aposta, 'Pago:', saldo.aposta)
    jogarnovamente()

def dealer(estouro, black):
    print('')
    if estouro:
        print('O Jogador Estourou!')
    elif black:
        print('Blackjack! O Dealer Ganhou!')
    else:
        print('O Dealer Ganhou!')
    print('Saldo:', saldo.val(), '                 Aposta:', saldo.aposta, 'Pago: 00')
    jogarnovamente()

def jogador(estourou, black):
    ganhou = 2 * saldo.aposta
    print('')
    if estourou:
        print('O Dealer Estourou!')
    elif black:
        ganhou = 3 * saldo.aposta
        print('Blackjack! O Jogador Ganhou!')
    else:
        print('O Jogador Ganhou!')
    saldo.soma(ganhou)
    print('Saldo:', saldo.val(), '                 Aposta:', saldo.aposta, 'Pago:', ganhou)
    jogarnovamente()


###################################################################################################################################################

def resultado():
    global somacartjog, somacartjogA, fimjogada, qtdcartajog, cartasjog, qtdcartasdealer, cartasdealer, resultjog
    if qtdcartajog == 2 and 1 in cartasjog and (10 in cartasjog or 11 in cartasjog or 12 in cartasjog or 13 in cartasjog):
        if qtdcartasdealer == 1 and (1 in cartasdealer or 10 in cartasdealer or 11 in cartasdealer or 12 in cartasdealer or 13 in cartasdealer):
            fimjogada = True
            distribuircartas(True, False)
        elif qtdcartasdealer == 2 and 1 in cartasdealer and (10 in cartasdealer or 11 in cartasdealer or 12 in cartasdealer or 13 in cartasdealer):
            empate()
        else:
            jogador(False, True)
    if fimjogada:
        if somacartdealer != somacartdealerA:
            if cartasdealer == 2 and 1 in cartasdealer and (10 in cartasdealer or 11 in cartasdealer or 12 in cartasdealer or 13 in cartasdealer):
                dealer(False, True)
            elif somacartdealer > 21:
                if 21 >= somacartdealerA >= 17:
                    if somacartdealerA > resultjog:
                        dealer(False, False)
                    elif somacartdealerA == resultjog:
                        empate()
                    else:
                        jogador(False, False)
                elif somacartdealerA < 17:
                    time.sleep(2)
                    distribuircartas(True, False)
                else:
                    jogador(True, False)
            elif somacartdealer >= 17:
                    if somacartdealer > resultjog:
                        dealer(False, False)
                    elif somacartdealer == resultjog:
                        empate()
                    else:
                        time.sleep(2)
                        distribuircartas(True, False)
            else:
                time.sleep(2)
                distribuircartas(True, False)
        elif 21 >= somacartdealer >= 17:
            if somacartdealer > resultjog:
                dealer(False, False)
            elif somacartdealer == resultjog:
                empate()
            else:
                jogador(False, False)
        elif somacartdealer < 17:
            time.sleep(2)
            distribuircartas(True, False)
        else:
            jogador(True, False)
    else:
        if somacartjog != somacartjogA:
            if somacartjog <= 21:
                resultjog = somacartjog
            else:
                resultjog = somacartjogA
        elif somacartjog > 21:
            dealer(True, False)
        else:
            resultjog = somacartjog
        if resultjog == 21:
            fimjogada = True
            distribuircartas(True, False)
        continuadobrafica()

################################################################ INÍCIO DO SISTEMA! ################################################################
print('                              Bem Vindo ao Blackjack do Glauco ;D!                              ')
novaaposta()
