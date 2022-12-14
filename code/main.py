import sys

from heuristics import Heurisitica1
from heuristics import Heurisitica12
from heuristics2 import Heurisitica2
#from heuristics2 import Heurisitica22
from local_search import LocalSearchM
from instances import create_instance


def main():
    instance = sys.argv[1]
    solveMethod = sys.argv[2]
    calculatedMatrix, nCities, nTravelers = create_instance(instance)

    match(solveMethod):
        case "h1":
            Heurisitica1(calculatedMatrix, nCities, nTravelers)
        case "h2":
            Heurisitica12(calculatedMatrix, nCities, nTravelers)
        case "heuristic2":
            Heurisitica2(calculatedMatrix, nCities, nTravelers)
        #case "heuristic22":
        #    Heurisitica22(calculatedMatrix, nCities, nTravelers)
        case "lsm":
            initialSol = Heurisitica1(calculatedMatrix, nCities, nTravelers)
            LocalSearchM(calculatedMatrix, nCities, nTravelers, initialSol)


main()
