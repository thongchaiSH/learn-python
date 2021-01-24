tup=(1,2,3,1) #Tuple
tup=tuple((1,2,3,1,"ทุเรียน")) #Constructor
lis=[1,2,3,4] #List
print(type(tup))
print(lis)

# การเข้าถึง
print(tup[::-1])

# การแก้ไขข้อมูล
lis=list(tup)
lis[0]="test"
tup=tuple(lis)
# tup[0]="test" #ไม่สามารถทำได้ ต้องแปลงเป็น list แล้วแก้ไขค่าแล้ว convert to tuple อีกครั้ง
print(tup)

#การแสดงผลด้วย loop
for i in tup:
    print(i)

[print(i) for i in tup]

if "ทุเรียน" in tup:
    print("เป็นสมาชิก")
else:
    print("ไม่เป็นสมาชิก")

print("tup size",len(tup))

# initial tuple
x=tuple(("Test"))
print(type(x))
x=("Test2")
print(type(x))
x=("Test2",)
print(type(x))

#การเพิ่มข้อมูล Tuple ต้องเป็นชนิดเดียวกัน
name=("Fluke","Aoi","Jane")
new=("Nut",)
name=name+new+("test2",)
print(name)

# การเพิ่ม /ลบใช้แบบเดียวกับ list

#การค้นหา index
print("Index of Nut",name.index("Nut"))

tup=(23,213,24,5,6,7,3,1,2)
lis=list(tup)
lis.sort()
tup=tuple(lis)
print("Sort",tup)

# นำค่าใน tuple ในใส่ตัวแปร 
tup=(10,20,30)
a,b,c=tup
print(a)
print(b)
print(c)

#สลับ tuple
x=(50,20)
y=(88,99)
print("Before x",x)
print("Before y",y)
x,y=y,x
print("After x",x)
print("After y",y)

#tuple = > String
character=('k','o','n','g')
name="".join(character)
print("name",name)

#Revert tuple
x=(1,2,3,4,5)
x=x[::-1]
print("x",x)