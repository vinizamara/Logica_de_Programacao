#Relembrando:
nota = float(input("Qual o valor desejado da nota? "))

if (nota >= 30 and nota < 60):
  print("Está de sub!")

else:
  print("Não está de sub...")

#Exercício 1:
#Cadastro de Vendas

nomeProduto = str(input("Qual o nome do produto? "))
valor = float(input("Qual o valor do produto? "))
quantidade = int(input("Qual a quantidade do produto? "))
metodoPagamento = str(input("Qual o método de pagamento? (1 = a vista 2 = a prazo) "))
total = 0

if metodoPagamento == "2":
  numParcelas = int(input("Qual o número de parcelas? "))
  acrescimo = 0
  if numParcelas <= 5:
    acrescimo = 0.15
  if numParcelas > 5:
    acrescimo = 0.20
  adicional = (valor * quantidade) * acrescimo
  total = (valor * quantidade) + adicional
  parcelas = total / numParcelas
  print("O valor total ficou: R$", total)
  print("O valor de cada parcela ficou: R$", parcelas)
  print("O valor adicional pago por ser parcelado foi: R$", adicional)

if metodoPagamento == "1":
  total = valor * quantidade
  totalLiquido = total * 0.90
  print("O preço total da venda foi: R$", total)
  print("O valor do desconto de 10% foi de: R$", float((total * 0.10)))
  print("Portanto, o total liquido foi de: R$", float((totalLiquido)))

'''
Versão simplificada:
# Cadastro de Vendas

nome_produto = input("Qual o nome do produto? ")
valor = float(input("Qual o valor do produto? "))
quantidade = int(input("Qual a quantidade do produto? "))
metodo_pagamento = input("Qual o método de pagamento? (1 = à vista, 2 = a prazo) ")

total = valor * quantidade

if metodo_pagamento == "2":
    num_parcelas = int(input("Qual o número de parcelas? "))
    acrescimo = 0.15 if num_parcelas <= 5 else 0.20

    adicional = total * acrescimo
    total_com_acrescimo = total + adicional
    parcelas = total_com_acrescimo / num_parcelas

    print(f"\nO valor total ficou: R$ {total_com_acrescimo:.2f}")
    print(f"O valor de cada parcela ficou: R$ {parcelas:.2f}")
    print(f"O valor adicional pago por ser parcelado foi: R$ {adicional:.2f}")

elif metodo_pagamento == "1":
    desconto = total * 0.10
    total_liquido = total - desconto

    print(f"\nO preço total da venda foi: R$ {total:.2f}")
    print(f"O valor do desconto de 10% foi de: R$ {desconto:.2f}")
    print(f"Portanto, o total líquido foi de: R$ {total_liquido:.2f}")

else:
    print("\nOpção de pagamento inválida.")
'''

#Exemplo de Repetição
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = a+1

print("Os números entre esses dois valores são:")
while c < b:
    print(c)
    c = c + 1

#Exemplo de for...in...
print("Exemplo de for...in...:")
for x in [5, 20, 16, 18, 55, 59]: #Exibira os números na sequência
  print(x)

#Exemplo de Range
for x in range(5):
  print(x) # Escreve de 0 até 5

for x in range(3, 10):
  print(x) # Escreve de 3 até 9

for x in range(3,10,2):
  print(x) # Escreve de 3 até 9 pulando de 2 em 2

#Exibir tabuada
tabuada = int(input("Qual o número que você deseja ver a tabuada? "))

for i in range(11):
  resultado = tabuada * i
  print(tabuada, "X", i, "=", resultado)
