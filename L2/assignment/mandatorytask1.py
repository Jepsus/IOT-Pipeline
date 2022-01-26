from abc import ABC, abstractmethod

if __name__== "__main__":
    print("Program started")

# Inheritance part (We have Sensor class as a parent, and after that we can create child classes like Tempsensor(Sensor) so we are using methods of parent class in child class.)
class Sensor(ABC):
    @abstractmethod
    def __init__(self,temperature):
        self.temperature = temperature
    def getTemp(self):
        print(self.temperature)

class TempSensor(Sensor):
    def __init__(self):
        super().__init__("The temperature in the room is 30 C")

class HumiditySensor(Sensor):
    def __init__(self):
        super().__init__("Humidity in the room is 50%")

class OxideSensor(Sensor):
    def __init__(self):
        super().__init__("The level of CO2 is 10%")
        

sens1 = TempSensor()
sens1.getTemp()
sens2 = HumiditySensor()
sens2.getTemp()
sens3 = OxideSensor()
sens3.getTemp()





#class instance from another class
class Sensor():
    def __init__(self,roomnumber):
        self._roomnumber = roomnumber
    def _getData(self):
        return 50
    def _location(self):
        return self._roomnumber

    
class Dashboard():
    def __init__(self,sensor):
        self._sensors = sensor
    def displayStatus(self):
        for sensor in self._sensors:
            print(f"location: {sensor._location()}, data: {sensor._getData()}")
            
mydash = Dashboard([
    Sensor("room number 2"),
    Sensor("room number 3"),
    Sensor("room number 10")
    ])
mydash.displayStatus()


        
        
    



