from Model import Model
from Controller import Controller
import sys
import datetime
def main():
    model = Model()
    controller = Controller(model)
    Exit = False
    while(Exit!=True):
        UserInput = input("Szallodák listázása (0), Foglalás(1), Lemondás(2), Foglalásaim Listázása(3), Kilépés(4)")
        match UserInput:
            case "0":
                controller.ListHotels()
            case "1":
                Name = input("Kérem a szálloda nevét: ")
                Date = input("Foglalás  dátuma(YYYY-MM-DD): ")
                year, month, day = map(int, Date.split('-'))
                Date = datetime.date(year, month, day)
                RoomNumber = input("Kérem a szoba számot: ")
                controller.Reservation(int(RoomNumber),Date,Name)
            case "2":
                Name = input("Kérem a szálloda nevét: ")
                RoomNumber = input("Kérem a szoba számát: ")
                Date = input("Foglalás  dátuma(YYYY-MM-DD): ")
                year, month, day = map(int, Date.split('-'))
                Date = datetime.date(year, month, day)
                controller.Resignation(int(RoomNumber),Date,Name)
            case "3":
                controller.ReservationListing()
            case "4":
                sys.exit()


if __name__ == "__main__":
    main()

