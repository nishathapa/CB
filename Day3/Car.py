#class Car:

#     def start(self):
#         print(sound)
#
# my_car = Car()
#
# my_car.name = (" bhjb")def __init__(self, name):
#      self.name = name
# # my_car.start = ("jhukj")
# slogan = none

##                                                                                                                                                                                                                                                                                                                                          # # my_car.start = ("jhukj")

                                                                                                                                                                          # # my_car.start = ("jhukj")

class Car:

    population = 0

    slogan = "Default slogan"

    def __init__(self, name = "deafault name"):
        self.name = name
        Car.population += 1


    def sound(self, data):
        print(data)

    def set_slogan(self, data ):
        Car.slogan = data

c = Car()

c.sound("Peeeee")


