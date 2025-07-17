# 3. function ที่ไม่มี parameter และมี return
# return คือ คำสั่งที่จะส่งค่าข้อมูลกลับไปยังจุดเรียกใช้ฟังก์ชัน (จุด call function)
 
def say_hi( ) :
    print('Hi....')
    return 'สวัสดี'
 
def showSenPa( ) :
    return '----------------------------'
 
print( showSenPa() )
x = say_hi( )
print( showSenPa() )
print( x)