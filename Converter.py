'''
Name: Converter.py
Purpose: Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.
input: An integer number or a binary number
'''

# decimal to binary converter
def decToBin():
    while True:
        try:
            dec_num = int(input("Enter a decimal number: "))
        except:
            print("Only integer value allowed!")
            continue
        else:
            print("Binary equivalent of {} is {}".format(dec_num,bin(dec_num)))
            break

# binary to decimal converter
def binToDec():
    s = input("Enter a binary number: ")
    dec_no = sum(int(c) * (2 ** i) for i, c in enumerate(s[::-1]))
    print("Decimal equivalent of {} is {}".format(s,dec_no))

decToBin()

binToDec()
