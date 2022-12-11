import sys
from math import sqrt


def create_instance(instance_name):
    dataWithCitys = {}
    names = set([])
    lines = []
    coordinates = []
    calculatedDistances = {}
    cityCoordenations = []

    with open("../instances-data/" + instance_name + ".txt") as file:
        index = 0
        for line in file.readlines():
            if index < 2:
                index += 1
                continue

            city, posX, posY = line.strip().split('\t')
            dataWithCitys[(int(posX), int(posY))] = int(city)
            cityCoordenations.append([(int(posX), int(posY))])

    totalCities = len(cityCoordenations)
    for x1 in range(totalCities):
        for y1 in range(totalCities):
            try:
                if dataWithCitys[(x1, y1)] is not None:
                    # Distance = sqrt((x1 - x2)^2 + (y1 - y2)^2)
                    calculatedDistances[x1, y1] = 1
                else:
                    calculatedDistances[x1, y1] = 0
            except (KeyError, IndexError):
                calculatedDistances[x1, y1] = 0
                continue

    print(dataWithCitys)
    print(dataWithCitys[(37, 52)])
    print("----------------------")
    print(cityCoordenations)
    print(calculatedDistances[(1, 1)])
    print(calculatedDistances)
    return cityCoordenations, dataWithCitys, calculatedDistances


create_instance("mtsp51_3")
# create_instance(sys.argv[1])



# testesteste


# coordinates.append((posX, posY))
# pos_array = [int(posX)][int(posY)]  # declaration of 2D array
# citys.append(pos_array);