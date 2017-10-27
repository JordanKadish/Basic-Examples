# Jordan Kadish
# 27/10/2017
# Testing inheritance: parent class


class Vehicle:
    def __init__(self, wheels, seats, speed):
        self.wheels = int(wheels)
        self.seats = int(seats)
        self.speed = int(speed)

    def __str__(self):
        return 'Wheels: ' + str(self.wheels) + '\nSeats: ' + str(self.seats)

    def move(self):
        self.speed += self.speed / 10

    def stop(self):
        self.speed = 0
