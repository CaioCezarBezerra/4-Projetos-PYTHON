#Projeto 2  - chute o numero

import random


class ChuteoNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minino = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Inciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.tentar_novamente == True:
            if int(self.valor_do_chute) > self.valor_aleatorio:
                print('Chute um Valor Mais Baixo')
                self.PedirValorAleatorio()
            elif int(self.valor_do_chute) < self.valor_aleatorio:
                print('Chute um valor mais alto!')
                self.PedirValorAleatorio()
            if int(self.valor_do_chute) == self.valor_aleatorio:    
                self.tentar_novamente = False
                print('PARABENS VOCE ACERTOU')    


    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um Numero: ')            

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minino,self.valor_maximo)

chute = ChuteoNumero()
chute.Inciar()
