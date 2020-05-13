import math


class Node:
    def __init__(self):
        self.value = ""
        self.name = ""
        self.instances = []
        self.branches = []


def count(instances, classes):
    return [[c, sum(i.animal_type == c for i in instances)] for c in classes]


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


def build(instances, attributes, classes, default):
    if not instances:
        node = Node()
        node.name = default
        return node
    elif not attributes:
        node = Node()
        node.name = max([sublist[-1] for sublist in instances])
        return node
