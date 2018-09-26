import pandas as pd
from YIDT_app import car_class as car

def getCars():
    carlist = pd.read_csv("YIDT_app\data\Billista.csv", sep=';')
    Cars = []
    for i in range(len(carlist)):

        currCar = car.Car(
        carlist["Brand"][i],
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

    return Cars
