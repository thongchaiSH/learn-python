#EP49 Keyword Arguments

def displayData(fname,lname,city):
    print("ชื่อ :",fname)
    print("นามสกุล :",lname)
    print("ที่อยู่ :",city)

displayData("ธงไชย","สิทธิเขตกรณ์","โคราช")
displayData("jojo","bkk","jaidee") #ปัญหาคือใส่สลับกัน
#Keyword Arguments
displayData(city="bkk",lname="jaidee",fname="jojo")