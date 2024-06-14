# Date: 14/06/2024
# Author: Byron Muller
# Version 2


# Greets user
print("Welcome to the fencing quote calculator")
print("In this program, you can input the size of the paddock as well as the cost of the fence per meter")

# Get user inputs
print("Please enter your measurements in metres")

error = "Please enter a number above zero\n"
if True:
    try:
        width = float (input("Desired Width:"))
        length = float (input("Desired Length:"))
        cost_per_meter = float (input("Cost Per Meter:"))

        if width > 0:
            done = True
        if length > 0:
            done = True
        if cost_per_meter > 0:
            done = True
        else:
            print(error)
                  
    except ValueError:
        print(error)

    perimeter = width * length
    total = cost_per_meter * perimeter

    print (f"Perimeter is: {perimeter}")
    print (f"total is: {total}")
    
    

print ("Would you like to print again")




