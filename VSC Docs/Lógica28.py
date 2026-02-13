def mover_esquerda(matriz):
    nova_matriz = []

    for linha in matriz:
        nova_linha = [num for num in linha if num != 0]
        while len(nova_linha) < 4:
            nova_linha.append(0)
        
    for i in range(3):
        if nova_linha[i] == nova_linha[i + 1] and nova_linha[i] != 0:
            nova_linha[i] *= 2
            nova_linha[i + 1] = 0
        
    nova_linha = [num for num in nova_linha if num != 0]
    while len(nova_linha) < 4:
        nova_linha.append(0)
    
    nova_matriz.append(nova_linha)
    return nova_matriz
    
matriz = [
    [4, 0, 2, 0],
    [4, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

resultado = mover_esquerda(matriz)

for linha in resultado:
    print(linha)