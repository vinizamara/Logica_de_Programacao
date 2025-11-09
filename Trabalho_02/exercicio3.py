'''
A MODA de um vetor de números é o número no vetor que é repetido com maior frequência. Se mais de um número for repetido com frequência máxima igual, não existirá uma moda. Fazer um programa que leia um vetor de números positivos (validar a entrada de dados) e imprima a moda do vetor ou uma mensagem que a moda não existe. Fazer uma função para a moda.
'''

def cadastrarNumero(vetor):
    numero = float(input("Qual o número que deseja cadastrar? "))
    while numero < 0:
        print("Valor de número inválido, tente novamente.")
        numero = float(input("Qual o número que deseja cadastrar? "))
    vetor.append(numero)
    print(f"O número '{numero}' foi cadastrado com sucesso")

def exibirNumeros(vetor):
    for numero in vetor:
        print(numero)
    
def moda(vetor):
    numerosVerificados = {}
    for numero in vetor:
        if numero not in numerosVerificados:
            numerosVerificados[numero] = 1
        else:
            numerosVerificados[numero] += 1
    modaValor = max(numerosVerificados.values())
    empate = 0
    for numero, quantidade in numerosVerificados.items():
        if quantidade == modaValor:
            empate += 1
            moda = numero
    if empate > 1:
        print("Não existe moda!")
    else:
        print("A moda dos números foi o número: ", moda)         

numeros = [5, 8, 8, 8, 9, 5, 3, 7, 6, 2]

opcao = 0
while opcao != 4:
    opcao = int(input("Escolha uma opção: 1)Cadastrar Número 2)Listar Números Cadastrados 3)Calcular Moda dos Números 4)Finalizar Programa // "))
    match opcao:
        case 1:
            cadastrarNumero(numeros)
        case 2:
            exibirNumeros(numeros)
        case 3:
            moda(numeros)
        case 4:
            print("Programa Finalizado!")
        case _:
            print("Opção Invalida")
