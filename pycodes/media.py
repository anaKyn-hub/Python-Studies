def calcMedia(nota1,nota2):
  media = (nota1 + nota2)/2
  return media

#Cálculo de Média Simples
while True:
  try:
    n1 = int(input("Digite a nota 1: "))
    n2 = int(input("Digite a nota 2: "))
    mediaFinal = calcMedia(n1,n2)
    break
  except:
    print("\nValor inválido, tente novamente.\n")

if (mediaFinal >= 6):
  print(f"O aluno foi aprovado com média de {mediaFinal}!")
elif (mediaFinal >=3 and mediaFinal < 6): 
  print("O aluno precisará fazer o exame de recuperação!")
elif (mediaFinal < 3):
  print("O aluno foi reprovado!")