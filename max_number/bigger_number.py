#!/usr/bin/env python

first_number = input("Please enter the first number: ")
second_number = input("Please enter the second number: ")

if first_number > second_number:
    print(first_number + " Is bigger")
elif second_number > first_number:
    print(second_number + " Is bigger")
elif first_number == second_number:
    print("The numbers are equal.")
