import random
print("*********************************")
print("Bem vindo ao jogo de adivinhaçao!")
print("*********************************")
# Gera número pseudo-aleatorio
numero_secreto = int(random.randrange(1,101))
# O jogo inicia com 1000 pontos
pontos = 1000
# print(numero_secreto)
# Inicializa variavel tentativas
tentativas = 0
# Usuario escolhe nivel
print("(1) Facil (2) Medio (3) Dificil")
nivel = int(input("Defina o nivel:"))

# Define nivel
# O nivel muda a quantidade de tentativas disponiveis
if nivel == 1:
    tentativas = 10;
elif nivel == 2:
    tentativas = 5;
elif nivel == 3:
    tentativas = 3;
else:
    print("Opção invalida.")

# Loop da quantidade de tentativas
for rodada in range(1, tentativas + 1):
    print("tentativa {} de {}".format(rodada, tentativas))
    # Usuario chuta um numero
    chute = int(input("Digite um número entre 1-100: "))
    # Se o numero não estiver no intervalo 1-100, pula.
    if chute < 1 or chute > 100:
        print("Insira um numero de 1 a 100!!")
        continue
    # Compara com o numero gerado aleatoriamente
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    # Acertou
    if (acertou):
        print("Você acertou!")
        break
    # Errou
    elif (rodada <= tentativas - 1):
        # Desconta o valor correspondente a distância do numero chutado com o valor secreto
        pontos = pontos - abs(numero_secreto - chute)
        # Da dicas se o numero é menor ou maior.
        if (maior):
            print("Você errou! chute mais baixo.")
        elif (menor):
            print("Você errou! chute mais alto.")
# Finaliza jogo, mensagem com o numero e pontuação.
print(f"Fim de jogo. \nO número era {numero_secreto}\n Voce fez {pontos} pontos.")

