#โปรแกรมคำนวณ BMI ดัชนีมวลกาย
#Formula BMI = น้ำหนัก (Kg) / ส่วนสูง*ส่วนสูง (m)

weight = float(input("Weight [kg]"))
height = float(input("Height [cm]"))

#Process
height=height/100;
bmi=weight/(height**2)

# Output
print("BMI",bmi)

