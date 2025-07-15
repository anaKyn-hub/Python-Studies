import os
from random import randint

exit = 0
tentativas = 0

def clear ():
  os.system('cls' if os.name == 'nt' else 'clear')

clear() #limpa o terminal
print("Bem vindo ao Jogo Adivinhe o Número!\n")

while True:
  try:
    print("Primeiro, escolha o intervalo de números para o jogo!")
    print("Digite o menor número, aperte a tecla 'enter' e em seguida o maior número do intervalo (Por exemplo 1 e depois 10 para um intervalo de 1 a 10)")

    num1 = int(input("Escolha o primeiro número inteiro: "))
    num2 = int(input("Escolha o segundo número inteiro: "))

    if num1 >= num2:
      raise ValueError("O primeiro número deve ser maior que o segundo número.")

    print ("\nOlá jogador, você consegue adivinhar o número?")
    print ("Para sair do jogo, digite 0")

    num = int(input(f"Por favor insira um número de {num1} a {num2}: "))
    tentativas += 1

    randnum = randint(num1,num2)

    while num != randnum and num != exit:
      clear()
      print("Errou :(")
      print("Se quiser sair digite 0, ou continue tentando :)")
      num = int(input(f"Tente novamente um número de {num1} a {num2}: "))
      tentativas += 1
    
    if num == randnum:
      clear()
      print("Sucesso! Você acertou o número!")
      print(f"Você acertou em {tentativas} tentativa!" if tentativas == 1 else f"Você acertou em {tentativas} tentativas!")
      print("\nObrigada por jogar!")
      break

    if num == exit:
      print("\nObrigada por jogar!")
      break

  except ValueError:
    clear()
    print("Valor invalido!\n")

  """
    *Mostra a mensagem de erro
    except ValueError as e:
    clear()
    print(f"Valor invalido! {e}\n")
  """