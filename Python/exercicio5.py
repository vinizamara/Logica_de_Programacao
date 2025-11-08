#Tratamento de listas de números

def mediaAritmetica(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    media = soma/len(numeros)
    #É possivel utilizar: sum(numeros)/len(numeros)
    return media

def mediaPonderada(numeros, pesos):
    soma = 0
    somaPesos = 0
    for i in range(len(numeros)):
        soma += numeros[i] * pesos[i]
        somaPesos += pesos[i]
    media = soma /somaPesos
    return media

def exibirMedias(mediaAritmetica, mediaPonderada):
    print(f"A média aritmética dos números na lista anterior é {mediaAritmetica:.2f}")
    print(f"A média ponderada dos números e os pesos das listas anteriores é {mediaPonderada:.2f}")
    print(f"A razão da média aritmética e a média ponderada é {(mediaAritmetica/mediaPonderada):.2f}")

    
        

listaNumeros = [1, 2, 3, 4, 5]
listaPesos = [1, 2, 3, 4, 5]

print(f"A lista de números têm os seguintes valores: {listaNumeros}")
print(f"A lista de pesos têm os seguintes valores: {listaNumeros}")
exibirMedias(mediaAritmetica(listaNumeros), mediaPonderada(listaNumeros, listaPesos))
