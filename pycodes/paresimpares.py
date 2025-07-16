import os

def clear ():
  os.system('cls' if os.name == 'nt' else 'clear')

#Consulta de números pares e impares
def n_pares (n, tipo):
  lista = []
  for i in range(n+1):
    if i % 2 == tipo:
      lista.append(i)
  return lista

clear()
while True:
  try:
    nome = ""
    ref = int(input("Você quer consultar os pares ou impares? 0.Par 1.Impar: "))

    if ref != 0 and ref != 1:
      raise ValueError("o número deve ser zero ou um.")

    if ref == 1:
      nome = "impares"
    elif ref == 0:
      nome = "pares"

    num = int(input(f"Digite um número para saber quais são os {nome} de 0 até sua referência: "))

    if num <= 0:
      raise ValueError("o número deve ser maior que zero.")
    
    break
  
  except ValueError as e:
    clear()
    if str(e).startswith("invalid literal for int"):
        print("Erro: você precisa digitar um número inteiro (sem letras ou símbolos).")
    else:
        print(f"Erro: {e}")
  
if len(n_pares(num, ref)) < 300:
  print(f"\nOs números {nome} entre 0 e {num} são:", n_pares(num, ref))
else:
  print("\nDesculpe, não foi possível mostrar a lista devido a grande quantidade de números.")

print("São",len(n_pares(num, ref)), f"{nome}", "no total")