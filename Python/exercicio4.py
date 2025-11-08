# Verificar vogais

frase = str(input("Forneça a frase que deseja verificar:"))

def verificarVogal(frase):
    contVogais = 0
    for i in frase:
        if i.upper() == "A" or i.upper() == "E" or i.upper() == "I" or i.upper() == "O" or i.upper() == "U":
            contVogais += 1
    return contVogais

'''
Outra forma de fazer:
def verificarVogal(frase):
    vogais = "aeiou"
    contVogais = 0
    for i in frase:
        if i in vogais:
            contVogais += 1
    return contVogais
'''
        

print(f"Existe um total de {verificarVogal(frase)} vogais na frase")
