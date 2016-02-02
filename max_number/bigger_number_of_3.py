#!/usr/bin/env python

first_number = input("Please enter the first number: ")
second_number = input("Please enter the second number: ")
third_number = input("Please enter the third number: ")

if first_number > second_number and first_number > third_number:
    print("The first number is the biggest")
elif second_number > first_number and second_number > third_number:
    print("The second number is the biggest")
elif third_number > second_number and third_number > first_number:
    print("The third number is the biggest")
