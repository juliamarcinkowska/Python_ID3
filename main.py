import csv
import math

from animal import Animal


def read_instances(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        objects = [Animal(row) for row in reader]
    return objects


def count(instances, classes):
    lst = []
    for c in classes:
        tmp = 0
        for i in instances:
            if i.animal_type == c:
                tmp += 1
        lst.append([c, tmp])
    # lst = [[instances.count(c) for number in c] for c in classes]
    return lst


def choose_attr(instances, attributes, classes):
    min_entropy = 100
    best_attr = -1
    for i in range(len(attributes)):  # for each attribute
        instance_sets = []
        total_entropy = 0
        for j in range(len(attributes[i][1])):  # for each attribute value
            # get instances with that attribute value
            insts = [inst for inst in instances if inst.__getattribute__(attributes[i][0]) == attributes[i][1][j]]
            counts = count(insts, classes)  # counts how many instances belong to each class
            entropy = 0
            size = len(insts)
            for c in counts:  # computes entropy for each subset
                if c[1] > 0:
                    entropy = entropy - c[1] / size * math.log2(c[1] / size)
            total_entropy = total_entropy + size / len(instances) * entropy
        # total attribute entropy
        if min_entropy > total_entropy:
            min_entropy = total_entropy
            best_attr = i
    return best_attr


def main():
    concept = "animal type"
    attributes = [["hair", [0, 1]],
                  ["feathers", [0, 1]],
                  ["eggs", [0, 1]],
                  ["milk", [0, 1]],
                  ["airborne", [0, 1]],
                  ["aquatic", [0, 1]],
                  ["predator", [0, 1]],
                  ["toothed", [0, 1]],
                  ["backbone", [0, 1]],
                  ["breathes", [0, 1]],
                  ["venomous", [0, 1]],
                  ["fins", [0, 1]],
                  ["legs", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]],
                  ["tail", [0, 1]],
                  ["domestic", [0, 1]],
                  ["catsize", [0, 1]],
                  ["class", ["mammal", "bird", "reptile", "fish", "amphibian", "insect", "invertebrate"]]]
    instances = read_instances("zoo.csv")
    choose_attr(instances, attributes, attributes[16][1])
    print(instances.__len__())
    # id3 = ID3(concept, instances, attributes)
    # id3.run()


if __name__ == "__main__":
    main()
