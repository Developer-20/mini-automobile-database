#Ferrari GT2050, 10000HP, 4WD, 900KM/hr
#Mercedez MXX400, 8700HP, 4WD, 600KM/hr
#Bentley MLL120, 5000HP, Hind Drive, 420KM/hr
 
#Car class in python   
class Car:
    #attributes of the class Car
    def __init__(self,name_of_car,horse_power,number_of_wheels,distance):
        self.model = name_of_car
        self.power = horse_power
        self.wheels = number_of_wheels
        self.distance = distance

#objects that define the class Car
object1 = Car(name_of_car="Ferrari GT2050",horse_power="10000HP",number_of_wheels="4WD",distance="900KM/hr")
object2 = Car(name_of_car="Mercedez GT2050",horse_power="8700HP",number_of_wheels="4WD",distance="600KM/hr")
object3 = Car(name_of_car="Bentley MLL120",horse_power="5000HP",number_of_wheels="Hind Drive",distance="4200KM/hr")

#input statement that allows the client to find the car brand he/she is willing to buy
user_specification = input("Enter the name of the brand: \n")

#if statement to check if the client's input is Ferrari
if user_specification == "Ferrari":
    print(f""",
        CAR SPECIFICATION
        -------------------
        CAR NAME: {object1.model}
        CAR HORSE POWER: {object1.power}
        NUMBER OF WHEELS: {object1.wheels}
        DISTANCE OF THE VEHICLE: {object1.distance}
        """)

#elif statement to check if the client's input is Mercedez
elif user_specification == "Mercedez":
    print(f""",
        CAR SPECIFICATION
        -------------------
        CAR NAME: {object2.model}
        CAR HORSE POWER: {object2.power}
        NUMBER OF WHEELS: {object2.wheels}
        DISTANCE OF THE VEHICLE: {object2.distance}
        """)

#elif statement to check if the client's input is Bentley
elif user_specification == "Bentley":
    print(f"""
        CAR SPECIFICATION
        -------------------
        CAR NAME: {object3.model}
        CAR HORSE POWER: {object3.power}
        NUMBER OF WHEELS: {object3.wheels}
        DISTANCE OF THE VEHICLE: {object3.distance}
        """)

else:
    print("Sorry we don't have that car model")

input()