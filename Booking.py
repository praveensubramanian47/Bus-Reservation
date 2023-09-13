import datetime
import Database
import BusInfo

class Booking:
    connect = Database.Database().DB_connection()
    pass_name = ""
    mobile_no = 0
    date = ""
    ori_date = datetime.date
    destination = ""

    def __init__(self):
        self.pass_name = input("Enter your Name:- ")
        self.mobile_no = input("Enter your Mobile Number:- ")
        self.date = input("Enter traveling (YYYY-MM-dd) date:- ")
        formate = '%Y-%m-%d'  # Using function strptime from module to convert date
        self.ori_date = datetime.datetime.strptime(self.date, formate)
        self.destination = input("Enter your Destination:-")

    def Booking(self):
        try:
            sql = "insert into booking_details values (%s, %s, %s, %s)"
            val = (self.pass_name, self.mobile_no, self.date, self.destination)
            curser = self.connect.cursor()
            capacity = BusInfo.BusInfo().get_bus_capacity(self.destination)
            count = Booking.Booking_con(destiny=self.destination, dt=self.ori_date, self=self)
            if count < capacity:
                curser.execute(sql, val)
                self.connect.commit()
                print(f"YOUR BOOKING CONFIRM, HAPPY JOURNEY!.✨")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            else:
                print("SORRY😞, BOOKING FULL. TRY OTHER DATE")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        except Exception as e:
            print(e)

    def Booking_con(self, destiny, dt):
        sql = "select count(pass_name) from booking_details where place = %s and pass_date = %s;"
        val = (destiny, dt.date())
        curser = self.connect.cursor()
        curser.execute(sql, val)
        re = curser.fetchone()
        return re[0]

