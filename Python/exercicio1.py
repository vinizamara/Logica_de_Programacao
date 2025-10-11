quantidadeProduto = []
valorProduto = []
total = []

for i in range(5):
    quantidadeProduto.append(int(input(f"Qual a quantidade do produto {i+1}?")))
    valorProduto.append(float(input(f"Qual o valor do produto{i+1}?")))
    total.append(float(quantidadeProduto[i] * valorProduto[i]))

print("A quantidade de cada produto:")
print(quantidadeProduto)


print("O valor de cada produto:")
print(valorProduto)

print("O total de cada produto:")
print(total)

somaTotal = 0
maiorValorQuantidade = quantidadeProduto[0]
maiorValor = valorProduto[0]
for i in range (5):
    somaTotal += quantidadeProduto[i] * valorProduto[i]
    if (maiorValor < valorProduto[i]):
        maiorValor = valorProduto[i]
        maiorValorQuantidade = quantidadeProduto[i]

print(f"A quantidade do produto de maior valor é: {maiorValorQuantidade}")

print(f"A soma do total dos produtos é: {somaTotal}")

