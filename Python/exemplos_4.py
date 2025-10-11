#Manipulação de vetores

valores = [1, 2, 3, 4, 5, 6, 7, 8]
#          0, 1, 2, 3, 4, 5, 6, 7

print(valores)

##Sub-Listas
###lista[i:j]: pega de um ponto até o outro / o j é sempre j-1.
print(valores[1:4])

print(valores[3:]) # da posição 3 até o fim

print(valores[:3]) # do começo até a posição 3 (no caso, 3-1)

print(valores[1:7:2]) # da posição 1 até a posição 7, pulando de dois em dois.

#Unpacking:
##De forma bruta:
x = [5, 7, 8]
print(x)
n1 = x[0]
n2 = x[1]
n3 = x[2]
print("n1: ", n1)

##Forma comum:
[a, b, c] = x
print(a)
print(b)

#Concatenando:

a = [1, 2, 3]
b = [4, 5, 6]

lista = a + b
print(lista)

lista_A_tripla = a * 3
print(lista_A_tripla) # os valores da lista é repetida 3 vezes


del lista_A_tripla[2] # remove o elemento da posição 2
print(lista)

#Exemplo de referência (receber o mesmo endereço) de valores:

c = [1, 3, 5]

#d recebe os endereços de c, ou seja, as alterações de c afetam d.
d = c

print(d)

c.append(-5)
print(c)
print(d)

d = c[:] #d recebe os valores de c
c.append(10)
print(c)
print(d)

#Verificar se um item está no vetor:
a = [1,54,23,4,55,23,5,6,776,523]

x = 11

if x in a:
    print("Encontrei")
else:
    print("Não encontrei")

#Inverte a ordem da lista
a.reverse()
print(a)

# Ordena os valores da lista
a.sort()
print(a)

nomes = ["joao", "david", "ricardo"]
nomes.sort()
print(nomes)

nomes.remove("david") # Remove um item baseado em seu valor
print(nomes)

removido = nomes.pop(0) # Remove o item baseado na posição e retorna o valor removido
print(nomes)
print(f"O item removido foi: {removido}")
