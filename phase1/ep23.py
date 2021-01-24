#เจาะลึกการใช้ String 2
fname="thongchai"
lname="sidthi"
age="26"
salary=283992.2223123

# การต่อ String ผ่าน format
fullname=fname+lname+age
print(fullname)
# text="ชื่อต้น :{}\t นามสกุล:{}\t อายุ:{}\t"
text="ชื่อต้น :{1}\t นามสกุล:{1}\t อายุ:{2}\t อาชีพ:{3}\t  เงินเดือน:{4:.2f}"
print(text.format(fname,lname,age,"โปรแกรมเมอร์",salary));

'''
นับจำนวนคำในประโยค func count
'''
fruit="ไปซื้อผลไม้ ทุเรียน มังคุด ส้ม ที่ตลาดทุเรียน"
print("พบคำว่า ทุเรียน : ",fruit.count("ทุเรียน"),"คำ")

#เช็คคำขึ้นต้น/ลงท้าย  startswith/endswith
name="นายกอไก่ ใจดี"
if name.startswith("นาย"):
    print("นาย")
else :
    print("บุคคลอื่น")
name="1150"
if name.endswith("0"):
    print("ลงท้ายด้วย 0")
