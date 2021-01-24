'''
list =[] ,แก้ไขข้อมูลได้ ,ข้อมูลซ้ำกันได้ ,ซ้ายไปขวา
tuple =() ,แก้ไขข้อมูลไม่ได้ ,ข้อมูลซ้ำกันได้ ,ซ้ายไปขวา
set ={} ,แก้ไขข้อมูลไม่ได้ ,ข้อมูลซ้ำกันไม่ได้ ,ลำดับไม่แน่นอน
'''
#แบบปกติ
fruit={"ส้ม","มะละกอ","กล้วย","มะขาม"}
print(fruit)
#Constructor
fish=set(["ปลาดุก","ปลาดุก","ปลากัด","ปลาหมอ"])
print(fish)

#เพิ่มข้อมูลสมาชิก
fruit.add("มะยม")
fruit.add("ทุเรียน")
print("fruit",fruit)

#เพิ่มข้อมูลสมาชิกหลายตัว
lis=["มะยม","ตะไคร้","โหรพา","ชะอม"]
fruit.update(lis) #update ข้อมูลแบบ list
fruit.update(["อ้อย","ส้มโอ"])
print("fruit",fruit)
for item in fruit:
    print(item)

# การลบข้อมูล
fruit.remove("อ้อย") #ไม่สามารถลบข้อมูลที่ไม่มีใน set ได้
fruit.discard("อ้อย2") #ไม่ว่าจะมีหรือไม่มีจะไม่ error
print("fruit",fruit)

# ลบข้อมูลใน set ทิ้ง
fruit.clear()
print("fruit",fruit)

del fruit