#criação de funções

preco = 1999.90

#calcular apenas 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

preco2= 100
imposto2 = preco2 * 0.05
print(imposto2)

#criar uma função calcular_imposto() que calcula um imposto de 5% e retorna a quem pediu...
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

#uso da função, calcular e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(f"Esse aqui é com a função (7%): {imposto}")

print(preco)
 #mudar só o valor na função por ex de 5% por 7%, em vez de mudar no codigo todo, muda só na função

valores = [1.99, 24.50, 78.27, 1515.5]
for valor in valores:
  print(f"o imposto de {valor} é {calcular_imposto(valor)}")


#Declarar um função calcular_imposto_aliquota que recebe dois parâmentro: o rpeço do produto e a alíquota de imposto a ser aplicada e retorna o imposto calcilado. Se a aliquota não for informada, utilize 7% como padrão.
def calcular_imposto_aliquota(valor, aliquota=7):
  imposto = valor * aliquota / 100
  return imposto

for valor in valores:
  print(f"o imposto de {valor} é {calcular_imposto_aliquota(valor)}")

for valor in valores:
  print(f"o imposto de {valor} é {calcular_imposto_aliquota(valor, 7)}")

for valor in valores:
  print(f"o imposto de {valor} é {calcular_imposto_aliquota(valor, 10)}")