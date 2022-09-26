#Simulador de Dado
#simular o uso de um dado, derando um numero de 1 a 6

from logging import exception
import random
from traceback import print_tb

class SimuladoDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Voce gostaria de gerar um novo valor para o dado: '

    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim' or resposta == 's':
            self.GerarValorDoDado()
        elif resposta == 'nao' or resposta == 'n':
            print('Agradecemos a sua participacao')
        else:
            print('Favor digitar sim ou nao')       

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))


simulador = SimuladoDeDado()
simulador.Iniciar()                   
