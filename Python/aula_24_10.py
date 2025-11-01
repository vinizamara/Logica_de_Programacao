lista1 = [1, 2, 3, 4]
lista2 = [9, 8, 7, 6]

#Exemplo de concatenação ou uniao
x = lista1 + lista2
print(x) #Retorna a junção das duas listas

y = lista1 * 3 #Repete a mesma lista 3 vezes
print(y)

del y[5] #Remove o item da posição
print(y)

#Copia
c = y[:]
print('c', x)
c.append(444)
print(c)
print('a: ', y)

#Endereços de memoria:
print(id(a))
print(id(b))
print(id(c))

#Verificar se um item consta na lista
if 7 in c:
    print("7 está na lista")
    
    
#Inserir em seção especifica:
c.insert(0, 99) #Insert(index, valor)

#Listas alinhadas

matriz = [[1,2,3],[4,5,6],[7,8,9]]
print(matriz)
print(matriz[0][1])
matriz[0][1] = "oi"
print(matriz)

##Append funciona para adicionar outro vetor
matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz.append([10,11,12])
print(matriz)

##Usando del em uma matriz
print(matriz[1][1])
del matriz[2][0]
print(matriz)

##Forma diferente de mostrar uma matriz
print("#### Matriz Impressao ####")
soma = 0
for linha in matriz:
    for coluna in linha:
        print(coluna)
        soma += coluna
print("Soma matriz: ", soma)

#Compreenssão de lista
quadrados = []

for x in range(10):
    quadrados.append(x**2)
    
print(quadrados)

listaQuadrados = [x**2 for x in range(10)]
print(listaQuadrados)

#Sublistas
numeros = [1,2,3,4,5]
##sublista valores < 4
sublista = []
for n in numeros:
    if n < 4:
        sublista.append(n)
print(sublista)

listab = [n for n in numeros if n < 4]
print(listab)

#Tuplas
##Tuplas não podem ser alteradas
aluno = ("joao da silva", 1111, 23.40)

print("Acesso posicional da tupla")
print("Nome", aluno[0])
print("Codigo", aluno[1])
print("Nota", aluno[2])

##Tuplas podem ser juntadas
aluno2 = ("Maria", 222, 33.22)
alunos = aluno + aluno2
print(alunos)

#Dicionarios
dicionario = {"nome": "joao", "codigo": 10}

print(dicionario)

##pop obtem o valor relativo a uma chave e remove
x = dicionario.pop("codigo")
print(x)
print(dicionario)

a = dicionario.popitem()
print(a)
print(dicionario)

##Adicionando Valores
aluno = {
    "nome": "joao",
    "curso": "Computacao",
    "instituicao": "facef",
    "codigo": 1919
}
print(aluno)
print(aluno['nome'])
aluno['disciplina'] = "logica"
print(aluno)

##Fazer copia
dic1 = {"nome": "ana", "codigo": 1123}
print(dic1)

dic2 = dic1
print(dic2)

dic2['codigo'] = 999
print("dic2: ", dic2)
print("dic1: ", dic1)

copia = dic1.copy()
print(copia)

print(id(dic1))
print(id(dic2))
print(id(copia))

#Retorna o valor de uma chave ou valor padrao, Se a chave não existir, porém é opcional
a = copia.get("codigo")
print(a)
print(copia)

##Métodos de dicionarios
print(copia.keys())
print(copia.values())

