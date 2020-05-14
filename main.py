import csv
import math
from operator import attrgetter

from animal import Animal
from node import Node


def read_instances(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        objects = [Animal(row) for row in reader]
    return objects


def build_tree(node, tree):
    if not node.branches:
        tree.append(node)
        return tree
    tree.append(node)
    for n in range(len(node.branches)):
        if node.branches:
            build_tree(node.branches[n], tree)
    return tree


def classify(tree, animal):
    in_nodes = []
    for t in tree:
        if animal in t.instances:
            in_nodes.append(t)
    chosen_node = max(in_nodes, key=attrgetter('tree_lvl'))
    value = animal.__getattribute__(chosen_node.name)
    for br in chosen_node.branches:
        if br.value == value:
            leaf = br.name
    print(animal.animal_name + " is " + animal.animal_type + " and is classified as " + leaf)


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
                  ["animal_type", ["mammal", "bird", "reptile", "fish", "amphibian", "insect", "invertebrate"]]]
    classes = attributes[16][1]
    attributes.pop(16)
    instances = read_instances("zoo.csv")
    node = Node()
    root_node = node.build(instances, attributes, classes, None, "mammal", [])
    # root_node.print_tree(root_node, 0, '')
    tree = build_tree(root_node, [])
    classify(tree, instances[61])
    # for u in tree:
    #     print(u.name)


if __name__ == "__main__":
    main()
