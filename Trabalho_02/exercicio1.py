'''
Uma loja online oferece descontos especiais baseados em dois critérios: ● Idade do cliente (estudante: <25 anos OU sênior: ≥60 anos) ● Valor total da compra As regras de desconto são: ● Clientes estudantes (<25 anos) OU sênior (≥60 anos) recebem desconto adicional ● Compras acima de R$ 200,00 têm desconto base de 10% ● Compras acima de R$ 500,00 têm desconto base de 15% Descontos especiais por categoria: ● Estudantes: +5% de desconto adicional ● Sênior: +7% de desconto adicional Escreva um programa em Python que: 1. Solicite a idade do cliente e o valor total da compra 2. Calcule o valor fi nal com os descontos apropriados 3. Informe:
○ O valor do desconto base
○ O valor do desconto adicional (se aplicável)
○ O valor final a ser pago
'''

idade = int(input("Qual a idade do cliente? "))
valorTotal = float(input("Qual o valor total da compra? "))
desconto = 0


if valorTotal > 200 and valorTotal <= 500:
    desconto = 0.1
    print(f"Você teve um desconto base de 10%, ou seja, R${(valorTotal * desconto):.2f}!")

elif valorTotal > 500:
    desconto = 0.15
    print(f"Você teve um desconto base de 15%, ou seja, R${(valorTotal * desconto):.2f}!")

if idade < 25:
    desconto += 0.05
    print(f"E um desconto adicional de 5% por ser estudante, ou seja, R${(valorTotal * 0.05):.2f}!")

elif idade >= 60:
    desconto += 0.07
    print(f"E um desconto adicional de 7% por ser Sênior, ou seja, R${(valorTotal * 0.07):.2f}!")

print(f"O valor final a ser pago é R${(valorTotal * (1.0 - desconto)):.2f}")

