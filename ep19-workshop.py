#โปรแกรมแลกเงินและหาจำนวนแบงค์
number=int(input("Input :"))

print("1,000 บาท",number//1000,"ใบ")
number%=1000
print("500 บาท",number//500,"ใบ")
number%=500
print("100 บาท",number//100,"ใบ")
number%=100