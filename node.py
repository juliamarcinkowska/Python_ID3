import math


class Node:
    def __init__(self):
        self.value = ""
        self.name = ""
        self.instances = []
        self.branches = []
        self.tree_lvl = 0


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


def print_tree(node, counter, text):
    if not node.branches:
        text += ' ' + node.name
        print(text)
        return
    print(text)
    for n in range(len(node.branches)):
        text = node.name + " = " + str(node.branches[n].value) + ':'
        if node.branches:
            print_tree(node.branches[n], counter + 1, text.rjust(counter * 2 + len(text)))


def build(instances, attributes, classes, value, default, prev_attr, counter=0):
    node = Node()
    node.value = value
    node.tree_lvl = counter
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
        if prev_attr:
            attr = attributes.copy()
            attributes.clear()
            for i in range(len(attr)):
                if attr[i][0] not in prev_attr:
                    attributes.append(attr[i])
        best_attribute = choose_attr(instances, attributes, classes)
        prev_attr.append(attributes[best_attribute][0])
        new_attributes = attributes.copy()

        branches = []
        for a in range(attributes[best_attribute][1].__len__()):
            new_instances = [inst for inst in instances if
                             inst.__getattribute__(attributes[best_attribute][0]) == a]
            lst = count(instances, classes)
            for i in range(lst.__len__()):
                if lst[i][1] == max([sublist[-1] for sublist in lst]):
                    default = lst[i][0]
            new_branch = build(new_instances, new_attributes, classes, a, default, prev_attr, counter + 1)
            branches.append(new_branch)

        node.value = value
        node.name = attributes[best_attribute][0]
        node.instances = instances
        node.branches = branches
        return node
