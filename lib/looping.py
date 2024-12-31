#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while (0 < i <= 10):
        print(i)
        if i == 1:
            print("Happy New Year!")
        i -= 1

def square_integers(int_list):
    # code goes here!
    return [int * int for int in int_list]
    

def fizzbuzz():
    # code goes here!
    for i in range(100):
        if (((i + 1) % 3) == 0) and (((i + 1) % 5) != 0):
            print("Fizz")
        elif (((i + 1) % 5) == 0) and (((i + 1) % 3) != 0):
            print("Buzz")
        elif (((i + 1) % 5) == 0) and (((i + 1) % 3) == 0):
            print("FizzBuzz")
        else:
            print(i+1)