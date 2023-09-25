# Class that defines the nut
class My_Hut:

    # Constructor or init method. This is run automatically when an object or specific place in the world gets created.
    def __init__(self, name):               # Self is used to reference your own objects. E.g. name
        self.name = name                    # The class itself name is assigned name send to the init function.
        self.items = []                      # define a couple of variables.
        self.huts = []
        self.description = ""
        self.inspect = ""

    # Add a description of the hut.
    def setdescription(self, description):  # A method. A function that is within a class.
        self.description = description

    # add an item to the hut
    def additem(self, item):
        self.items.append(item)

    # When we have openings in the hut we are assigning them to this.
    def addhut(self, hut):
        self.huts.append(hut)

    # Set a description if we are looking close at the hut
    def setinspect(self, inspect):
        self.inspect = inspect

    # Lets define a function that creates and returns a description of the hut
    def tostring(self):
        # Description of the hut
        response = ""
        response = self.description + "\n"
        response = response + "Items you see scattered around the hut: \n"

        # Add all the items
        for item in self.items:
            response = response + item.getname() + ": " + item.getdescription() + "\n"
        response = response + "\n"

        # Print all the huts
        response = response + "There are more huts out there!"
        # Format and print out all the directions that are available in the hut.
        directions = ""
        for direction in self.huts:
            directions = directions + ", " + direction
        directions = directions[2:]
        response = response + directions + "\n\n"

        return response

    # print out detailed information about hut.
    def lookcloser(self):
        print(self.inspect)