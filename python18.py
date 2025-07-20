# ชนิดข้อมูลแบบ dictionary
# - ประกอบด้วยข้อมูลหลายข้อมูล
# - ต้องเขียนอยู่ใน { ???? }
# - ข้อมูลแบบ dictionary จะอยู่ในรูปแบบ key: value
# - โดย key จะต้องไม่ซ้ำกัน และเป็นได้แค่ string หรือ number
# - โดย value สามารถซ้ำกันได้ และเป็นข้อมูลอะไรก็ได้
# - ทุก value สามารถเปลี่ยนค่าได้
# - การเข้าถึง value ใน dictionary จะใช้ key เขียนใน [ ]

listData1 = [10, 20, 30, 40, 10]     # จะถือว่ามี 5 ข้อมูล
tupleData1 = (10, 20, 30, 40, 10)    # จะถือว่ามี 5 ข้อมูล
setData1 = {10, 20, 30, 40, 10}      # จะถือว่ามี 4 ข้อมูล

dictData1 = {
    'name': 'สมชาย',
    'age': 30,
    'is_student': True,
    'scores': [80, 90, 100],
    111: 'wow wow wow'
}
print(dictData1)
print(dictData1['name'])
print(dictData1['age'])
print(dictData1['is_student'])
print(dictData1['scores'])
print(dictData1[111])