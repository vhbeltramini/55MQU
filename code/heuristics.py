# Gerar Heurística para o problema do Múltiplo caixeiro viajante
'''
restrições:
garantir que todos m saiam do nodo 1
garantir que todos m voltem para o nodo 1
garantir que todos os nodos sejam visitados
garantir que todos os nodos sejam saidos
'''
from utils import ShowResult

print("Starting")


def Heurisitica1(distancesMatrix, nCities, nTravelerSalesman):
    vertices_Faltantes = []
    vertices_percoridos = [1]
    solution = []
    concluido = False

    for i in range(nCities):
        if i != 00:
            vertices_Faltantes.append(i+1)

    for i in range(nTravelerSalesman):
        linha = [1]
        solution.append(linha)

    while concluido == False:
        # print("----------------------------------------------")
        distancias = []
        # calcular distancia para cada caixeiro de todos os vértices possíveis
        for i in range(len(vertices_Faltantes)):
            caixdist = []
            for j in range(nTravelerSalesman):
                verticeatual = vertices_Faltantes[i]
                verticecaixeiro = solution[j][-1]
                dist = distancesMatrix[(verticecaixeiro, verticeatual)]
                #print(solution[j][-1]-1)
                #print(verticeatual-1)
                caixdist.append(dist)
            
            distancias.append(caixdist)
            #print(distancias)
            #print(i)

        #print("Distancias ==")
        #print(distancias)

        # Soma as distâncias e acha a menor distância
        menor = 0
        menorCidade = 0
        for i in range(len(vertices_Faltantes)):
            soma = 0
            for j in range(nTravelerSalesman):
                soma += distancias[i][j]
            if i == 0:
                menor = soma
            elif soma < menor:
                menor = soma
                menorCidade = i

        #print("soma Dis ==")
        #print(menor)
        #print(menorCidade)

        #print(vertices_Faltantes)
        #print(vertices_percoridos)

        #achar o caixeiro com a menor distândia da menor soma
        menorcaixeiro = 0
        for j in range(nTravelerSalesman):
            if distancias[menorCidade][j] < distancias[menorCidade][menorcaixeiro]:
                menorcaixeiro = j
        #print(menorcaixeiro)
        verticemenor = vertices_Faltantes[menorCidade]
        solution[menorcaixeiro].append(verticemenor)
        del (vertices_Faltantes[menorCidade])
        vertices_percoridos.append(verticemenor)

        #print(vertices_Faltantes)
        #print(vertices_percoridos)

        if len(vertices_Faltantes) == 0:
            concluido = True

    for j in range(nTravelerSalesman):
        solution[j].append(1)

    ShowResult(distancesMatrix, vertices_Faltantes, vertices_percoridos, solution, nTravelerSalesman)
    return solution

def Heurisitica12(distancesMatrix, nCities, nTravelerSalesman):
    vertices_Faltantes = []
    vertices_percoridos = [1]
    solution = []
    concluido = False
    alfa = 50

    for i in range(nCities):
        if i != 00:
            vertices_Faltantes.append(i+1)

    for i in range(nTravelerSalesman):
        linha = [1]
        solution.append(linha)

    while concluido == False:
        #print("----------------------------------------------")
        distancias = []
        # calcular distancia para cada caixeiro de todos os vértices possíveis
        for i in range(len(vertices_Faltantes)):
            caixdist = []
            for j in range(nTravelerSalesman):
                verticeatual = vertices_Faltantes[i]
                verticecaixeiro = solution[j][-1]
                dist = distancesMatrix[(verticecaixeiro-1, verticeatual-1)]
                #print(solution[j][-1]-1)
                #print(verticeatual-1)
                caixdist.append(dist)
            
            distancias.append(caixdist)
            #print(distancias)
            #print(i)

        #print("Distancias ==")
        #print(distancias)

        # Soma as distâncias e acha a menor distância
        menor = 0
        menorCidade = 0
        for i in range(len(vertices_Faltantes)):
            soma = 0
            for j in range(nTravelerSalesman):
                soma += distancias[i][j]
            if i == 0:
                menor = soma
            elif soma < menor:
                menor = soma
                menorCidade = i

        #print("soma Dis ==")
        #print(menor)
        #print(menorCidade)

        #print(vertices_Faltantes)
        #print(vertices_percoridos)

        #achar o caixeiro com a menor distândia da menor soma
        menorcaixeiro = 0
        for j in range(nTravelerSalesman):
            if distancias[menorCidade][j] < distancias[menorCidade][menorcaixeiro]:
                menorcaixeiro = j
        #print(menorcaixeiro)
        verticemenor = vertices_Faltantes[menorCidade]
        solution[menorcaixeiro].append(verticemenor)
        del (vertices_Faltantes[menorCidade])
        vertices_percoridos.append(verticemenor)

        #print(vertices_Faltantes)
        #print(vertices_percoridos)

        if len(vertices_Faltantes) == 0:
            concluido = True

    ShowResult(distancesMatrix, vertices_Faltantes, vertices_percoridos, solution, nTravelerSalesman)
    return solution

# def ShowResult(vertices_Faltantes, vertices_percoridos, percorridos):
#     print()
#     print(vertices_Faltantes)
#     print()
#     print(vertices_percoridos)
#     print()
#     print(percorridos)