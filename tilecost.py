'''
Name: tilecost.py
Purpose: Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take
to cover a floor plan of width and height, using a cost entered by the user.
input: cost/sqft,width,height
'''
sqft_cost = float(input("Enter the cost of tile in Rs per sqft: "))
width = float(input("Enter the width of the floor in ft: "))
height = float(input("Enter the height of the floor in ft: "))
total_cost = sqft_cost * width * height
print('Total cost of Tile for Floor {:.2f} x {:.2f} would be Rs.{:.2f}'.format(width,height,total_cost))
