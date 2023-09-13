import BusInfo as busIn
import Booking as book

if __name__ == "__main__":
    print("~~~~~~~~~~~~~~~~~~~~~~~~~ WELCOME ~~~~~~~~~~~~~~~~~~~~~~~~~")
    while True:
        busIn.BusInfo().display_bus_info()
        check = input("1. for booking, 2. exit :- ")
        if check == '1':
            book.Booking().Booking()
        elif check == '2':
            print("THANKYOU FOR USING ME 😉")
            exit()
        else:
            print("You Entered wrong input, try again")