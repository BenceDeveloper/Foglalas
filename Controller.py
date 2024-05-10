from Foglalás import Reservation
from datetime import date
class Controller:
    def __init__(self,model):
        self.Model = model
        self.Reservation(1,date(2024,5,15),"Hotel California")
        self.Reservation(1,date(2025,3,20),"Hotel California")
        self.Reservation(2,date(2024,5,17),"Hotel California")
        self.Reservation(2,date(2024,6,30),"Hotel California")
        self.Reservation(3,date(2024,5,25),"Hotel California")
    def Reservation(self,RoomNumber, Date, HotelName):
        if Date > date.today():
            szoba = self.FindRoom(RoomNumber,HotelName)
            if szoba:
                if not self.check_duplicate_foglalas(szoba,Date):
                    self.Model.Reservation.append(Reservation(szoba, Date, HotelName))
                    print("A foglalás sikeres volt!")
                    print(f"A szoba ára: {szoba.Price}")
                else:
                    print("Erre a napra már van foglalás ezen a szoba számon!")
            else:
                print("Rossz szoba számot adott meg!")
        else:
            print("nem megfelelő dátum vissza menőleges foglalás nem lehetséges!")


    def check_duplicate_foglalas(self, Rooms, Date):
        for reserv in self.Model.Reservation:
            if reserv.Room == Rooms and reserv.Date == Date:
                return True
        return False
    def GetHotel(self,HotelName):
        for Hotel in self.Model._Hotels:
            if Hotel.Name == HotelName:
                return Hotel
        return None
    def FindRoom(self,RoomNumber,HotelName):
        Hotel = self.GetHotel(HotelName)
        if Hotel != None:
            for Rooms in Hotel.Rooms:
                if Rooms.Number == RoomNumber:
                    return Rooms
        else:
            print("Nincs ilyen nevű hotelünk!!")
    def ReservationListing(self):
        for reservations in self.Model.Reservation:
            print(f"Szálloda: {reservations._Hotelname} Szoba: {reservations._Room.Number}, Dátum: {reservations._Date}")
    def Resignation(self,RoomNumber, Date,HotelName):
        Hotel = self.GetHotel(HotelName)
        for Reserv in self.Model.Reservation:
            if Reserv._Room.Number == RoomNumber and Reserv._Date == Date:
                self.Model.Reservation.remove(Reserv)
                print("A lemondás Sikeres volt!")
                return
        print("A lemondás Sikertelen volt nincs ilyen (Hotelre,dátumra,szobaszámra) szoló foglalás!")
    def ListHotels(self):
        for i in self.Model._Hotels:
            print(i.Name)
    def RoomsAvailable(self,HotelName):
        SortedList = []
        for i in self.Model._Hotels:
            if i.Name == HotelName:
                for a in i.Rooms:
                    if a.isavailable == True:
                        SortedList.append(a)
        SortedList.sort(key=lambda x: x.Number)
        for b in SortedList:
            print(f"{b.Number}. {b.Price}Ft")
            SortedList = []
