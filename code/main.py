import sys

from heuristics import Heurisitica1
from instances import create_instance


def main():
    instance = sys.argv[1]
    solveMethod = sys.argv[2]
    create_instance(instance)

    match(solveMethod):
        case "heuristic1":
            Heurisitica1(instance)


main()
