#Gerenciamento de produtos
produtos = []

def criarProduto(lista):
    codigo = int(input("Qual o código do produto?"))
    desc = str(input("Qual a descrição do produto?"))
    valor = float(input("Qual o valor do produto?"))
    lista.append({
        "codigo": codigo,
        "desc": desc,
        "valor": valor
    })

def alterarValor(lista):
    codigo = int(input("Qual o código do produto que você quer alterar?"))
    novoValor = float(input("Qual o novo valor do produto?"))
    for produto in lista:
        if produto["codigo"] == codigo:
            produto["valor"] = novoValor
            print("Produto Alterado com sucesso!")
    

opcao = 0
while opcao != 4:
    opcao = int(input("Escolha uma opção: 1)Criar Produto 2)Alterar Valor do Produto 3)Mostrar Produtos Cadastrados 4)Finalizar programa // "))
    match opcao:
        case 1:
            criarProduto(produtos)
        case 2:
            alterarValor(produtos)
        case 3:
            print(produtos)
        case 4:
            print("Programa Finalizado!")
        case _:
            print("Opção Invalida")

