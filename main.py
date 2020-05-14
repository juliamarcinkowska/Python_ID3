import csv
import math
import random

from animal import Animal
from node import build


def read_instances(file):  # create list of Animal objects from csv file
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        objects = [Animal(row) for row in reader]
    return objects


def print_tree(node, counter, text):  # print tree with indentation (recursively) based on root node
    if not node.branches:  # leaves
        text += ' ' + node.name
        print(text)
        return
    print(text)
    for n in range(len(node.branches)):  # branches
        text = node.name + " = " + str(node.branches[n].value) + ':'
        if node.branches:
            print_tree(node.branches[n], counter + 1, text.rjust(counter * 2 + len(text)))


def classify(node, animal):  # recursive function that classifies animal based on nodes
    if node.branches:
        for b in node.branches:
            if b.value == animal.__getattribute__(node.name):
                return classify(b, animal)
    else:
        if node.name == animal.animal_type:
            return True
        else:
            print(animal.animal_name + " is " + animal.animal_type + " and is classified as " + node.name)
            return False


def main():
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
                  ["animal_type", ["mammal", "bird", "reptile", "fish", "amphibian", "insect", "invertebrate"]]]
    classes = attributes[16][1]
    attributes.pop(16)  # copy animal_type to classes and delete from attributes

    instances = read_instances("zoo.csv")
    root_node = build(instances, attributes, classes, None, "mammal", [])
    print_tree(root_node, 0, '')

    results = 0  # testing algorithm
    for i in range(10):
        success = 0
        random.shuffle(instances)
        test_instances = instances.copy()
        test_set = test_instances[:math.ceil(len(test_instances) / 10)]
        training_set = test_instances[math.ceil(len(test_instances) / 10):]
        new_root_node = build(training_set, attributes, classes, None, "mammal", [])
        for ts in test_set:
            if classify(new_root_node, ts):
                success += 1
        results += success / len(test_set)
    precision = results / 10
    print(precision)


if __name__ == "__main__":
    main()
