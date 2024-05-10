from Hotel import Hotel
from Foglalás import Reservation
class Model:
    def __init__(self):
        self._Hotels = []
        self._Reservation = []
        self._Hotels.append(Hotel("Hotel California", 3))
    @property
    def Reservation(self):
        return self._Reservation

    @property
    def Hotels(self):
        return self._Hotels

