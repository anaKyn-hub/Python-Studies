import os

def clear ():
  os.system('cls' if os.name == 'nt' else 'clear')

clear()
#Funções Recursivas--------

#Fatorial
def fatorial(n):
 if n == 1:
   return 1
 else:
   return n*fatorial(n-1)
 
num = int(input("Digite um número inteiro para saber seu fatorial: "))
 
print(f"O fatorial de {num} é", fatorial(num))

#Sequência de Fibonacci
def fibonacci(n):
  if n == 0 or n ==1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)
  
n = int(input("\nDigite o número inteiro correspondente ao índice da série de Fibonacci para saber que número ocupa essa posição: "))

print(f"O número de Fibonacci no indice {n} é", fibonacci(n))