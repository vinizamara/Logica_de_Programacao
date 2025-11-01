#Função

##Se inicia com a palavra def
def imprimeCompras():
    compras = ["Miojo", "Ovo", "Leite", "Pão"]
    print("Lista de compras")
    for item in compras:
        print("Produto: ", item)
##Fim da função

print("Antes da função")

imprimeCompras()

print("Depois da função")

##Parâmetros com valor padrão
def reajuste(salario, juros = 0.25):
    return salario + salario * juros

print("Reajuste 1: ", reajuste(100))
print("Reajuste 2: ", reajuste(100,0.10))


##É possivel utilizr dois returns em uma função, por exemplo:
def maior(x, y):
    if x > y:
        return x
    else:
        return y
        print("Essa mensagem não será impressa!")
# fim da função

x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))
z = maior(x, y)
print("O maior valor é: ", z)
