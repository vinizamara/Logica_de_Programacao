#Função para calcular

def calcular(a, b, operacao):
    resultado = 0
    if operacao.upper() == "A":
        resultado = a + b
    elif operacao.upper() == "B":
        resultado = a - b
    elif operacao.upper() == "C":
        resultado = a * b
    elif operacao.upper() == "D":
        resultado = a / b
    return resultado

a = float(input("Escolha o valor do primeiro número:"))
b = float(input("Escolha o valor do segundo número:"))
operacao = str(input("Escolha entre uma das operações a seguir: a)Somar b) subtrair c)Multipliar d)Dividir // "))

print(f"O resultado é {calcular(a, b, operacao)}")
