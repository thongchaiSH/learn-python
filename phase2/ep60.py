# EP60 Function หาผลรวมค่าเฉลี่ย

def summation(number):
    total = 0
    avg = 0.0
    for i in number:
        total += i
    avg = total/len(number)
    return total, avg


x = [1, 2, 3, 4, 5]

sum,avg=summation(x)
print("sum:",sum)
print("avg:",avg)