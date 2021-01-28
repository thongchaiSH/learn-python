# EP2 Try except with while

while True:
    try:
        number1 = int(input("Number1 : "))
        number2 = int(input("Number2 : "))
        result = number1/number2
        print("result=", result)
        break
    except Exception as e:
        print("Error", e)
        
