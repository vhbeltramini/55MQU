import sys

from heuristics import Heurisitica1
from local_search import LocalSearchM
from instances import create_instance


def main():
    instance = sys.argv[1]
    solveMethod = sys.argv[2]
    calculatedDistances, totalCities, totalTravelingSalesman = create_instance(instance)

    match(solveMethod):
        case "heuristic1":
            Heurisitica1(calculatedDistances, totalCities)
        case "lsm":
            initialSol = Heurisitica1(calculatedDistances, totalCities)
            LocalSearchM(calculatedDistances, totalCities, totalTravelingSalesman, initialSol)


main()
