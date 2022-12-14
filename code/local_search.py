# Local search implementations to solve the multiple traveling salesman problem
'''
restrições:
garantir que todos m saiam do nodo 1
garantir que todos m voltem para o nodo 1
garantir que todos os nodos sejam visitados
garantir que todos os nodos sejam saidos
'''
from utils import CalculateObjetiveFunction, CalculateObjetiveFunctionWithPrintForLocalSearch
from copy import copy, deepcopy

def LocalSearchM(distancesMatrix, nCities, nTravalers, initialSolution):
    print("starting local search")
    for i in range(nTravalers):
        initialSolution[i].pop(-1)
        initialSolution[i].pop(0)
    iterations = 0
    while(iterations < 1):
        newIntinalSol = intra_route_shift(distancesMatrix, nCities, nTravalers, initialSolution)
        CalculateObjetiveFunctionWithPrintForLocalSearch(distancesMatrix, newIntinalSol, nTravalers, True)
        iterations += 1


def calculatedImprove(distancesMatrix, solutionToBeCalculated):
    for i in range(len(solutionToBeCalculated)):
        for y in range(len(solutionToBeCalculated[i])):
            print(y)

def intra_route_shift(distancesMatrix, nCities, nTravalers, initialSolution):
    print("intra_route_shift")
    bestTotalCost = CalculateObjetiveFunction(distancesMatrix, initialSolution, nTravalers)
    for i in range(nTravalers):
        for x in range(len(initialSolution[i])-1):
            for y in range(len(initialSolution[i])-1):
                initialSolutionAux = deepcopy(initialSolution)

                # print("I", i)
                # print("Y", y)
                # print("initialSolution[i][y]", initialSolution[i][y])
                # print("initialSolution[i]", initialSolution[i])
                # initialSolution[i].insert(y, initialSolution[i][x])
                initialSolution[i].insert(y, initialSolution[i].pop(x))

                newTotalCost = CalculateObjetiveFunction(distancesMatrix, initialSolution, nTravalers)
                # print(initialSolution)
                # print("bestTotalCost "+str(bestTotalCost))
                # print("newTotalCost "+str(newTotalCost))
                if newTotalCost < bestTotalCost:
                    # print("melhorou")
                    bestTotalCost = newTotalCost
                    continue
                else:
                    initialSolution = deepcopy(initialSolutionAux)

    return initialSolution

def intra_route_shift_two(distancesMatrix, nCities, nTravalers, initialSolution):
    print("intra_route_shift")
    bestTotalCost = CalculateObjetiveFunction(distancesMatrix, initialSolution, nTravalers)
    for i in range(nTravalers):
        for x in range(len(initialSolution[i])-1):
            for y in range(len(initialSolution[i])-1):
                auxY = initialSolution[i][y]
                auxX = initialSolution[i][x]
                initialSolution[i][y] = auxX
                initialSolution[i][x] = auxY
                newTotalCost = CalculateObjetiveFunction(distancesMatrix, initialSolution, nTravalers)
                if newTotalCost < bestTotalCost:
                    bestTotalCost = newTotalCost
                    continue
                else:
                    initialSolution[i][y] = auxY
                    initialSolution[i][x] = auxX
    return initialSolution



def calc_shift_cost(inital_pos, next_pos_candidate):
    print("inter_route_shift")



def inter_route_shift(instance, S):
    print("inter_route_shift")


def showResultLocalSearhM(vertices_Faltantes, vertices_percoridos, solution):
    print("Local Search solution")
    print("vertices faltantes: " + vertices_Faltantes)
    print()
    print("vertices percoridos: " + vertices_percoridos)
    print(vertices_percoridos)
    print()
    print("solution: " + solution)
