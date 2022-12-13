# Gerar Heurística para o problema do Múltiplo caixeiro viajante
'''
restrições:
garantir que todos m saiam do nodo 1
garantir que todos m voltem para o nodo 1
garantir que todos os nodos sejam visitados
garantir que todos os nodos sejam saidos
'''

print("Starting")


def Heurisitica1(matriz, Ncidade):
    distancesMatrix = matriz
    caixeiros = 3
    vertices_Faltantes = []
    vertices_percoridos = [1]
    percorridos = [[1], [1], [1]]
    menor = 0
    concluido = False
    menorCidade = 0
    menorcaixeiro = 0
    print(distancesMatrix)

    for i in range(Ncidade):
        vertices_Faltantes.append(i)

    # print(vertices_Faltantes)

    while concluido == False:
        distancias = [[]] * caixeiros

        # calcular distancia para cada caixeiro de todos os vértices possíveis
        for i in range(len(vertices_Faltantes)):
            for j in range(caixeiros):
                distancias[j].append(distancesMatrix[(percorridos[j][-1], vertices_Faltantes[i])])

        print("Distancias ==")
        print(distancias)
        # Soma as distâncias e acha a menor distância
        somadis = [[]] * caixeiros
        for i in range(len(vertices_Faltantes)):
            index = i - 1
            linha = []
            soma = 0
            for j in range(caixeiros):
                linha.append(distancias[j][index])
                soma += distancias[j][index]
                somadis[j].append(linha)

            if index == 0:
                menor = soma
                menorCidade = 0
            elif soma < menor:
                menor = soma
                menorCidade = index

        # print(menorCidade)
        print("soma Dis ==")
        print(somadis)
        print(menor)

        menorcaixeiro = 0
        for j in range(caixeiros):
            print("----------------------------------------------")
            if somadis[j][j] < somadis[j][menorCidade]:
                menorcaixeiro = j

        verticemenor = vertices_Faltantes[menorCidade]
        percorridos[menorcaixeiro].append(verticemenor)
        del (vertices_Faltantes[menorCidade])
        vertices_percoridos.append(verticemenor)
        # print(menorCidade)
        # print(vertices_Faltantes)

        if len(vertices_Faltantes) == 0:
            concluido = True

    ShowResult(vertices_Faltantes, vertices_percoridos, percorridos)
    return percorridos


def ShowResult(vertices_Faltantes, vertices_percoridos, percorridos):
    print()
    print(vertices_Faltantes)
    print()
    print(vertices_percoridos)
    print()
    print(percorridos)
    print(len(percorridos))
