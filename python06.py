# input statement ตัว python ใช้คำสั่ง input()
# แต่มีข้อกำหนดอยู่ค่า ข้อมูลที่ป้อนถือเป็น string ทั้งหมด
# คำสั่งแปลง string เป็นตัวเลข เช่น int( ???? ), float( ???? ) , ...........
 
fname = input("ป้อนชื่อ : ")
year_born = input('ป้อนปีเกิด พ.ศ. : ')
salary = float(input('ป้อนเงินเดือน : '))


print(f'สวัสดีคุณ {fname}')
print(f'คุณเกิดปี พ.ศ. {year_born} ตอนนี้คุณอายุ {2568 - int(year_born)} ปี')
print(f'คุณได้เงินเดือน {salary} บาท ภาษี 7% เป็นเงิน{salary * 7 / 100} บาท')

