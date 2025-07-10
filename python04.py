# output statement EP.02
#กรณี print เดียว มีข้อมูลหลายประเภท 
#แบบที่ 1 ใช้ , คั่น โดยทุกๆ , จะเว้นวรรค 1 space เวลาแสดงผล
fullname = 'Somjai'
print('AAAA',1111,10 + 20 + 30 , True,'Wow wow wow',fullname)

#แบบที่ 2 ใช้เครื่องหมาย + คั่น แต่มีข้อกำหนดอยู่ว่าข้อมูลใดที่ไม่ใช่ string ต้องแปลงให้เป็น string 
#และโดยทุกๆ + จะไม่มีเว้นวรรค ให้ 
print('AAAA'+str(1111)+str(10 + 20 + 30) + str(True)+'Wow wow wow'+fullname)

#แบบที่ 3 ใช้เมธอด format() คือตรงไหนไม่ใช้ string รวมถึงตัวแปลและนิพจน์ให้ใส่ {} แล้วเอาข้อมูลที่ไม่ใช่ string ไปใส่ใน () ของเมธอด format()
print('AAAA {} {} {} Wow wow wow {}'.format(1111,10+20+30,True,fullname))

#แบบที่ 4 ใช้ f-string มีข้อกำหนด ตรงไหนที่ไม่ใช่ string ให้ใส่ข้อมูลตัวแปร นิพจน์ใน{}
print(f'AAAA {1111} {10+20+30} {True} Wow wow wow {fullname}')