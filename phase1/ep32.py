#ตัวเลขขั้นบันได

round=int(input("Round = "))
# round=5
for i in range(round+1):
    # print(i+1)
    result=""
    for j in range(0,i):
        print(j+1,end='')
        # result+=str(j+1)
    print(result)