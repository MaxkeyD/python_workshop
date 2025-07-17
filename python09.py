# control statement Ep.03
# คำสั่ง break และ continue ใน Loop
# break ใน Loop ทำงานเมื่อใด หยุดทำซ้ำทันที
# continue ใน Loop ทำงานเมื่อใด ไปรอบต่อไปทันที
 
for x in range(1, 6) :
    print(f'{x} SAU')
    if x == 3 :
        break
    print(f'{x} IoT')
print('-------------------------')
for y in range(1, 6) :
    print(f'{y} SAU')
    if y == 3 :
        continue
    print(f'{y} IoT')