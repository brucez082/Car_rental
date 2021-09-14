#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      brucez.19233
#
# Created:     09/09/2021
# Copyright:   (c) brucez.19233 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

def unique_code_generator(first_name, last_name):
    a = first_name[0:2]
    b = last_name
    random_number = random.randint(100000, 999999)
    user_name = str(random_number) + a + b
    return user_name.upper()

def force_name(message, lower, upper):
    while True:
        name = str(input(message))
        if len(name) >= lower and len(name) <= upper and name.isalpha():
            break
        else:
            print("Please enter in a valid name, e.g the number of letters has to be between {} - {}".format(lower, upper))
    return name

def force_number(message, lower, upper):
    while True:
        try:
            number = int(input(message))
            if carnumber >= lower and carnumber <= upper:
                break
            else:
                print("Please enter a number between {} - {}".format(lower, upper))
        except:
            print("Please enter a number instead of a piece of string")
    return number

def car_prices(cars_list):
    print("These are the prices for our cars....")
    count = 0
    while count < len(cars_list):
        print(int(count/2+1), " ", cars_list[count], "$", cars_list[count + 1])
        count += 2
    print("*" * 20)

def car_booking(cars_list):
    confirmed_booking = []
    car_number = force_number("Which number car would you like to book? (1 - 9))",1,9)
    car_number = car_number * 2 -2
    car_days = force_number("How many days would you like the {} for?".format(cars_list[car_number]),1,30)
    first_name = force_name("Please enter your first name",2,30)
    last_name = force_name("Please enter your last name",2,30)
    booking_code = unique_code_generator(first_name, last_name)
    car_cost = cars_list[car_number + 1] * car_days #calculates the cost of the booking

    confirmed_booking.append("Vehicles: {}".format(cars_list[car_number])) #this adds all of the variables to confirm booking list
    confirmed_booking.append("${}".format(cars_list[car_number + 1]))
    confirmed_booking.append("Daily car price: {}".format(car_cost))
    confirmed_booking.append("First name: {}".format(first_name))
    confirmed_booking.append("Last name: {}".format(last_name))
    confirmed_booking.append("Your unique code: {}".format(unique_code_generator))








    print("*** Confirmed Booking***")
    for item in confirmed_booking:
        print(item)
    print("*** End of confirmed booking***")

def main_menu():
    cars_list = ["Fiesta", 100, "Focus", 130, "Mondeo", 180, "Falcon", 230, "Territory", 280, "XR6 Ute", 250, "F150 Truck", 300, "Mustang", 350, "Van", 230]
    print("Welcome to Speedy Car Rentals")
    while True:
        print("Please select from one of the following options: ")
        print("Press 0 to exit")
        print("Press 1 for the price list")
        print("Press 2 to make a booking")
        choice = force_number("Please enter your choice: \n 1 for prices \n 2 for a booking \n 0 to quit",0,2)
        if choice == 1:
            car_prices(cars_list)
        if choice == 2:
            car_booking(cars_list)
        if choice == 0:
            break
    print("PROGRAM ENDS******")

#Call the function
main_menu()
