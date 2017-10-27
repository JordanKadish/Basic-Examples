# Jordan Kadish
# 27/10/2017
# Testing inheritance: child class

from vehicles import Vehicle


class Car(Vehicle):  # stating the class we inherit from
    def __init__(self, wheels, seats, speed, windows, brand):
        Vehicle.__init__(self, wheels, seats, speed)
        self.windows = int(windows)
        self.brand = brand

    def __str__(self):
        toString = Vehicle.__str__(self)
        toString += '\nWindows: ' + str(self.windows) + '\nBrand: ' + \
            self.brand
        return toString


if __name__ == '__main__':
    use = input("use: wheels, seats, speed, windows, brand\n").strip().split()
    car = Car(use[0], use[1], use[2], use[3], use[4])
    print(car)
    car.move()
    print('accelerating car 10%, speed becomes ' + str(int(car.speed)))
    car.stop()
    print('stopping car, speed becomes ' + str(car.speed))
