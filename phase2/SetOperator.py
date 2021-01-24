# Union การรวมข้อมูล
fruitA = {"ส้ม", "มะละกอ", "กล้วย", "มะขาม"}
fruitB = {"สตอเบอรี่", "กีวี"}
allFruit = fruitA.union(fruitB) 
# fruitA=fruitA.update(fruitB)
print("allFruit",allFruit)

# Copy set
fruitC=fruitA.copy()
print("fruitC",fruitC)

# Difference หาตัวที่ต่างกัน
fruitA = {"ส้ม", "มะละกอ", "กล้วย", "มะขาม","เงาะ"}
fruitB =  {"ส้ม", "มะละกอ", "กล้วย", "มะขาม","ส้มโอ"}
fruitC=fruitA.difference(fruitB)
print("fruitC",fruitC)
# fruitA.difference_update(fruitB)
# print("fruitA",fruitA)

#intersection ข้อมูลที่เหมือนกัน
fruitC=fruitA.intersection(fruitB)
print("fruitC",fruitC)

# Subset
fish=set(["ปลาดุก","ปลาดุก","ปลากัด","ปลาหมอ","ปลาซิว"])
x={"ปลาหมอ","ปลาซิว"}
print(x.issubset(fish))

# Max , min
number ={1,2,3,4,5,65,6}
print("Min =",min(number))
print("Max =",max(number))

# frozenset เป็นการกำหนดไม่สามารถเพิ่มลดแก้ไขได้
fruit = frozenset(["ส้ม", "มะละกอ", "กล้วย", "มะขาม"])
print("fruit",fruit)