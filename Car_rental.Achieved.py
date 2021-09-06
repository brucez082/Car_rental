#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bruce Zhang
#
# Created:     06/09/2021
# Copyright:   (c) Bruce Zhang 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def car_prices(cars_list):
    print("These are the prices for our cars....")
    count = 0
    while count < len(cars_list):
        print(int(count/2+1), " ", cars_list[count], "$", cars_list[count + 1])
        count += 2
    print("*" * 20)

def car_booking(cars_list):
    confirmed_booking = []
    car_number = int(input("Which number car would you like to book? (1 - 9)"))
    car_number = car_number * 2 -2
    car_days = int(input("How many days would you like the {} for?".format(cars_list[car_number])))
    first_name = str(input("Please enter your first name"))
    last_name = str(input("Please enter your last name"))
    car_cost = cars_list[car_number + 1] * car_days #calculates the cost of the booking

    confirmed_booking.append(cars_list[car_number]) #this adds all of the variables to confirm booking list
    confirmed_booking.append(cars_list[car_number + 1])
    confirmed_booking.append(car_cost)
    confirmed_booking.append(first_name)
    confirmed_booking.append(last_name)

    print("*** Confirmed Booking***")
    print("Car model: {}".format(confirmed_booking[0]))
    print("The daily hire cost of the {} is ${}".format(confirmed_booking[0], confirmed_booking[1]))
    print("The total hire cost will be ${}".format(confirmed_booking[2]))
    print("First name: {}".format(confirmed_booking[3]))
    print("Last name: {}".format(confirmed_booking[3]))
    print("*** End of the Confirmed Booking ***")

def main_menu():
    import time
    global cars_list
    cars_list = ["Fiesta", 100, "Focus", 130, "Mondeo", 180, "Falcon", 230, "Territory", 280, "XR6 Ute", 250, "F150 Truck", 300, "Mustang", 350, "Van", 230]
    print("Welcome to Speedy Car Rentals")
    choice = 99
    while choice != 0:
        print("Please select from one of the following options: ")
        print("Press 0 to exit")
        print("Press 1 for the price list")
        print("Press 2 to make a booking")
        choice = int(input("Please enter your choice: \n 1 for prices \n 2 for a booking \n 0 to quit"))
        if choice == 1:
            car_prices(cars_list)
        if choice == 2:
            car_booking(cars_list)
    print("PROGRAM ENDS******")

#Call the function
main_menu()