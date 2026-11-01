from abc import ABC, abstractmethod
from typing import  List

class AirTrafficControl(ABC): 
    @abstractmethod
    def register_plane(self):
        pass
    @abstractmethod
    def send_message(self):
            pass

class ControlTower(AirTrafficControl):
    def __init__(self):
         self.__airplanes:List[Airplane] = []

    def register_plane(self,new_airplane:'Airplane'):
        self.__airplanes.append(new_airplane)

    def send_message(self,msg:str,sender_plane:'Airplane'):
        

        for airplane in self.__airplanes:
            if airplane != sender_plane:
                airplane.receive_message(msg,sender_plane)   


class Airplane:
    def __init__(self,flight_number:str, tower:"ControlTower"):
        self.__flight_number = flight_number
        self.__tower = tower
        self.__tower.register_plane(self)  # entire object gone to register_airplane

    def send_message(self, msg:str):
        self.__tower.send_message(msg,self,)
    
    def getflightno(self)->str:
        return self.__flight_number
    
    def receive_message(self,msg:str,who_sent:"Airplane"):
         print(f"{self.__flight_number} got {msg} from {who_sent.getflightno()}")
              
    

control_tower = ControlTower()

air_india = Airplane("AIR-546", control_tower)
spicejet = Airplane ("SPICE-87171", control_tower)
indigo = Airplane ("IND-9911", control_tower)
air_india.send_message("I am getting on runway")