# Gerar Heurística para o problema do Múltiplo caixeiro viajante
'''
restrições:
garantir que todos m saiam do nodo 1
garantir que todos m voltem para o nodo 1
garantir que todos os nodos sejam visitados
garantir que todos os nodos sejam saidos
'''

print("Starting")


def Heurisitica1(matriz, Ncidade, TravelerSalesman):
    distancesMatrix = matriz
    caixeiros = 3
    vertices_Faltantes = []
    vertices_percoridos = [1]
    percorridos = []
    concluido = False

    for i in range(Ncidade):
        if i != 00:
            vertices_Faltantes.append(i+1)

    for i in range(caixeiros):
        linha = [1]
        percorridos.append(linha)

    while concluido == False:
        print("----------------------------------------------")
        distancias = []
        # calcular distancia para cada caixeiro de todos os vértices possíveis
        for i in range(len(vertices_Faltantes)):
            caixdist = []
            for j in range(caixeiros):
                verticeatual = vertices_Faltantes[i]
                verticecaixeiro = percorridos[j][-1]
                dist = distancesMatrix[(verticecaixeiro-1, verticeatual-1)]
                print(percorridos[j][-1]-1)
                print(verticeatual-1)
                caixdist.append(dist)
            
            distancias.append(caixdist)
            print(distancias)
            print(i)

        print("Distancias ==")
        print(distancias)

        # Soma as distâncias e acha a menor distância
        menor = 0
        menorCidade = 0
        for i in range(len(vertices_Faltantes)):
            soma = 0
            for j in range(caixeiros):
                soma += distancias[i][j]
            if i == 0:
                menor = soma
            elif soma < menor:
                menor = soma
                menorCidade = i

        print("soma Dis ==")
        print(menor)
        print(menorCidade)

        print(vertices_Faltantes)
        print(vertices_percoridos)

        #achar o caixeiro com a menor distândia da menor soma
        menorcaixeiro = 0
        for j in range(caixeiros):
            if distancias[menorCidade][j] < distancias[menorCidade][menorcaixeiro]:
                menorcaixeiro = j
        print(menorcaixeiro)
        verticemenor = vertices_Faltantes[menorCidade]
        percorridos[menorcaixeiro].append(verticemenor)
        del (vertices_Faltantes[menorCidade])
        vertices_percoridos.append(verticemenor)

        print(vertices_Faltantes)
        print(vertices_percoridos)

        if len(vertices_Faltantes) == 0:
            concluido = True

    ShowResult(vertices_Faltantes, vertices_percoridos, percorridos)
    return percorridos

def Heurisitica12(matriz, Ncidade, TravelerSalesman):
    distancesMatrix = matriz
    caixeiros = 3
    vertices_Faltantes = []
    vertices_percoridos = [1]
    percorridos = []
    concluido = False
    alfa = 50

    for i in range(Ncidade):
        if i != 00:
            vertices_Faltantes.append(i+1)

    for i in range(caixeiros):
        linha = [1]
        percorridos.append(linha)

    while concluido == False:
        print("----------------------------------------------")
        distancias = []
        # calcular distancia para cada caixeiro de todos os vértices possíveis
        for i in range(len(vertices_Faltantes)):
            caixdist = []
            for j in range(caixeiros):
                verticeatual = vertices_Faltantes[i]
                verticecaixeiro = percorridos[j][-1]
                dist = distancesMatrix[(verticecaixeiro-1, verticeatual-1)]
                print(percorridos[j][-1]-1)
                print(verticeatual-1)
                caixdist.append(dist)
            
            distancias.append(caixdist)
            print(distancias)
            print(i)

        print("Distancias ==")
        print(distancias)

        # Soma as distâncias e acha a menor distância
        menor = 0
        menorCidade = 0
        for i in range(len(vertices_Faltantes)):
            soma = 0
            for j in range(caixeiros):
                soma += distancias[i][j]
            if i == 0:
                menor = soma
            elif soma < menor:
                menor = soma
                menorCidade = i

        print("soma Dis ==")
        print(menor)
        print(menorCidade)

        print(vertices_Faltantes)
        print(vertices_percoridos)

        #achar o caixeiro com a menor distândia da menor soma
        menorcaixeiro = 0
        for j in range(caixeiros):
            if distancias[menorCidade][j] < distancias[menorCidade][menorcaixeiro]:
                menorcaixeiro = j
        print(menorcaixeiro)
        verticemenor = vertices_Faltantes[menorCidade]
        percorridos[menorcaixeiro].append(verticemenor)
        del (vertices_Faltantes[menorCidade])
        vertices_percoridos.append(verticemenor)

        print(vertices_Faltantes)
        print(vertices_percoridos)

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