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


def build(instances, attributes, classes, value, default, prev_attr):
    node = Node()
    node.value = value
    if not instances:
        node.name = default
        # print_tree(node, counter)
        return node
    elif not attributes:
        lst = count(instances, classes)
        for i in range(lst.__len__()):
            if lst[i][1] == max([sublist[-1] for sublist in lst]):
                node.name = lst[i][0]
        # print_tree(node, counter)
        return node
    elif instances.__len__() == max([sublist[-1] for sublist in count(instances, classes)]):
        lst = count(instances, classes)
        for i in range(lst.__len__()):
            if lst[i][1] == max([sublist[-1] for sublist in lst]):
                node.name = lst[i][0]
        # print_tree(node, counter)
        return node
    else:
        try:
            best_attribute = choose_attr(instances, attributes, classes)
            while attributes[best_attribute][0] in prev_attr:
                if len(attributes) > 1:
                    attributes.pop(best_attribute)
                    best_attribute = choose_attr(instances, attributes, classes)
                else:
                    lst = count(instances, classes)
                    for i in range(lst.__len__()):
                        if lst[i][1] == max([sublist[-1] for sublist in lst]):
                            node.name = lst[i][0]
                    return node
            prev_attr.append(attributes[best_attribute][0])
            new_attributes = attributes.copy()
        except IndexError:
            print(best_attribute, len(attributes))

        branches = []
        for a in range(attributes[best_attribute][1].__len__()):
            new_instances = [inst for inst in instances if
                             inst.__getattribute__(attributes[best_attribute][0]) == a]
            lst = count(instances, classes)
            for i in range(lst.__len__()):
                if lst[i][1] == max([sublist[-1] for sublist in lst]):
                    default = lst[i][0]
            new_branch = build(new_instances, new_attributes, classes, a, default, prev_attr)
            branches.append(new_branch)

        node.value = value
        node.name = attributes[best_attribute][0]
        node.instances = instances
        node.branches = branches
        return node
