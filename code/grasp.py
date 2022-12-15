from heuristics import Heurisitica12


def GraspSemiGredyConstructionWithIntraLocalSearch(calculatedMatrix, nCities, nTravelers):
    initialSol = Heurisitica12(calculatedMatrix, nCities, nTravelers)
    print()
