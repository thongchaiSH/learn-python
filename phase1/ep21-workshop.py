#โปรแกรมคำนวณ BMI ดัชนีมวลกาย ปรับปรุง
#Formula BMI = น้ำหนัก (Kg) / ส่วนสูง*ส่วนสูง (m)

weight = float(input("Weight [kg]"))
height = float(input("Height [cm]"))

#Process
height=height/100;
bmi=weight/(height**2)

# Output
print("BMI",bmi)
'''
<18 ต่ำกว่าเกณฑ์
18.5 - 22.9 = สมส่วน
23.0 - 24.9 = น้ำหนักเกิน
25.0 - 29.9 = โรคอ้วน ระดับที่ 1
>30 = โรคอ้วนอันตราย
'''
if bmi>0 and bmi<18:
    print("ต่ำกว่าเกณฑ์")
elif bmi>=18 and bmi<23:
    print("สมส่วน")
elif bmi>=23 and bmi<25:
    print("น้ำหนักเกิน")
elif bmi>=25 and bmi<=30:
    print("โรคอ้วน ระดับที่ 1")
elif bmi>30:
    print("โรคอ้วนอันตราย")
else :
    print("ไม่ทราบค่าชัดเจน")
