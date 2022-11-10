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
  imposto = preco_produto * 0.05
  return imposto

#uso da função, calcular e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(imposto)
  