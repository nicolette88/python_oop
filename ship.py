# Házi feladat: Spaceship
class SpaceShip(object):
    def __init__(self):
        self._fuel = 400
        self._passengers = ['John', 'Steve', 'Sam', 'Danielle']
        self._shields = True
        self._speedometer = 0

    def list_passengers(self):
        for element in self._passengers:
            print("Passenger: " + element)

    def add_passenger(self, new_passenger):
        self._passengers.append(new_passenger)
        print(new_passenger + " was added to the ship")

    def travel(self, distance):
        print("trying to travel: " + str(distance))
        if (self._fuel == 0):
            print("can't go further, tank is empty")
        else:
            tempFuel = self._fuel - (distance / 2)
            if (tempFuel < 0):
                newDistance = distance - (tempFuel * -2)
                self._fuel = 0
                self._speedometer = newDistance + self._speedometer
                print("can only travel: " + str(int(newDistance)))
            else:
                self._fuel = tempFuel
                self._speedometer = distance + self._speedometer

            if (self._fuel < 30 and self._shields == True):
                self._shields = False
                print("fuel is low, turning off shields...")

            print("the SpaceShip is at: " + str(int(self._speedometer)))
            print("the spaceship has: " + str(int(self._fuel)) + ' fuel')


# main
mySpaceShip = SpaceShip()

mySpaceShip.list_passengers()
mySpaceShip.add_passenger('Lindsay')
mySpaceShip.list_passengers()
mySpaceShip.travel(750)
mySpaceShip.travel(200)
mySpaceShip.travel(100)
