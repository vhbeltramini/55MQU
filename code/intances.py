import sys


def create_instance(instance_name):
    lines = []
    with open("../instances-data/"+instance_name+".txt") as file:
        for item in file:
            lines.append(item)

    print(lines)
    # 


create_instance( sys(1))