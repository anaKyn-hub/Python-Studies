import os
from random import randint

randnum = randint(1,5)
exit = 0
tentativas = 0

def clear ():
  os.system('cls' if os.name == 'nt' else 'clear')

clear()
print ("Olá jogador, você consegue advinhar meu número?")
print ("Para sair do jogo, digite 0")

while True:
  try:
    num = int(input("Por favor insira um número de 1 a 5: "))
    tentativas += 1

    while num != randnum and num != exit:
      clear()
      print("Errou :(")
      print("Se quiser sair digite 0, ou continue tentando :)")
      num = int(input("Tente novamente um número de 1 a 5: "))
      tentativas += 1
    
    if num == randnum:
      print("\nSucesso! Você acertou o número!")
      print(f"Você acertou em {tentativas} tentativa!" if tentativas == 1 else f"Você acertou em {tentativas} tentativas!")
      break

    if num == exit:
      print("\nObrigada por jogar!")
      break

  except:
    clear() #limpa o terminal
    print("Valor invalido!")