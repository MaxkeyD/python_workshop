# Python OOP (Object-Oriented Programming)
# Class คือ ต้นแบบ หรือ แม่แบบ ของ Object
# Object คือ วัตถุ ที่ถูกสร้างขึ้นมาจาก Class หรืออาจจะเรียกว่าตัวแทนของคลาส instance of class

class IoTSAU:
    pass

class Car:
    # data member
    brand = ""
    model = ""
    wheel = 0

    # method member
    def letGo():
        print("ไปกันเลย......")

    def carStop():
        print("จอดแล้ว.......")
oba = Car()
obB = Car()
wowA = Car()
oba.brand = "Toyota"
print(obB.whell+wowA.wheel)

oba.letGo()
wowA.letGo()
obB.carStop()