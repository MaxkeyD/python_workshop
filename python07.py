# control statement Ep.01
# กลุ่ม พิสูจน์/ตรวจสอบ ก่อนทำงานใดๆ (if, if-else, if-elif-else)
# พิสูจน์/ตรวจสอบ ครั้งเดียว จริงทำ/เท็จไม่ทำ (if)
num1 = 50
if num1 > 25 :
    print('wow...')
    print('woo...')
 

if num1 < 0 :
    print('Hello...')
 
# พิสูจน์/ตรวจสอบ ครั้งเดียว จริงทำอย่าง/เท็จทำอีกอย่าง (if-else)
print('-----------------------------')
data1 = 'Bang5na'
if data1 >= 'Bangpoo' :
    print('Hi...')
    print(1111)
else :
    print('Hey')
    print(2222)
 
# พิสูจน์/ตรวจสอบ หลายครั้ง (if-elif-else)
score = 35
if score >= 80 :
    print('Grade A')
    print('Grade A')
    print('Grade A')
elif score >= 70 :
    print('Grade B')
elif score >= 60 :
    print('Grade C')
elif score >= 50 :
    print('Grade D')
    print('Grade D')
    print('Grade D')
    print('Grade D')
else:
    print('Grade F')