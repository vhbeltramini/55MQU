# Local search implementations to solve the multiple traveling salesman problem
'''
restrições:
garantir que todos m saiam do nodo 1
garantir que todos m voltem para o nodo 1
garantir que todos os nodos sejam visitados
garantir que todos os nodos sejam saidos
'''

def LocalSearchM(distancesMatrix, nCities, nTravalers, initialSolution):
    print("starting local search")
    calculatedCost(distancesMatrix, initialSolution)


def calculatedCost(distancesMatrix, solutionToBeCalculated):
# for solutionToBeCalculated in :


def showResultLocalSearhM(vertices_Faltantes, vertices_percoridos, solution):
    print("Local Search solution")
    print("vertices faltantes: " + vertices_Faltantes)
    print()
    print("vertices percoridos: " + vertices_percoridos)
    print(vertices_percoridos)
    print()
    print("solution: " + solution)
