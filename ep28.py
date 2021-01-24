#Break/continue
i=0
while i<10:
    i+=1
    if i==2:
        continue
    if i==5:
        break
    print(i)
    
else:
    print("จบโปรแกรม")

print("แสดงผลเลขคี่")
for i in range(10):
    if i%2==0:
        continue
    print(i)