import mysql.connector

class Database:

    def DB_connection(self):
        try:
            host = "localhost"
            user = "root"
            passwd = "ASdf12!@"
            database = "bus_reservation"
            db = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)
            return db
        except mysql.connector.Error as error:
            print(f"failed database {error}")


"""
str_date = '2023-05-23'
format = "%Y-%m-%d"
date = datetime.datetime.strptime(str_date, format)
print(date.date(), type(date))
"""
