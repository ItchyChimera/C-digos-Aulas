funcionarios = [
    [5,2,3],
    [3,4,2],
    [2,1,5],
]

projetos = [
    [4,3,2],
    [2,1,5],
]

for i in range(len(projetos)):
    melhor_funcionario = -1
    melhor_pontuação = -1

    for j in range(len(funcionarios)):
        pontuação = 0

        for k in range(3):
            pontuação += funcionarios[j][k] * projetos[i][k]   
            projetos[i][k]

        if pontuação > melhor_pontuação:
            melhor_pontuação = pontuação
            melhor_funcionario = j + 1

        print(f"O funcionario {melhor_funcionario} é o mais adequado para o projeto {i + 1} (Pontuação:{melhor_pontuação})")