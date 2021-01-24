#เจาะลึกการใช้ List
#เขียนแบบ primitive
a=1
a1=2
a3=3
#non primitive : list
arr=[1,2,3,4]
name=["นาย A","นาย B"]
all=[10,"นายไข่",True,3.14,-10]
print(all)
#constructor
consall=list(["นายไข่",True,3.14])
print(consall)
print(type(consall))

#การเข้าถึงข้อมูล
print(consall[0])
print(len(consall)) #size

#การแก้ไขข้อมูล
number=[1,2,3,4,5]
print("ก่อนแก่ไข",number)
number[2]=9
print("หลังแก่ไข",number)

#การแสดงผลด้วย loop
for i in number:
    print("สมาชิก = ",i)

#การตรวจสอบข้อมูล
fruit=["มะม่วง","มะนาว","มะละกอ","มะยม"]
if "มะม่วง" in fruit :
    print("มะม่วง in fruit")

print("Size of fruit =",len(fruit))

#การเพิ่มข้อมูล append แบบต่อท้าย
print("Before add ",fruit)
fruit.append("กล้วย")
print("After add ",fruit)
#การเพิ่มข้อมูล insert แบบแทรก => (index,สมาชิกใหม่)
fruit.insert(0,"แทรก")
print("After insert ",fruit)

# การลบข้อมูล remove
fruit.remove("แทรก")
print("After remove ",fruit)
# การลบข้อมูล pop ลบข้อมูลตัวท้ายสุดออกไป
fruit.pop()
print("After pop ",fruit)
# การลบข้อมูล del โดย index
del fruit[1] #remove index 1
print("After del  ",fruit)

#del fruit ลบตัวแปรทิ้งและ clear หน่วยความจำ
#print("After del  ",fruit)

#clear ลบข้อมูลใน list ออกไป
fruit.clear()
print("Clear fruit",fruit)


'''
การคัดลอกข้อมูล
'''
fruit=["มะม่วง","มะนาว","มะละกอ","มะยม"]
fruit_copy=[]
fruit_copy=fruit.copy()
print(fruit_copy)

'''
การวมข้อมูล
'''
allGroup=number+fruit
print("การวมข้อมูล",allGroup)

'''
แสดงจำนวนสมาชิก
'''
allGroup.append(1)
allGroup.append(1)
print("allGroup",allGroup)
print("count 1 of allGroup=",allGroup.count(1))

#เพิ่มข้อมูลจาก list อื่น
allGroup.extend(fruit)
print("allGroup",allGroup)