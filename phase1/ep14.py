#Control Structure
'''
    โครงสร้างควบคุม (Control Structure)
    1.แบบลำดับ
    2.แบบเลือก
    3.แบบทำซ้ำ
'''
'''
    if expression:
        statement
'''
age=int(input("Age : "))
if age>=15 and age <50:
    print("age > 15",age)
    print("นาย/นางสาว")
elif age>=50 and age < 100:
    print("คุณลุง")
elif age>=100 and age <150:
    print("แก่แล้ว")
elif age >= 150:
    print("ไม่ใช่คน")
else:
    print("เด็กชาย")
print("End program. ")

#Ternary Operator
print("นาย/นางสาว") if age>=15 and age <50 else  print("เด็กชาย")

