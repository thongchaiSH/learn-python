# EP56 Factorial

def factorial(number):
    if number == 1:
        return number
    else:
        return number*factorial(number-1)


print(factorial(5))
print(factorial(2))