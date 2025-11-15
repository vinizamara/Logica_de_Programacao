def somar(matriz):
    soma = 0
    for linha in matriz:
        for i in linha:
            soma = soma + i
    return soma

def multipliquePares(matriz):
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if matriz[l][c] % 2 == 0:
                matriz[l][c] *= 3
    return matriz


def maiorValor(matriz):
    maior = matriz[0][0]
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if matriz[l][c] > maior:
                maior = matriz[l][c] 
    return maior

matriz = [[1, 2, 3],
          [9, 8, 7],
          [3, 5, 9]]

print(f"A soma dos valores da matriz é {somar(matriz)}")
print(f"Os valores da matriz com os números pares multiplicados por 3 é: {multipliquePares(matriz)}")
print(f"O maior valor da matriz é: {maiorValor(matriz)}")
