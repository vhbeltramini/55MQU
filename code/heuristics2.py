# Gerar Heurística para o problema do Múltiplo caixeiro viajante
'''
restrições:
garantir que todos m saiam do nodo 1
garantir que todos m voltem para o nodo 1
garantir que todos os nodos sejam visitados
garantir que todos os nodos sejam saidos
'''
from utils import ShowResult
import random


# print("Starting")


def Heurisitica2(distancesMatrix, nCities, nTravelerSalesman, showResult):
    vertices_Faltantes = []
    vertices_percoridos = [1]
    solution = []
    concluido = False

    for i in range(nCities):
        if i != 00:
            vertices_Faltantes.append(i + 1)

    for i in range(nTravelerSalesman):
        linha = [1]
        solution.append(linha)

    while not concluido:

        # calcular distancia para cada caixeiro de todos os vértices possíveis
        distancias = []
        for i in range(len(vertices_Faltantes)):
            caixdist = []
            for j in range(nTravelerSalesman):
                verticeatual = vertices_Faltantes[i]
                verticecaixeiro = solution[j][-1]
                dist = distancesMatrix[(verticecaixeiro, verticeatual)]
                caixdist.append(dist)

            distancias.append(caixdist)

        # acha a menor distância
        menor = 0
        menorCidade = 0
        menorcaixeiro = 0
        for i in range(len(vertices_Faltantes)):
            for j in range(nTravelerSalesman):
                dist = distancias[i][j]
                if i == 0 and j == 0:
                    menor = dist
                elif dist < menor:
                    menor = dist
                    menorCidade = i
                    menorcaixeiro = j

        verticemenor = vertices_Faltantes[menorCidade]
        solution[menorcaixeiro].append(verticemenor)
        del (vertices_Faltantes[menorCidade])
        vertices_percoridos.append(verticemenor)

        if len(vertices_Faltantes) == 0:
            concluido = True

    for j in range(nTravelerSalesman):
        solution[j].append(1)

    ShowResult(distancesMatrix, vertices_Faltantes, vertices_percoridos, solution, nTravelerSalesman, showResult)
    return solution


def Heuristica22(distancesMatrix, nCities, nTravelerSalesman, showResult):
    vertices_Faltantes = []
    vertices_percoridos = [1]
    solution = []
    concluido = False
    alfa = 50

    for i in range(nCities):
        if i != 00:
            vertices_Faltantes.append(i + 1)

    for i in range(nTravelerSalesman):
        linha = [1]
        solution.append(linha)

    while not concluido:

        # calcular distancia para cada caixeiro de todos os vértices possíveis
        distancias = []
        for i in range(len(vertices_Faltantes)):
            for j in range(nTravelerSalesman):
                caixdist = []
                verticeatual = vertices_Faltantes[i]
                verticecaixeiro = solution[j][-1]
                dist = distancesMatrix[(verticecaixeiro, verticeatual)]
                caixdist.append(dist)
                caixdist.append(i)
                caixdist.append(j)
                distancias.append(caixdist)

        # ordenar por insertion sort------------------------------
        for i in range(len(distancias)):
            aux = distancias[i]
            j = i - 1
            while (j >= 0) and (aux < (distancias[j])):
                distancias[j + 1] = distancias[j]
                j -= 1
            distancias[j + 1] = aux

        # pega uma distância aleatória entre as alfa selecionadas
        randomCidade = random.randint(0, int(len(vertices_Faltantes) * (alfa / 100)))

        # achar o caixeiro e a cidade com a menor distândia da menor soma
        menorCaixeiro = distancias[randomCidade][2]
        menorCidade = distancias[randomCidade][1]
        # print(distancias[randomCidade])
        # print(menorCidade)
        verticemenor = vertices_Faltantes[menorCidade]
        solution[menorCaixeiro].append(verticemenor)
        del (vertices_Faltantes[menorCidade])
        vertices_percoridos.append(verticemenor)

        if len(vertices_Faltantes) == 0:
            concluido = True

    if showResult:
        ShowResult(distancesMatrix, vertices_Faltantes, vertices_percoridos, solution, nTravelerSalesman, True)
    return solution
