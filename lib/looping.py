#!/usr/bin/env python3
def happy_new_year():
    # For loop to count down from 10 to 1
    for count in range(10, 0, -1):
        print(count)
    
    # Print the final message
    print("Happy New Year!")

# Call the function to see the result
happy_new_year()
def square_integers(int_list):
    return[x**2 for x in int_list]
    pass

def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Call the function
fizzbuzz()

