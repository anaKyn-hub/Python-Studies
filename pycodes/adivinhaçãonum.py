import os
from random import randint
#PODER JOGAR NOVAMENTE

def clear ():
  os.system('cls' if os.name == 'nt' else 'clear')

clear()
print ("Olá jogador, você consegue advinhar meu número?")

while True:
  try:
    num = int(input("Por favor insira um número: "))
    break
  except:
    clear() #limpa o terminal
    print("Valor invalido!")

if num == randint(0,5):
  print("Sucesso!")
else:
  print("Falhou :(")