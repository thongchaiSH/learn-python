# Type conversion
x =10
y= 3.14
z="20"

print(type(x))
print(type(y))
print(type(z))
#บวกเลข 
result=x+y
print(result)

#String => Int
print(int(z)+y+x)

#Int => String
print(str(x)+z)

result=str(x)+z
print(result)

#String => Float
a="3.141"
print(float(a))

#Float to Int
print(int(y))

#Int to Float
print(float(x))

# กำหนดค่าใหม่ String to float
z=float(z)
print(type(z))