# Primitive Data types (ชนิดข้อมูลพื้นฐาน)
# 1. string '????' , "????", '''????''', """???"""
# 2. integer 10, 30, 40, ...
# 3. float 12.234, 2342.34, 23.234234, ......
# 4. boolean True, False
# 5. complex number จำนวนเชิงซ้อน เช่น 1 + 2j
 
# Compound Data types (ชนิดข้อมูลแบบกลุ่ม)
# 1. list
# 2. tuple
# 3. set
# 4. dictionary
# -------------------------------------------
# ชนิดข้อมูลแบบ List
# -ประกอบด้วยข้อมูลหลายข้อมูล
# -ที่แต่ละข้อมูลมี index number กำกับ โดยเริ่มที่ 0 (มองจากซ้ายไปขวา) แต่เร่มที่ -1 (มองจากขวาไปซ้าย)
# -ทุกข้อมูลสามารถเปลี่ยนค่าได้
# -ต้องเขียนอยู่ใน [ ???? ]
# -เพิ่มข้อมูลได้ ลบข้อมูลออกได้
# -การเข้าถึงข้อมูลใน List ใช้ index number
listData1 = [10, 20, 30, 40]
listData2 = [10, 20, 'สมชาย', True, [1, 2, 3]]
print(listData1[2]) #เข้าถึงข้อมูล 30
print(listData1[-2]) #เข้าถึงข้อมูล 30
print('--------------------------')
print(listData2[3]) #เข้าถึงข้อมูล True
print(listData2[-2]) #เข้าถึงข้อมูล True
print('--------------------------')
print(listData2)
listData2[2] = 'สมหญิง'
print(listData2)
listData2[4][0] = 111
listData2[4][2] = 333
print(listData2)