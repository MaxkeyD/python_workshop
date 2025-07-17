# 4. function ที่มี parameter และมี return
# parameter คือ ตัวแปรประเภทหนึ่ง ที่รับข้อมูลมาใช้ได้เฉพาะใน function นั้นๆ เท่านั้น
 
def calSquareArea(width, long) : #หา พท.สี่เหลี่ยม
    area = width * long
    return area
 
def calTriangleArea(base, height) : #หา พท.สามเหลี่ยม
    return base * height / 2
 
 
print(f'พท.สี่เหลี่ยม กว้าง 10 ยาว 20 คือ {calSquareArea(10, 20)}')
print('-------------------------')
print(f'พท.สี่เหลี่ยม กว้าง 5 ยาว 100 คือ {calSquareArea(5, 100)}')
print('-------------------------')
print(f'พท.สามเหลี่ยม ฐาน 20 สูง 15 คือ {calTriangleArea(205,15)}')