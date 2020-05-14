def assign_type(x):  # switch case function to assign string as animal_type
    return {
        '1': 'mammal',
        '2': 'bird',
        '3': 'reptile',
        '4': 'fish',
        '5': 'amphibian',
        '6': 'insect',
        '7': 'invertebrate'
    }[x]


class Animal:

    def __init__(self, row):
        self.animal_name = row[0]
        self.hair = int(row[1])
        self.feathers = int(row[2])
        self.eggs = int(row[3])
        self.milk = int(row[4])
        self.airborne = int(row[5])
        self.aquatic = int(row[6])
        self.predator = int(row[7])
        self.toothed = int(row[8])
        self.backbone = int(row[9])
        self.breathes = int(row[10])
        self.venomous = int(row[11])
        self.fins = int(row[12])
        self.legs = int(row[13])
        self.tail = int(row[14])
        self.domestic = int(row[15])
        self.catsize = int(row[16])
        self.animal_type = assign_type(row[17])
