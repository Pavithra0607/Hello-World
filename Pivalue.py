'''
Name: Pivalue.py
Purpose: To display pi value upto n digits entered by user
input: An integer upto 50
'''
from math import pi
while True:
    try:
        number_of_places = int(input("Please enter the number of places you want to see after decimal point: "))
    except:
        print("Please enter a correct number!")
        continue
    else:
        if number_of_places > 50:
            print("Number till 50 is only allowed!")
            continue
        else:
            print("Pi value upto {n} digit is {p:.{n}f}".format(n=number_of_places,p=pi))
            break
