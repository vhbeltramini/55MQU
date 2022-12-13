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
    CalculateObjetiveFunction(distancesMatrix, solution, nTravelerSalesman)


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

    print(result)
    print()
    print("Custo total")
    totalCost = 0
    for i in range(len(result)):
        totalCost = totalCost + result[i]
    print(totalCost)
    return result, totalCost
