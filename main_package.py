import os
import time
''' 
function dictionary_Package ทำการเก็บรายการ Package ทั้งหมด
country_name ใช้ในการเก็บชื่อประเทศในรูปแบบ dict ซ้อน dict
    - โดยการดึงค่าเพื่อดึงชื่อประเทศออกมาใช้งาน จะต้องอ้างอิงคีย์ที่เป็นตัวเลขเพื่อทำการดึงค่า ชื่อประเทศต่างๆออกมาใช้งาน
price_Package ใช้ในการเก็บราคาเที่ยวบินต่างประเทศ ในรูปแบบ dict ซ้อน dict
    - โดยการดึงค่าราคาเที่ยวบินออกมาใช้งาน จะต้องอ้างอิงคีย์ที่เป็นชื่อประเทศเพื่อทำการดึงค่า ราคาเที่ยวบินต่างประเทศออกมาใช้งาน
Room price ใช้ในการเก็บราคาค่าเช้าห้องในรูปแบบ dict ซ้อน dict
    - โดยการดึงค่าราคาค่าเช้าห้องออกมาใช้งาน จะต้องอ้างอิงคีย์ที่เป็นชื่อประเทศเพื่อทำการดึงค่า ราคาค่าเช้าห้องออกมาใช้งาน
'''
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

print("--------------Tour packet--------------")
print("""1.Portugal  packet 50,000 baht.
2.Bulgarian packet 45,000 baht.
3.Poland    packet 46,000 baht.
4.Monaco    packet 51,000 baht. 
5.Spain     packet 55,000 baht.""")
print("---------------------------------------\n")
try:
    packet_input = input("Choose your packet number: ") # รับค่าตามคีย์ของ packet ใน dictionary
    # ตัวแปร packet_number ใช้ในการเก็บค่าเพื่อนำมาเปรียบเทียบในเงื่อนไข
    # ถ้าหากผู้ใช้รับค่าเข้ามาแล้วไม่ตรงกับคีย์ที่แสดงอยู่ก็ให้ แสดง Invalid Package ออกมาผ่านทางจอภาพ
    packet_number = dictionary_Package(Name_package="country_name", packet_number=int(packet_input))
    if packet_number == "ERROR":
        print("Invalid Package")
    else:
        people_input = int(input("How many people are go: ")) # รับค่าจำนวนคนที่จะเที่ยวบิน
        # ถ้ารับค่าตรงกับคีย์ที่กำหนดให้ก็จะเอาชื่อประเทศมาทำการเข้า dict ซ้อน dict ที่ 2 ในตัวแปรที่ชื่อว่า price_packet
        # เพื่อทำการดึงราคาเที่ยวบินต่างประเทศออกมาคำนวณโดยเอาไปคูณด้วยจำนวนคนที่ จะไปเที่ยวบินแล้ว เก็บลงไปที่ตัวแปร summation_packet
        price_packet = dictionary_Package(Name_package="price_Package",packet_number=packet_number)
        summation_packet = price_packet * people_input
        print("Want to rent a car?\n2000/1day") # แสดงวันเช้ารถและราคาออกมา
        Rent_car = input("Y = yes , N = no: ").upper() # ถามผู้ใช้ว่าต้องการเช่ารถหรือไม่ (ถ้าเช้า ก็กด Y-y ถ้าไม่เช้า ก็กด N-n)
        # ถ้าหาก รถเช้า มีค่าเท่ากับ Y แล้วเป็นจริง
        # ให้รับค่าจำนวนวันที่จะเช้ารถ และ นำไปคำนวณกับโดยเอา ราคา 2000 คูณด้วย จำนวนวันที่จะเช้ารถ และนำไปเก็บที่ตัวแปร price_car
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
        os.system('cls'); time.sleep(1.5) # ใช้ในการเคลียหน้าจอส่วนบนออกไปทุก 1.5 วินาที
        input_receipt(packet_input, people_input, summation_packet, rent_day, price_car, many_room, many_day, price_room)
except (ValueError, KeyboardInterrupt):
    print("error".upper())
