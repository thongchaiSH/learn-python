#โปรแกรมแม่สูตรคูณ
start=int(input("แม่สูตรคูณเริ่มต้น :"))
end=int(input("แม่สูตรคูณสิ้นสุด :"))

for x in range(start,end+1):
    print("แม่ =",x)
    for y in range(1,13):
        print(x,"x",y,"=",(x*y))