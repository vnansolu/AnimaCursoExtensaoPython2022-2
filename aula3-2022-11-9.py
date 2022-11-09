print("ola")

contador = 1

#exibir de 1 ate 10 repetidamente
while (contador <= 10):
  print(contador)
  contador = contador+1 #contador += 1



frutas = ["morango", "pêssego", "limão"]
print(frutas)

#quero exibir apenas a 3a. fruta (limão)
print(frutas[2])

#exibir quantidade de objetos na lista
print(len(frutas)) #length = tamanho

#adicionar objetos na lista
frutas.append("laranja")
print(frutas)
print(len(frutas)) #length = tamanho

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

print("Exemplo das frutas com while..")
frutas.append("uva")

i=0
while(i<len(frutas)):   #while(i<4):
  print(frutas[i])
  i = i + 1
  