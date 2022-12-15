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

print("Starting")


def Heurisitica1(distancesMatrix, nCities, nTravelerSalesman, showResult):
    vertices_Faltantes = []
    vertices_percoridos = [1]
    solution = []
    concluido = False

    # carrega cidades eliminando a primeira cidade que é o ponto inicial
    for i in range(nCities):
        if i != 00:
            vertices_Faltantes.append(i+1)

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

        # acha a melhor distância entre todas as somas de distâncias
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

        #achar o caixeiro com a menor distândia da menor soma
        menorcaixeiro = 0
        for j in range(nTravelerSalesman):
            if distancias[menorCidade][j] < distancias[menorCidade][menorcaixeiro]:
                menorcaixeiro = j

        verticemenor = vertices_Faltantes[menorCidade]
        solution[menorcaixeiro].append(verticemenor)
        del (vertices_Faltantes[menorCidade])
        vertices_percoridos.append(verticemenor)

        if len(vertices_Faltantes) == 0:
            concluido = True

    for j in range(nTravelerSalesman):
        solution[j].append(1)

    ShowResult(distancesMatrix, vertices_Faltantes, vertices_percoridos, solution, nTravelerSalesman, True)
    return solution

def Heurisitica12(distancesMatrix, nCities, nTravelerSalesman):
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
        distancias = []
        # calcular distancia para cada caixeiro de todos os vértices possíveis
        for i in range(len(vertices_Faltantes)):
            caixdist = []
            for j in range(nTravelerSalesman):
                verticeatual = vertices_Faltantes[i]
                verticecaixeiro = solution[j][-1]
                dist = distancesMatrix[(verticecaixeiro, verticeatual)]
                caixdist.append(dist)

            distancias.append(caixdist)

        # ordenar por insertion sort
        for i in range(len(vertices_Faltantes)):
            aux = distancias[i][0] + distancias[i][1] + distancias[i][2]
            aux2 = distancias[i]
            j = i-1
            while (j >= 0) and (aux < (distancias[j][0] + distancias[j][1] + distancias[j][2])):
                distancias[j+1] = distancias[j]
                j -= 1
            distancias[j+1] = aux2

        # pega uma distância aleatória entre as alfa selecionadas
        randomCidade = random.randint(0, int(len(vertices_Faltantes) * (alfa/100)))

        #achar o caixeiro com a menor distândia da menor soma
        menorcaixeiro = 0
        for j in range(nTravelerSalesman):
            if distancias[randomCidade][j] < distancias[randomCidade][menorcaixeiro]:
                menorcaixeiro = j

        verticemenor = vertices_Faltantes[randomCidade]
        solution[menorcaixeiro].append(verticemenor)
        del (vertices_Faltantes[randomCidade])
        vertices_percoridos.append(verticemenor)

        if len(vertices_Faltantes) == 0:
            concluido = True

    ShowResult(distancesMatrix, vertices_Faltantes, vertices_percoridos, solution, nTravelerSalesman, True)
    return solution