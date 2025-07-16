import os

def clear ():
  os.system('cls' if os.name == 'nt' else 'clear')

#TABUADA
clear()
while True:
  try:
    print("Digite um número inteiro para exibir sua tabuada")
    num = int(input("Insira um número inteiro de 1 a 10: "))
    i = 1

    while i <= 10:
      print(num," x ", i, " = ", num * i)
      i = i + 1
    break
    
  except:
    clear()
    print("Valor Inválido! Tente novamente\n")
