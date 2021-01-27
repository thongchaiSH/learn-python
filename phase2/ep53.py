#EP53 Arbitrary Arguments (kwargs)

# *args
def add(*number):
    print(number)

# **kwargs keyword arguments
def displayData(**kwargs):
    print("data=",kwargs)
    print("fName=",kwargs['fName'])

# displayData("Fluke")
displayData(fName="Fluke")
displayData(fName="Fluke",city="BKK")
displayData(fName="Fluke",lName="fail")