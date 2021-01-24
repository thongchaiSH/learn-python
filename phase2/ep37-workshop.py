#รับและเรียงลำดับข้อมูลตัวเลข
number=[]
for i in range(5):
    number.append(int(input("Input number = ")))

print("number",number)
number.sort() #sort asc
print("number sort asc",number)
number.reverse() #sort desc
print("number sort desc",number)