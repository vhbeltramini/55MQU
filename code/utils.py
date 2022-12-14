def ShowResult(distancesMatrix, vertices_Faltantes, vertices_percoridos, solution, nTravelerSalesman):
    print()
    print(vertices_Faltantes)
    print()
    print(vertices_percoridos)
    print()
    print()
    print("Representação das rotas")
    for i in range(nTravelerSalesman):
        print(solution[i])
    print()
    print("Representação de soluções")
    CalculateObjetiveFunctionWithPrint(distancesMatrix, solution, nTravelerSalesman, True)


def CalculateObjetiveFunctionWithPrint(distancesMatrix, solution, nTravelerSalesman, showTotalCost):
    result = []

    for i in range(nTravelerSalesman):
        line = 0
        result.append(line)

    for i in range(nTravelerSalesman):
        for y in range(len(solution[i])):
            if y == (len(solution[i]) - 1):
                continue
            result[i] = round(result[i] + distancesMatrix[(solution[i][y], solution[i][y + 1])], 2)

    print(result)
    print()
    totalCost = 0
    for i in range(len(result)):
        totalCost = totalCost + result[i]
    print(totalCost)

    if showTotalCost:
        print("Custo total")
        print(totalCost)

    return totalCost


def CalculateObjetiveFunction(distancesMatrix, solution, nTravelerSalesman):
    result = []

    for i in range(nTravelerSalesman):
        line = 0
        result.append(line)

    for i in range(nTravelerSalesman):
        for y in range(len(solution[i])):
            if y == (len(solution[i]) - 1):
                continue
            result[i] = round(result[i] + distancesMatrix[(solution[i][y], solution[i][y + 1])], 2)

    totalCost = 0
    for i in range(len(result)):
        totalCost = totalCost + result[i]
    return totalCost


def CalculateObjetiveFunctionWithPrintForLocalSearch(distancesMatrix, solution, nTravelerSalesman, showTotalCost):
    result = []

    for i in range(nTravelerSalesman):
        line = 0
        result.append(line)
        solution[i].append(1)
        solution[i].insert(0, 1)

    for i in range(nTravelerSalesman):
        for y in range(len(solution[i])):
            if y == (len(solution[i]) - 1):
                continue
            result[i] = round(result[i] + distancesMatrix[(solution[i][y], solution[i][y + 1])], 2)

    print(result)
    print()
    totalCost = 0
    for i in range(len(result)):
        totalCost = totalCost + result[i]
    print(totalCost)

    if showTotalCost:
        print("Custo total")
        print(totalCost)

    return totalCost