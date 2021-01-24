# แปลงอุณหภูมิ
temp=input("ป้อนอุณหภูมิ (องศา) :")

isCels=temp.lower().endswith("c")
isFahr=temp.lower().endswith("f")
degree=float(temp[:-1])
print("isCels",isCels)
print("isFahr",isFahr)
print("degree",degree)

if isCels:
    result=(degree*9/5)+32
    unit_result="ฟาเรนไฮน์"
elif isFahr:
    result=(degree-32)*5/9
    unit_result="เซลเซียนส"
else :
    print("Unit fail !!.")
print("result :",result,unit_result)