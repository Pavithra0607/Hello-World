'''
Name: fibonacci.py
Purpose: Enter a number and have the program generate the
Fibonacci sequence to that number or to the Nth number.
input: An integer number
'''

# define a generator to generate n fibonacci numbers
def gen_fib(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

# Ask for user input
while True:
    try:
        num = int(input("Enter the number of values you want to see in fibonacci sequence: "))
    except:
        print("Please enter a correct number!")
        continue
    else:
        # Iterate through the generator to print the numbers
        for i in gen_fib(num):
            print(i)
        break
