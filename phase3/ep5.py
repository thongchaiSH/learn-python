#EP5 จัดการ Text ไฟล์ใน Python
# open("ชื่อไฟล์","โหมด","การเข้ารหัส") mode =r,w,a,
try:
    fr=open("file/student.txt","r",encoding="utf-8")
    print(fr.read())
except FileNotFoundError:
    print("หาไฟล์ไม่เจอ")