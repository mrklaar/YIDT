class Car():

    def __init__(self,make, model, owner, color, year, gear, weight, fuel, power, plate,img):
        self.Make = make
        self.Model = model
        self.Owner = owner
        self.Color = color
        self.Year = year
        self.Gear = gear
        self.Weight = weight
        self.Fuel = fuel
        self.Power = power
        self.Plate = plate
        self.Img = img

    def __str__(self):
        print(self.Make + " " + self.Model)
