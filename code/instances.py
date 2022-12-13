import sys
from math import sqrt


def create_instance(instance_name):
    dataWithCities = {}
    calculatedDistances = {}
    cityCoordenations = []
    totalTravelingSalesman = 0

    with open("../instances-data/" + instance_name + ".txt") as file:
        index = 0
        for line in file.readlines():
            if index < 2:
                if index == 0:
                    totalTravelingSalesman = line.strip().split(' ')[2]

                index += 1
                continue

            city, posX, posY = line.strip().split('\t')
            dataWithCities[(int(posX), int(posY))] = int(city)
            cityCoordenations.append([int(posX), int(posY)])

    totalCities = len(cityCoordenations)

    for i in range(totalCities):
        for j in range(totalCities):
            if i == j:
                calculatedDistances[i, j] = 0
            calculatedDistances[i, j] = round(sqrt((cityCoordenations[i][0] - cityCoordenations[j][0]) ** 2 + (cityCoordenations[i][1] - cityCoordenations[j][1]) ** 2), 2)


    # print(dataWithCitys)
    # print(dataWithCitys[(37, 52)])
    # print("----------------------")
    # # print(cityCoordenations[0].index(0))
    # # print(cityCoordenations[0][0])
    # print("----------------------")
    # print(cityCoordenations)
    # print(calculatedDistances[(1, 5)])
    print(len(calculatedDistances))
    return calculatedDistances, totalCities, totalTravelingSalesman


create_instance("mtsp51_3")
# create_instance(sys.argv[1])


# testesteste


# coordinates.append((posX, posY))
# pos_array = [int(posX)][int(posY)]  # declaration of 2D array
# citys.append(pos_array);
