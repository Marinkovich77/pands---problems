#This program calculates how many tiles you 
#need when tiling a floor (in m2)

length = float(input("Enter room length:"))
width = float(input("Enter room width:"))

area = length * width

needed = area * 1.05

print("You need", needed, "tiles in squared metres")