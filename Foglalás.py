class Reservation:
    def __init__(self, Room, Date,HotelName):
        self._Hotelname = HotelName
        self._Room = Room
        self._Date = Date

    @property
    def Room(self):
        return self._Room

    @property
    def HotelName(self):
        return self._Hotelname

    @property
    def Date(self):
        return self._Date



