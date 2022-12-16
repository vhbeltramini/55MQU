import sys
'''
command example:
# python main.py mtsp51_3 lsm h12 -- local
garantir que todos m voltem para o nodo 1
garantir que todos os nodos sejam visitados
garantir que todos os nodos sejam saidos
'''
from instances import create_instance
from heuristics import Heurisitica1, Heuristica12
from heuristics2 import Heurisitica2, Heuristica22
from local_search import LocalSearchInterIntra, LocalSearchInter, LocalSearchIntra
from grasp import GraspSemiGredyConstructionWithIntraLocalSearch, GraspSemiGredyConstructionWithInterLocalSearch, \
    GraspSemiGredyTwoConstructionWithIntraLocalSearch, GraspSemiGredyTwoConstructionWithInterLocalSearch

def main():
    instance = sys.argv[1]
    solveMethod = sys.argv[2]
    initialSolutionArg = sys.argv[3]
    calculatedMatrix, nCities, nTravelers = create_instance(instance)

    match (solveMethod):
        case "h1":
            Heurisitica1(calculatedMatrix, nCities, nTravelers, True)
        case "h12":
            Heuristica12(calculatedMatrix, nCities, nTravelers, True)
        case "h2":
            Heurisitica2(calculatedMatrix, nCities, nTravelers, True)
        case "h22":
            Heuristica22(calculatedMatrix, nCities, nTravelers, True)
        case "lsii":
            initialSol = getInitialSolutionFromArg(initialSolutionArg, calculatedMatrix, nCities, nTravelers)
            LocalSearchInterIntra(calculatedMatrix, nCities, nTravelers, initialSol, 30)
        case "lsia":
            initialSol = getInitialSolutionFromArg(initialSolutionArg, calculatedMatrix, nCities, nTravelers)
            LocalSearchIntra(calculatedMatrix, nCities, nTravelers, initialSol, 30, True)
        case "lsie":
            initialSol = getInitialSolutionFromArg(initialSolutionArg, calculatedMatrix, nCities, nTravelers)
            LocalSearchInter(calculatedMatrix, nCities, nTravelers, initialSol, 20, True)
        case "grasp1":
            GraspSemiGredyConstructionWithIntraLocalSearch(calculatedMatrix, nCities, nTravelers)
        case "grasp2":
            GraspSemiGredyConstructionWithInterLocalSearch(calculatedMatrix, nCities, nTravelers)
        case "grasp3":
            GraspSemiGredyTwoConstructionWithIntraLocalSearch(calculatedMatrix, nCities, nTravelers)
        case "grasp4":
            GraspSemiGredyTwoConstructionWithInterLocalSearch(calculatedMatrix, nCities, nTravelers)


def getInitialSolutionFromArg(arg, calculatedMatrix, nCities, nTravelers):
    match arg:
        case "h1":
            return Heurisitica1(calculatedMatrix, nCities, nTravelers, False)
        case "h12":
            return Heuristica12(calculatedMatrix, nCities, nTravelers, False)
        case "h2":
            return Heurisitica2(calculatedMatrix, nCities, nTravelers, False)
        case "h22":
            return Heuristica22(calculatedMatrix, nCities, nTravelers, False)
        case _:
            print("Please informe an heuristic to be the intial solution")
            exit()



main()

