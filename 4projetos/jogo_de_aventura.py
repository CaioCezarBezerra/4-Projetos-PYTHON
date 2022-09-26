
class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul? (n/s) '
        self.pergunta2 = 'Você prefere a espada ou escudo? (espadao/escudo)'
        self.pergunta3 = 'Qual é a sua especialidade? (linha de frente/tation)'
        self.finaldahistaoria1 = 'Você será um heroi na linha de frente1'
        self.finaldahistaoria2 = 'Você sera um heroi protegendo a nossa tropas!'
        self.finaldahistaoria3 = 'Você ira se sacrificar na batalha!'
        self.finaldahistaoria4 = 'Você nao e capaz de lutar nessa batalha'
    def Inciar(self):
        resposta1 = input(self.pergunta1)
        if resposta1 == 'n':
            resposta2 = input(self.pergunta2)
            if resposta2 == 'espada':
                print(self.finaldahistaoria1)
            if resposta2 == 'escudo':
                print(self.finaldahistaoria2)
        if resposta1 == 's':
            resposta2 = input(self.pergunta3)
            if resposta2 == 'linha de frente':
                print(self.finaldahistaoria3)
            if resposta2 == 'tatico':
                print(self.finaldahistaoria4)                


jogo = JogoDeAventura()
jogo.Inciar()