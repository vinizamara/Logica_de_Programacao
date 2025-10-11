#Exemplo 1:
print("Unifacef \nAlgoritmo")

x = 10

print("X vale:", x)

y = 33.3
print(type(y))

a = 'facef'
print(type(a))

#Exemplo 2:
idade = 22
altura = 1.78

print(f"A idade é {idade} e a altura é {altura}")

#Exemplo 3:
idade = 22
altura = 1.78

print(f"A idade é {idade} e a altura é {altura}")

nome = input("Digite seu nome: ") # input transforma a resposta em texto
print("Seu nome é:", nome)

x = "0"

int(x) # Converte x para inteiro

round(x) # Converte x para inteiro através do arredondamento

float(x) # coverte x para ponto-flutuante

str(x) # Transforma o número em string.

#Exemplo 4:
a = int(input("Forneça um número: "))

print("O dobro de", a, "é:", a*2)

#a = input("Forneça um número: ")
#print("O dobro de", a, "é:", int(a)*2)

#Exemplo 5:
import math # Importa uma biblioteca

print(math.e)

print(math.pi)

print(math.sqrt(4))

print(dir(math)) # Este comando mostra todos os comandos de um modulo

#Exemplo 6:
x = int(input("Digite um número: "))

if x > 0:
    print("positivo")

print("Fim do programa")

#Exemplo 7:
nota = int(input("Qual a nota do aluno?"))

if nota >= 30 and nota < 60:
    print("Está de sub")

if nota >= 60:
    print("Não está de sub")

# Exemplo 7
a = int(input("Digite o valor de A:"))
b = int(input("Digite o valor de B:"))

while a <= b:
    print(a)
    a = a + 1
    
print("Fim do programa")

# Exemplo 8
n = int(input("Digite a quantidade de números que deseja calcular a média: "))
i = 0
soma = 0
while i < n:
    numero = float(input("Digite o valor: "))
    soma = soma + numero
    numero = 0
    i = i + 1

media = soma/n
print("A media dos números é:", media)

# Exemplo 9
for n in [10, 30, 55, 11, -1, 15]:
    print(n)
    
lista = [10, 30, 55, 11, -1, 15]
for n2 in lista:
    print(n2)

for n in ["Carro", "Moto", "Caminhão"]:
    print(n)

for x in range(2,5):
    print(x)
