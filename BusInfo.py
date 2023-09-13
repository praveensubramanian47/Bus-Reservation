import Database


class BusInfo:
    connect = Database.Database().DB_connection()
    __bus_no = 0
    __bus_capacity = 0
    __bus_endpoint = ""

    def get_bus_no(self):
        return self.__bus_no

    def set_bus_no(self, bus_no):
        self.__bus_no = bus_no

    def set_bus_capacity(self, bus_cap):
        self.__bus_capacity = bus_cap

    def get_bus_destination(self):
        return self.__bus_endpoint

    def set_bus_destination(self, dest):
        self.__bus_endpoint = dest

    def get_bus_capacity(self, destiny):
        try:
            sql = "select bus_capacity from bus_info where bus_root = %s"
            val = [destiny]
            curser = self.connect.cursor()
            curser.execute(sql, val)
            re = curser.fetchone()
            value = re[0]
            return value
        except Exception as e:
            print(e)

    def display_bus_info(self):
        try:
            sql = "select * from bus_info"
            cursor = self.connect.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                print("Bus Number:-", i[0])
                print("Bus Capacity:-", i[1])
                print("Bus Destination:-", i[2], "\n")
        except Exception as e:
            print(e)