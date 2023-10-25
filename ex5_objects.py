# Objects can be thought of as collections of data and functions
# You can make many unique versions, using different parameters

# In this example we have a Dog class that provides a template for making Dog objects.
# You can see that dogs have 3 parameters: colour, breed, and a bark sound

# When we make a new dog, we must give the object those parameters.
class Dog():
    # __init__ is the function that runs when a new object is created
    # it is responsible for doing any initial set up required to use the object
    # in this case we want the object to store the three parameters in itself
    # the "self" keyword refers to the object that is currently being used.

    # This storing is done by using self.<parameter name>
    # this is just a variable owned by the current object (self)
    def __init__(self, colour, breed, bark_sound):
        self.colour = colour
        self.breed = breed
        self.bark_sound = bark_sound

        print(f"Creating new {self.breed} with {self.colour} fur who goes \"{self.bark_sound}\".")

    # Objects can also have functions! 
    # These usually operate on the object's specific variables.
    # They can be called by using self.<function name> from another function inside the object 
    # or <object name>.<function name> when outside the object.  
    def bark(self):
        print(f"The {self.colour} {self.breed} fur who goes \"{self.bark_sound}\".")


# This is how you make a new object!
new_dog = Dog("black and brown", "border collie", "bork bork")

# This is how you call that new object's function
new_dog.bark()

# Make a note that multiple versions of the same object can exist
newer_dog = Dog("white and blue", "australian shephard", "woof woof")

new_dog.bark()
newer_dog.bark()