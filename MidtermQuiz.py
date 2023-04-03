givenmeters = int(input("Meters?: "))
class DistanceConversion:
    def __init__(self,meters):
        self.__meters = givenmeters

    def centimeter(self):
        print("Centimeters: ", givenmeters*100)

    def kilometer(self):
        print("Kilometers: ", givenmeters/1000)

    def inches(self):
        print("inches: ", givenmeters*39.37)

centi = DistanceConversion(givenmeters)
centi.centimeter()
kilo = DistanceConversion(givenmeters)
kilo.kilometer()
inch = DistanceConversion(givenmeters)
inch.inches()