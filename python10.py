# Function (การทำงานหนึ่งๆ ) Ep.01
# นิยาม คือ การทำงานหนึ่งๆ จะไม่ทำงานหากไม่ถูกเรียกใช้ (call function)
# Function มี 4 ประเภทใหญ่
# 1. function ที่ไม่มี parameter และไม่มี return
# 2. function ที่มี parameter และไม่มี return
# 3. function ที่ไม่มี parameter และมี return
# 4. function ที่มี parameter และมี return
 
# การสร้าง Function ใน Python ต้องมีคีย์เวิร์ด  def
# 1. function ที่ไม่มี parameter และไม่มี return
def say_h( ) :
    print('Hello...')
    print('Hi...')
    print('Hey...')
 
def show_cal( ):
    print(10 + 20 + 30)
    x = 10
    y = x
    print(x + y)
 
say_h( )
show_cal( )
say_h( )
say_h( )