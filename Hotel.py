from Rooms import Szoba
from Rooms import EgyAgyasSzoba
from Rooms import KetAgyasSzoba
import random
class Hotel:
    def __init__(self,Name,HowManyRoom):
        self._Name = Name
        self._Rooms = []
        self.HowManyRoom = HowManyRoom
        Count = 0
        Be = False
        while(self.HowManyRoom != Count):
            Number = random.randint(1, HowManyRoom)
            for i in self._Rooms:
                if i.Number == Number:
                    Be = True
                    break
                else:
                    Be = False
            if Be == False:
                self.AddRooms(Number,random.randint(0,1))
                Count += 1
    @property
    def Name(self):
        return self._Name
    @property
    def Rooms(self):
        return self._Rooms
    def AddRooms(self,Number,OneOrTwo = 0):
        if OneOrTwo == 0:
            self.Rooms.append(EgyAgyasSzoba(Number))
        if OneOrTwo == 1:
            self.Rooms.append(KetAgyasSzoba(Number))