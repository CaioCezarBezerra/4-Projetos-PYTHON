import random

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza voce deve fazer isso!',
            'Nao sei. Voce que sabe',
            'Nao faz isso Nao',
            'acho que ta na hora certa!'
        ]

    def Iniciar(self):
        input('Faça Sua Pergunta: ')
        print(random.choice(self.respostas))
decida = DecidaPorMim()
decida.Iniciar()          

