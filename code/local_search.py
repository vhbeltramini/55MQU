# Local search implementations to solve the multiple traveling salesman problem
'''
restrições:
garantir que todos m saiam do nodo 1
garantir que todos m voltem para o nodo 1
garantir que todos os nodos sejam visitados
garantir que todos os nodos sejam saidos
'''
from utils import CalculateObjetiveFunction, CalculateObjetiveFunctionWithPrintForLocalSearch, ShowRoutes, \
    ShowLocalSearchImproviments, CalculateObjetiveFunctionWithPrint
from copy import copy, deepcopy


def LocalSearchInterIntra(distancesMatrix, nCities, nTravelers, randomSolution, desiredIterations):
    print("starting local search")
    for i in range(nTravelers):
        randomSolution[i].pop(-1)
        randomSolution[i].pop(0)
    iterations = 0
    localSearchSol = randomSolution
    while iterations < desiredIterations:
        localSearchSol = intra_route_shift(distancesMatrix, nCities, nTravelers, localSearchSol, False)
        localSearchSol = inter_route_shift(distancesMatrix, nTravelers, localSearchSol, False)
        iterations += 1
    ShowLocalSearchImproviments(distancesMatrix, localSearchSol, randomSolution, nTravelers)


def LocalSearchIntra(distancesMatrix, nCities, nTravelers, randomSolution, desiredIterations, printSol):
    for i in range(nTravelers):
        randomSolution[i].pop(-1)
        randomSolution[i].pop(0)
    iterations = 0
    localSearchSol = randomSolution
    while iterations < desiredIterations:
        localSearchSol = intra_route_shift(distancesMatrix, nCities, nTravelers, localSearchSol, False)
        iterations += 1
    print("Initial Solution")
    CalculateObjetiveFunctionWithPrintForLocalSearch(distancesMatrix, randomSolution, nTravelers, True)
    print("Final Solution")
    return CalculateObjetiveFunctionWithPrintForLocalSearch(distancesMatrix, localSearchSol, nTravelers, printSol), \
        localSearchSol

def LocalSearchIntraGrasp(distancesMatrix, nCities, nTravelers, randomSolution, desiredIterations, printSol):
    for i in range(nTravelers):
        randomSolution[i].pop(-1)
        randomSolution[i].pop(0)
    iterations = 0
    localSearchSol = randomSolution
    while iterations < desiredIterations:
        localSearchSol = intra_route_shift(distancesMatrix, nCities, nTravelers, localSearchSol, False)
        iterations += 1
    return CalculateObjetiveFunction(distancesMatrix, localSearchSol, nTravelers, printSol), \
        localSearchSol


def LocalSearchInter(distancesMatrix, nCities, nTravelers, randomSolution, desiredIterations, printSol):
    for i in range(nTravelers):
        randomSolution[i].pop(-1)
        randomSolution[i].pop(0)
    iterations = 0
    localSearchSol = randomSolution
    while iterations < desiredIterations:
        print(iterations)
        localSearchSol = inter_route_shift(distancesMatrix, nTravelers, localSearchSol, printSol)
        iterations += 1
    print("Initial Solution")
    CalculateObjetiveFunctionWithPrintForLocalSearch(distancesMatrix, randomSolution, nTravelers, True)
    print("Final Solution")
    CalculateObjetiveFunctionWithPrintForLocalSearch(distancesMatrix, localSearchSol, nTravelers, printSol)


def LocalSearchInterGrasp(distancesMatrix, nCities, nTravelers, randomSolution, desiredIterations, printSol):
    for i in range(nTravelers):
        randomSolution[i].pop(-1)
        randomSolution[i].pop(0)
    iterations = 0
    localSearchSol = randomSolution
    while iterations < desiredIterations:
        localSearchSol = inter_route_shift(distancesMatrix, nTravelers, localSearchSol, False)
        iterations += 1

    return CalculateObjetiveFunction(distancesMatrix, localSearchSol, nTravelers, printSol), localSearchSol


def calculatedImprove(distancesMatrix, solutionToBeCalculated):
    for i in range(len(solutionToBeCalculated)):
        for y in range(len(solutionToBeCalculated[i])):
            print(y)


def intra_route_shift(distancesMatrix, nCities, nTravelers, initialSolution, printImprove):
    bestTotalCost = CalculateObjetiveFunction(distancesMatrix, initialSolution, nTravelers, False)
    for i in range(nTravelers):
        for x in range(len(initialSolution[i]) - 1):
            for y in range(len(initialSolution[i]) - 1):
                initialSolutionAux = deepcopy(initialSolution)
                initialSolution[i].insert(y, initialSolution[i].pop(x))

                newTotalCost = CalculateObjetiveFunction(distancesMatrix, initialSolution, nTravelers, False)
                if newTotalCost < bestTotalCost:
                    if printImprove:
                        print("Improved by intra_route_shift | new total cost (", newTotalCost, ") old total cost (",
                              bestTotalCost, ")")
                        ShowRoutes(nTravelers, initialSolution)
                    bestTotalCost = newTotalCost
                    continue
                else:
                    initialSolution = deepcopy(initialSolutionAux)
    return initialSolution


# def intra_route_shift_two(distancesMatrix, nCities, nTravalers, initialSolution):
#     print("intra_route_shift")
#     bestTotalCost = CalculateObjetiveFunction(distancesMatrix, initialSolution, nTravalers)
#     for i in range(nTravalers):
#         for x in range(len(initialSolution[i])-1):
#             for y in range(len(initialSolution[i])-1):
#                 auxY = initialSolution[i][y]
#                 auxX = initialSolution[i][x]
#                 initialSolution[i][y] = auxX
#                 initialSolution[i][x] = auxY
#                 newTotalCost = CalculateObjetiveFunction(distancesMatrix, initialSolution, nTravalers)
#                 if newTotalCost < bestTotalCost:
#                     bestTotalCost = newTotalCost
#                     continue
#                 else:
#                     initialSolution[i][y] = auxY
#                     initialSolution[i][x] = auxX
#     return initialSolution

def inter_route_shift(distancesMatrix, nTravelers, newIntinalSol, printImprove):
    bestTotalCost = CalculateObjetiveFunction(distancesMatrix, newIntinalSol, nTravelers, False)
    for i in range(nTravelers):
        for x in range(len(newIntinalSol[i]) - 1):
            for j in range(nTravelers):
                iterations = 0
                for y in range(len(newIntinalSol[j])):
                    index = y - iterations
                    iterations += 1
                    newIntinalSolAux = deepcopy(newIntinalSol)
                    newIntinalSol[i].insert(x, newIntinalSol[j].pop(index))
                    newTotalCost = CalculateObjetiveFunction(distancesMatrix, newIntinalSol, nTravelers, False)
                    if newTotalCost < bestTotalCost and len(newIntinalSol[j]) >= 2:
                        if printImprove:
                            print("Improved by inter_route_shift | new total cost (", newTotalCost,
                                  ") old total cost (",
                                  bestTotalCost, ")")
                            ShowRoutes(nTravelers, newIntinalSol)
                        bestTotalCost = newTotalCost
                        continue
                    else:
                        newIntinalSol = deepcopy(newIntinalSolAux)
    return newIntinalSol
