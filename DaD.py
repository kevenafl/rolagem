import random

def rolar_dados(numero_de_dados, numero_de_lados):
    resultados = [random.randint(1, numero_de_lados) for _ in range(numero_de_dados)]
    return resultados


while True:
  entrada_usuario = input("Digyte o dado que sera rolado (ex: 2d20): ")
  dados, lados = [int(valor) for valor in entrada_usuario.lower().split('d')]
  resultados= rolar_dados(dados, lados)
  print(f"Resultado da rolagem: ({entrada_usuario}): {resultados}")
  resposta = str(input("Qier fazer uma nova rolagem? ")).lower()
  if resposta == 'n':
    break
