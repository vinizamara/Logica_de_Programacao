#Cálculo de CDB e LCA

def calculoInvestimento(juros, valor, prazo):
    total = valor
    for i in range(1, prazo+1):
        acrescimo = total * juros
        total = total + acrescimo
        print(f"Ano {i}: Rendimento = {acrescimo:.2f} / Total = {total:.2f}")

print("Escolha uma opção de Investimento:")
print("A)CDB B)LCA C)Poupança")
investimento = str(input("Qual a sua escolha? (Escreva a letra da aternativa em maiuscula)"))

juros = 0
if investimento == "A":
    juros = 0.145
elif investimento == "B":
    juros = 0.115
elif investimento == "C":
    juros = 0.06

valor = float(input("Qual o valor que você deseja adicionar? "))
prazo = int(input("Por quantos anos?(digite 5, 10 ou 20) "))

print("O qualculo do rendimento durante o périodo digitado é: ")
calculoInvestimento(juros, valor, prazo)
