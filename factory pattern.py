class Apple:
    def display(self):
        print("Apple")


class Mango:
    def display(self):
        print("Mango")


class Orange:
    def display(self):
        print("Orange")


class FruitFactory:
    def get_fruit(self, fruit):
        if fruit == "apple":
            return Apple()
        elif fruit == "mango":
            return Mango()
        elif fruit == "orange":
            return Orange()
        else:
            print("Fruit not available")


factory = FruitFactory()

fruit1 = factory.get_fruit("apple")
fruit1.display()

fruit2 = factory.get_fruit("mango")
fruit2.display()

fruit3 = factory.get_fruit("orange")
fruit3.display()