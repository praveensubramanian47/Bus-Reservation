CREATE DATABASE bus_reservation;
USE bus_reservation;

CREATE TABLE bus_info(bus_no INT, bus_capacity INT, bus_root VARCHAR(50));
INSERT INTO bus_info VALUES (5681, 3, "chennai"),
(5682, 45, "banglore"), (5683, 45, "pune");

CREATE TABLE booking_details( pass_name VARCHAR(50), pass_no DOUBLE,pass_date DATE, place LONGTEXT);
INSERT INTO booking_details VALUES ("PK", 8122360890, '2023-10-12', "chennai");