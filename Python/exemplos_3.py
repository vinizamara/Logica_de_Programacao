#Exemplo de lista
n = 5
notas = []
for i in range(1, n+1):
    x = int(input("Nota do aluno: "))
    notas.append(x)

media = 0
for n1 in notas:
    media = media + n1
media = media / n1

for n1 in notas:
    if n1 > media:
        print("Aprovado: ", n1)
