from heuristics import Heuristica12
from heuristics2 import Heuristica22
from local_search import LocalSearchIntraGrasp, LocalSearchInterGrasp
from utils import CalculateObjetiveFunctionWithPrintForLocalSearch
from copy import deepcopy


def GraspSemiGredyConstructionWithIntraLocalSearch(calculatedMatrix, nCities, nTravelers):
    initialSol = Heuristica12(calculatedMatrix, nCities, nTravelers, False)
    initalCost, initialSol = LocalSearchIntraGrasp(calculatedMatrix, nCities, nTravelers, initialSol, 10, False)
    bestFounded = deepcopy(initialSol)
    print("initial best sol", bestFounded)
    print("initial best cost", initalCost)

    iterations = 0
    while iterations <= 20:
        newSol = Heuristica12(calculatedMatrix, nCities, nTravelers, False)
        newTotalCost, newSol = LocalSearchIntraGrasp(calculatedMatrix, nCities, nTravelers, newSol, 20, False)
        if initalCost > newTotalCost:
            initalCost = newTotalCost
            bestFounded = newSol
        iterations += 1
    print("Initial Solution")
    CalculateObjetiveFunctionWithPrintForLocalSearch(calculatedMatrix, initialSol, nTravelers, True)
    print()
    print("Final Solution")
    return CalculateObjetiveFunctionWithPrintForLocalSearch(calculatedMatrix, bestFounded, nTravelers, True)


def GraspSemiGredyConstructionWithInterLocalSearch(calculatedMatrix, nCities, nTravelers):
    initialSol = Heuristica12(calculatedMatrix, nCities, nTravelers, False)
    initalCost, initialSol = LocalSearchInterGrasp(calculatedMatrix, nCities, nTravelers, initialSol, 10, False)
    bestFounded = deepcopy(initialSol)
    print("initial best sol", bestFounded)
    print("initial best cost", initalCost)

    iterations = 0
    while iterations <= 20:
        newSol = Heuristica12(calculatedMatrix, nCities, nTravelers, False)
        newTotalCost, newSol = LocalSearchInterGrasp(calculatedMatrix, nCities, nTravelers, newSol, 20, False)
        if initalCost > newTotalCost:
            initalCost = newTotalCost
            bestFounded = newSol
        iterations += 1
    print("Initial Solution")
    CalculateObjetiveFunctionWithPrintForLocalSearch(calculatedMatrix, initialSol, nTravelers, True)
    print()
    print("Final Solution")
    return CalculateObjetiveFunctionWithPrintForLocalSearch(calculatedMatrix, bestFounded, nTravelers, True)


def GraspSemiGredyTwoConstructionWithIntraLocalSearch(calculatedMatrix, nCities, nTravelers):
    initialSol = Heuristica22(calculatedMatrix, nCities, nTravelers, False)
    initalCost, initialSol = LocalSearchIntraGrasp(calculatedMatrix, nCities, nTravelers, initialSol, 10, False)
    bestFounded = deepcopy(initialSol)
    print("initial best sol", bestFounded)
    print("initial best cost", initalCost)

    iterations = 0
    while iterations <= 20:
        newSol = Heuristica22(calculatedMatrix, nCities, nTravelers, False)
        newTotalCost, newSol = LocalSearchIntraGrasp(calculatedMatrix, nCities, nTravelers, newSol, 20, False)
        if initalCost > newTotalCost:
            initalCost = newTotalCost
            bestFounded = newSol
        iterations += 1
    print("Initial Solution")
    CalculateObjetiveFunctionWithPrintForLocalSearch(calculatedMatrix, initialSol, nTravelers, True)
    print()
    print("Final Solution")
    return CalculateObjetiveFunctionWithPrintForLocalSearch(calculatedMatrix, bestFounded, nTravelers, True)


def GraspSemiGredyTwoConstructionWithInterLocalSearch(calculatedMatrix, nCities, nTravelers):
    initialSol = Heuristica22(calculatedMatrix, nCities, nTravelers, False)
    initalCost, initialSol = LocalSearchInterGrasp(calculatedMatrix, nCities, nTravelers, initialSol, 10, False)
    bestFounded = deepcopy(initialSol)
    print("initial best sol", bestFounded)
    print("initial best cost", initalCost)

    iterations = 0
    while iterations <= 20:
        newSol = Heuristica22(calculatedMatrix, nCities, nTravelers, False)
        newTotalCost, newSol = LocalSearchInterGrasp(calculatedMatrix, nCities, nTravelers, newSol, 20, False)
        if initalCost > newTotalCost:
            initalCost = newTotalCost
            bestFounded = newSol
        iterations += 1
    print("Initial Solution")
    CalculateObjetiveFunctionWithPrintForLocalSearch(calculatedMatrix, initialSol, nTravelers, True)
    print()
    print("Final Solution")
    return CalculateObjetiveFunctionWithPrintForLocalSearch(calculatedMatrix, bestFounded, nTravelers, True)
