def fluid_to_mililiters(num):
    total = float(num*29.57353)
    print("Result : ",total)
    
def mililiters_to_fluid(num):
    total = float(num/29.57353)
    print("Result : ",total)
    
print("Welcome to converter Calculator")
ans = int(input("What measure are you trying to convert?(Please enter the number\n1. Fluid ounce\n2. Mililiters"))
if ans==1:
    number = int(input("Please enter the amount : "))
    fluid_to_mililiters(number)
elif ans==2:
    number = float(input("Please enter the amount : "))
    mililiters_to_fluid(number)
else:
    print("Please enter the right number")
    
