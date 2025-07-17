# 2. function ที่มี parameter และไม่มี return
# parameter คือ ตัวแปรประเภทหนึ่ง ที่รับข้อมูลมาใช้ได้เฉพาะใน function นั้นๆ เท่านั้น
def sayHi(name, year_born) :
    print(f'สวัสดีคุณ {name}')
    print(f'คุณเกิดปี {year_born} อายุ {2568 - year_born} ปี')
 
def sumNumber(n1, n2) :
    print(f'{n1} + {n2} = {n1 + n2}')
 
sayHi('Sombat', 2500)
sayHi('Somjai', 2525)
 
sumNumber(10, 20)
sumNumber(100, 200)
 
sayHi('Somsri', 2545)