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
    calculatedDistances, totalCities, totalTravelingSalesman = create_instance(instance)

    match(solveMethod):
        case "heuristic1":
            Heurisitica1(calculatedDistances, totalCities, totalTravelingSalesman)
        case "heuristic12":
            Heurisitica12(calculatedDistances, totalCities, totalTravelingSalesman)
        case "heuristic2":
            Heurisitica2(calculatedDistances, totalCities, totalTravelingSalesman)
        #case "heuristic22":
        #    Heurisitica22(calculatedDistances, totalCities, totalTravelingSalesman)
        case "lsm":
            Heurisitica1(calculatedDistances, totalCities)
            #initialSol = Heurisitica1(calculatedDistances, totalCities)
            #LocalSearchM(calculatedDistances, totalCities, totalTravelingSalesman, initialSol)


main()
