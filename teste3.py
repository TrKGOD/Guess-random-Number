# Jogo de adivinhação de número em Python
# Criador: Tarek Ayache
# Python 3.10

# Bibliotecas importadas

import time
import random
from pyfiglet import Figlet

# Menu do programa

f = Figlet(font='slant')
print(f.renderText('Adivinhador-Python'))

# Funções e valores iniciais

numerosecreto = random.randint(0,20)
points = 1000
perdeuruim = 0
space = ("---------------------------------------------------------------------------")

# Explicação do programa

time.sleep(1)
print("Aqui você terá que adivinhar um número de 0 a 20.")
time.sleep(1)
print("Não se preucupe, a cada erro você receberá uma dica!")
time.sleep(1)
print("Além disso temos um sistema de score e seleção de dificuldade!")
time.sleep(1)
print("Boa sorte e divirta-se!")
time.sleep(1)
print(space)
u = input("Digite algo pra continuar: ")
print(space)

# Seleção de dificuldade do programa

print("Selecione uma das dificuldades a seguir:")
print("1-Fácil")
time.sleep(1)
print("2-Mediano")
time.sleep(1)
print("3-Difícil")
time.sleep(1)
print(space)

# Parte do código que define o número de tentativas e o desconto de pontos ao acontecer um erro.

z = int(input())
if z == 1:
        tent = 10
        desconto = 100
        print("Muito bem, a dificuldade fácil foi selecionada, você terá 10 tentativas.")
elif z == 2:
        tent = 5
        desconto = 200
        print("Muito bem, a dificuldade mediano foi selecionada, você terá 5 tentativas.")
else:
        tent = 3
        desconto = 333
        print("Oloco, a dificuldade difícil foi selecionada, você terá apenas 3 tentativas.")
print(space)

# Parte do código que detecta os erros e acertos do chute feito pelo jogador, juntamente a mensagens com dicas.

print("Agora é hora da seleção do número, tente dar um palpite")
time.sleep(1)
for chute in range(0, tent):
    x = int(input())
    tent -= 1
    if x == numerosecreto:
        print("Parabéns, você acertou o número secreto que era:", numerosecreto)
        print("Sua pontuação final foi de:", points)
    elif x != numerosecreto:
        print("Você errou o número, você possui a seguinte quantidade de tentativas restantes:", tent)
        points -= desconto
        print("Sua nova pontuação é:", points)
        if x > numerosecreto:
            print("DICA: O número secreto é menor do que", x)
            print(space)
        elif x < numerosecreto:
            print("DICA: o número secreto é maior do que", x)
            print(space)
            if tent == 0:
                print("Fim de jogo, você perdeu")
                print("Você pode melhorar! Sua pontuação final foi de:", perdeuruim)
                input("Digite qualquer coisa para finalizar o programa.")
                time.sleep(1)
