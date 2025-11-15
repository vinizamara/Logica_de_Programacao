# listaAlunos = [
#     {"codigo": 101, "notas": [8.5, 7.0, 9.0], "media": 8.17},
#     {"codigo": 102, "notas": [6.0, 5.5, 7.0], "media": 6.17},
#     {"codigo": 103, "notas": [9.2, 8.8, 9.5], "media": 9.17},
#     {"codigo": 104, "notas": [4.5, 6.0, 5.0], "media": 5.17},
#     {"codigo": 105, "notas": [7.5, 8.0, 7.0], "media": 7.50}
# ]

listaAlunos = []

def listarAlunos(dicionario):
    for i in dicionario:
        print(i)

def cadastrarAlunos(dicionario):
    print("Cadastre os alunos:")
    for i in range(5):
        codigo = int(input("Codigo: "))
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        dicionario.append({
        'codigo': codigo,
        'notas': [nota1, nota2, nota3],
        'media': ((nota1 + nota2 + nota3) / 3)
        })

def verificarAluno(dicionario, matricula):
    for i in range(len(dicionario)):
        if dicionario[i]['codigo'] == matricula:
            return dicionario[i]

def verificarMedia(dicionario):
    media = 0
    soma = 0
    quant = 0
    for i in range(len(dicionario)):
        for j in range(3):
            soma += dicionario[i]['notas'][j]
            quant += 1
    media = soma / quant
    print("A media geral dos alunos foi: ", media)

def mediaSuperior(dicionario):
    alunosSuperior = []
    for aluno in dicionario:
        if aluno['media'] > 6:
            alunosSuperior.append(aluno)
    print("Os alunos com média superior a 6 são: ")
    for aluno in alunosSuperior:
        print(aluno)

cadastrarAlunos(listaAlunos)

opcao = 0

while opcao != 5:
    opcao = int(input("Qual opção você deseja? 1)Listar alunos 2)Buscar aluno por codigo 3)Verificar média geral de notas dos alunos 4)Exibir alunos com média superior a 6 5) Finalizar programa / "))
    match opcao:
        case 1:
            listarAlunos(listaAlunos)
        case 2:
            matricula = int(input("Por favor, forneça o código do aluno que deseja buscar: "))
            if verificarAluno(listaAlunos, matricula) == None:
                print("Não encontrado!")
            else:
                print(f"O aluno existe: {verificarAluno(listaAlunos, matricula)}")
        case 3:
            verificarMedia(listaAlunos)
        case 4:
            mediaSuperior(listaAlunos)
        case 5:
            print("Programa Finalizado!")
        case _:
            print("Valor inválido!")

