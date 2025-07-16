import os
import math

def clear ():
  os.system('cls' if os.name == 'nt' else 'clear')

#Consulta de números primos

#Primeira resolução
"""
num = int(input("Digite um número inteiro para saber quais são os primos até sua referência: "))

def n_primos (n):
  lista2 = []
  for i in range(2, n+1):
    cprimo = 0
    for j in range(1, i+1):
      if i % j == 0:
        cprimo += 1
    if cprimo == 2:
      lista2.append(i)

  return lista2

print("São", len(n_primos(num)), "números primos, sendo eles:", n_primos(num))
"""
#Resolução utilizando raiz quadrada
clear()
def n_primos(n):
    lista = []

    for i in range(2, n + 1): 
        primo = True  #Começa com i sendo primo
        for j in range(2, int(math.sqrt(i)) + 1):  #Verifica se tem divisor exato além de 1 e ele mesmo, dividindo entre 2 e o arredondamento da raiz quadrada de i
            if i % j == 0:
                primo = False
                break  #Se achar um divisor, ele sai do laço, pois fez uma divisão exata
        if primo:
            lista.append(i)  #Se não achou divisor é primo, então adiciona o número na lista

    return lista

while True:
    try:
      num = int(input("Digite um número inteiro para saber quais são os números primos até sua referência: "))

      if num < 2:
        raise ValueError("o número deve ser maior que um.")
    
      break
    except ValueError as e:
      clear()
      if str(e).startswith("invalid literal for int"):
        print("Erro: você precisa digitar um número inteiro (sem letras ou símbolos).")
      else:
        print(f"Erro: {e}")
        
print("São", len(n_primos(num)), f"números primos até {num}, sendo eles:", n_primos(num))