import os
import time

def dictionary_Package(Name_package : str, packet_number : int):
    try:
        dict_Package = {
            "country_name" : {1 : "Portugal", 2 : "Bulgarian", 3 : "Poland", 4 : "Monaco", 5 : "Spain"},
            "price_Package" : {"Portugal" : 50000, "Bulgarian" : 45000, "Poland" : 46000, "Monaco" : 51000, "Spain" : 55000},
            "Room price"  : {"Portugal" : 2000, "Bulgarian" : 1500, "Poland" : 1200, "Monaco" : 1600, "Spain" : 2100}
        }
        return dict_Package[Name_package][packet_number]
    except (KeyError,ValueError,ValueError):
        return "error".upper()

def input_receipt(*prefix) -> str:
    print("============== Total packet ==============")
    print(f"{prefix[1]} packet (packet number is {prefix[0]})")
    print(f"Total packet price: {prefix[2]}")
    if prefix[3] > 0:
        print(f"Rent car for {prefix[3]} day")
        print(f"Total rent car price: {prefix[4]}")
    if prefix[6] > 0:
        print(f"More rent {prefix[5]} room for {prefix[6]} day")
        print(f"Total rent room : {prefix[7]}")
    print(f"Total price: {prefix[2] + prefix[4] + prefix[7]} baht.")
    print("===========================================")

# packet_input, people_input, summation_packet, rent_day, price_car, many_room, many_day, price_room
print("--------------Tour packet--------------")
print("""1.Portugal  packet 50,000 baht.
2.Bulgarian packet 45,000 baht.
3.Poland    packet 46,000 baht.
4.Monaco    packet 51,000 baht. 
5.Spain     packet 55,000 baht.""")
print("---------------------------------------\n")
try:
    packet_input = input("Choose your packet number: ")
    packet_number = dictionary_Package(Name_package="country_name", packet_number=int(packet_input))
    if packet_number == "ERROR":
        print("Invalid Package")
    else:
        people_input = int(input("How many people are go: "))
        price_packet = dictionary_Package(Name_package="price_Package",packet_number=packet_number)
        summation_packet = price_packet * people_input
        print("Want to rent a car?\n2000/1day")
        Rent_car = input("Y = yes , N = no: ").upper()
        if Rent_car == "Y":
            rent_day = int(input("How many day you want to rent?: "))
            price_car = 2000 * rent_day
        else:
            rent_day = price_car = 0
        price_room = dictionary_Package(Name_package="Room price",packet_number=packet_number)
        print(f"Do you want more room?\nRoom price {price_room}/1day")
        room_day = input("Y = yes , N = no: ").upper()
        if room_day == "Y":
            many_room = int(input("How many room: "))
            many_day = int(input("How many day: "))
            price_room *= many_room * many_day
        else:
            many_room = many_day = price_room = 0
        os.system('cls'); time.sleep(1.5)
        input_receipt(packet_input, people_input, summation_packet, rent_day, price_car, many_room, many_day, price_room)
except (ValueError, KeyboardInterrupt):
    print("error".upper())