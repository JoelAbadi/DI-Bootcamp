class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_list = self.get_animal_types()
        formatted_list = []

        for animal in animal_list:
            count = self.animals[animal]
            if count > 1:
                formatted_list.append(animal + "s")
            else:
                formatted_list.append(animal)

        if len(formatted_list) > 1:
            animal_str = ', '.join(formatted_list[:-1]) + " and " + formatted_list[-1]
        else:
            animal_str = formatted_list[0]

        return f"{self.name}'s farm has {animal_str}."


# Test the code
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print()
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
