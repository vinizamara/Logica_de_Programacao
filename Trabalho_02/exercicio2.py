'''
Uma escola precisa de um sistema para cadastrar notas dos alunos e gerar relatórios estatísticos. O programa deve: 1. Cadastrar múltiplos alunos (nome e nota) 2. Calcular estatísticas das notas 3. Permitir que o usuário cadastre quantos alunos desejar 4. Validar notas (apenas entre 0 e 10) 5. Gerar relatório fi nal Escreva um programa em Python que: ● Use um loop para cadastrar alunos até que o usuário decida parar ● Para cada aluno, solicite nome e nota (validando a entrada) ● Ao fi nal, exiba:
○ Quantidade de alunos cadastrados
○ Média geral das notas
○ Maior e menor nota
○ Porcentagem de alunos aprovados (nota ≥ 7)
○ Lista de alunos com suas situações (Aprovado/Reprovado)
'''

def cadastrarAluno(vetor):
    nome = str(input("Qual o nome do aluno? "))
    nota = float(input("Qual a nota do aluno? "))
    while nota < 0 or nota > 10:
        print("Valor de nota inválido, tente novamente.")
        nota = float(input("Qual a nota do aluno? "))
    vetor.append({
        "nome": nome, "nota": nota
    })
    print(f"Aluno {nome} cadastrado com sucesso")

def exibirAlunos(vetor):
    for aluno in vetor:
        print(f"Nome: {aluno["nome"]}, Nota: {aluno["nota"]}")
    
def estatisticas(vetor):
    quantAluno = 0
    quantAprovado = 0
    notas = []
    for aluno in vetor:
        quantAluno += 1
        notas.append(aluno['nota'])
        if aluno['nota'] >= 7:
            quantAprovado += 1
    
    print(f"Quantidade de alunos cadastrados é: {quantAluno}")
    print(f"Média Geral de notas é: {sum(notas)/len(notas)}")
    print(f"A maior nota é: {max(notas)} / A menor nota é: {min(notas)}")
    print(f"A porcentagem de alunos aprovados é: {(quantAprovado/len(vetor))*100}%")

    print("================================================")
    print("Aqui está a lista de alunos com suas situações: ")
    for aluno in vetor:
        if aluno['nota'] >= 7:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"
        print(f"Nome: {aluno["nome"]}, Nota: {aluno["nota"]}, situação: {situacao}")

alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.0},
    {"nome": "Carla", "nota": 9.2},
    {"nome": "Diego", "nota": 4.8},
    {"nome": "Eduarda", "nota": 7.0},
    {"nome": "Felipe", "nota": 5.5},
    {"nome": "Gabriela", "nota": 10.0},
    {"nome": "Henrique", "nota": 3.9},
    {"nome": "Isabela", "nota": 7.8},
    {"nome": "João", "nota": 6.7}
]

opcao = 0
while opcao != 3:
    opcao = int(input("Escolha uma opção: 1)Cadastrar Aluno 2)Listar Alunos Cadastrados 3)Exibir Relatório e Finalizar Programa // "))
    match opcao:
        case 1:
            cadastrarAluno(alunos)
        case 2:
            exibirAlunos(alunos)
        case 3:
            estatisticas(alunos)
        case _:
            print("Opção Invalida")
