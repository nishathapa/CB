class Car:
    def __init__(self, color = "white", slogan = "Default"):
        self.doors = 4
        self.seats = 4
        self.color = color
        self.slogan = slogan

    def start(self):
        print(' Im starting')


    def acc(self):
        print('Vroom, Vroom')


    def stop(self):
        print('Im stopping')


class Maruti(Car):
    def honk(self):
        print("peee")

    def start(self):
        print('new start')

    def __init__(self,abs = True,color = "white", slogan = "Default"):
        super().__init__(color,slogan)
        self.seats = 5
        self.abs = abs

    def start(self):
        super().start()
    print("Im Maruti")

first= Car()
print(first.color)
print(first.slogan)

second=Car("Red")
print(second.color)
print(second.slogan)

third= Car("red", "Maa")
print(third.color)
print(third.slogan)

# third.start()
# print(third.start())

fourth = Maruti(False, "pink")
fourth.start()
fourth.stop()
fourth.acc()
fourth.honk()
fourth.start()

print(fourth.seats)
print(fourth.color)
print(fourth.start())