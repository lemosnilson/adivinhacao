import random

print("*********************************")
print("Bem-vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
pontos = int(1000)
pontos_perdidos = int(0)

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))
if nivel == 1:
    tentativas = 10
elif nivel == 2:
    tentativas = 7
else:
    tentativas = 5

for rodada in range(1, tentativas+1):
    print("Tentativa {} de {}". format(rodada, tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("você digitou o número", chute_str)

    chute = int(chute_str)

    if not 1 <= chute <= 100:
        print("O número deve estar entre 1 e 100")

    acertou = numero_secreto == chute
    menor = chute > numero_secreto
    maior = chute < numero_secreto

    if acertou:
        print("Você acertou!")
        print("Você fez {} pontos!".format(pontos))
        break
    else:
        if menor:
            print("Você errou. O número secreto é menor.")
        elif maior:
            print("Vcê errou. O número secreto é maior.")
        pontos_perdidos = numero_secreto - chute
        pontos = pontos - abs(pontos_perdidos)

print("Fim de Jogo")
