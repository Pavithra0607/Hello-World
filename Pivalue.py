'''
Name: Pivalue.py
Purpose: To display pi value upto n digits entered by user
input: An integer number
'''
from math import pi
number_of_places = int(input("Please enter the number of places you want to see after decimal point: "))
print("Pi value upto {} digit is {:.{}f}".format(number_of_places,pi,number_of_places))
