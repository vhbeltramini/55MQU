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
                    totalTravelingSalesman = int(line.strip().split(' ')[2])

                index += 1
                continue

            city, posX, posY = line.strip().split('\t')
            dataWithCities[(int(posX), int(posY))] = int(city)
            cityCoordenations.append([int(posX), int(posY)])

    totalCities = len(cityCoordenations)

    for i in (number + 1 for number in range(totalCities)):
        for j in (number + 1 for number in range(totalCities)):
            if i == j:
                calculatedDistances[i, j] = 0
            calculatedDistances[i, j] = round(sqrt((cityCoordenations[i-1][0] - cityCoordenations[j-1][0]) ** 2 + (cityCoordenations[i-1][1] - cityCoordenations[j-1][1]) ** 2), 2)

    # print(dataWithCitys)
    # print(dataWithCitys[(37, 52)])
    # print("----------------------")
    # # print(cityCoordenations[0].index(0))
    # # print(cityCoordenations[0][0])
    # print("----------------------")
    # print(cityCoordenations)
    # print(calculatedDistances[(1, 5)])
    # print(calculatedDistances)
    return calculatedDistances, totalCities, totalTravelingSalesman


create_instance("mtsp51_3")
# create_instance(sys.argv[1])


# testesteste


# coordinates.append((posX, posY))
# pos_array = [int(posX)][int(posY)]  # declaration of 2D array
# citys.append(pos_array);


def calculate_cost_shift(instance, route_one, route_two, point_one_index, point_two_index):
    intra = 0
    if route_one == route_two and point_one_index < point_two_index:  # Se for intrarota e o ponto i é menor que o j
        intra = 1  # Então adiciona 1 ao ponto, pois ao retirar da posição i, o vetor será rearranjado e j será j - 1

    i = route_one[point_one_index]['index']
    i_front = route_one[point_one_index + 1 if point_one_index + 1 < len(route_one) else 0]['index']
    i_back = route_one[point_one_index - 1]['index']
    j = route_two[point_two_index + intra if point_two_index + intra < len(route_two) else 0]['index']
    j_back = route_two[point_two_index - 1 + intra]['index']

    cost = (- instance.matrix[i_back][i]
            - instance.matrix[i][i_front]
            + instance.matrix[i_back][i_front]
            + instance.matrix[j_back][i]
            + instance.matrix[i][j]
            - instance.matrix[j_back][j])

    return round(cost, 2)