#เจาะลึกการใช้ String
name="thongchai" #index of string start at 0
print(name[0])
print(name[0:5]) #substring index start - end+1
print(name[:5]) #Start 0 - 4

print(name[-2]) #ขวาไปซ้าย
print(name[-4:])

#func len ความยาวของ String
print(len(name))

#func strip ลบช่องว่างหน้าหลัง
print(" name ".strip())
#func lstrip ลบช่องว่างซ้าย
print(" name ".lstrip())
#func rstrip ลบช่องว่างซ้าย
print(" name ".rstrip())

#func upper แปลงเป็นตัวพิมพ์ใหญ่
print(name.upper());
#func lower แปลงเป็นตัวพิมพ์เล็ก
print(name.lower());

#func capitalize แปลงข้อความตัวแรกสุดเป็นตัวพิมพ์ใหญ่
print(name.capitalize())

#func replace แทนที่คำทั้งหมด
print(name.replace("c","55"))
print(name.replace("h","55",1)) #2 คำตำแหน่งที่ต้องการเปลี่ยน

#in เช็คว่ามีคำในตัวแปร ?
name="ไปซื้อข้าวอาหารที่ตลาด"
print("name = ",name)
print("มีคำว่าข้าวใน name ?","ข้าว" in name)
print("มีคำว่าไข่ใน name ?","ไข่" in name)

#not in เช็คว่าไม่มีคำในตัวแปร ?
print("มีคำว่าไข่ไม่มีใน name ?","ไข่" not in name)