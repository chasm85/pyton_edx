#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 10:32:33 2020

@author: mariusz
"""

print("Please think of a number between 0 and 100!: ")
min =0
max =100

while True:
    answer = min + (max - min)//2   #podział na pół bez reszty
    print("Is your secret number: " + str(answer))
    
    odpowiedz = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if odpowiedz == "c":
        print("Game over. Your secret number was: ", end=str(answer))
        break
    
    elif odpowiedz == "l":
        min = answer  
    
    elif odpowiedz == "h":
        max = answer
    
    else:
        print("Sorry, I did not understand your input.")
    
