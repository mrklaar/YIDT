import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Django_YIDT.settings')

import django
django.setup()

from YIDT_app.models import Car, Owner
import pandas as pd
import math
from YIDT_app import car_class as car

carlist = pd.read_csv("YIDT_app\data\Billista.csv", sep=';')
Cars = []
for i in range(len(carlist)):
    currCar = car.Car(
    carlist["Make"][i],
    carlist["Model"][i],
    carlist["Owner"][i],
    carlist["Color"][i],
    carlist["Year"][i],
    carlist["Gear"][i],
    carlist["Weight"][i],
    carlist["Fuel"][i],
    carlist["Power"][i],
    carlist["Plate"][i],
    carlist["Img"][i],
    )
    Cars.append(currCar)

def populate():
    for car in Cars:
        ownr = Owner.objects.get_or_create(Name = car.Owner, Username ="-")[0]

        c = Car.objects.get_or_create(
        Make = car.Make,
        Model = car.Model,
        Owner = ownr,
        Color = car.Color,
        Year = int(car.Year),
        Gear = car.Gear,
        Weight = int(car.Weight),
        Fuel = car.Fuel,
        Power = int(car.Power),
        Plate = car.Plate,
        Img = car.Img,
        )[0]

if __name__ == '__main__':
    print ('Populating Script')
    populate()
    print('populating complete!')
