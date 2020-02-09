#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 18:55:51 2020

@author: mariusz
"""
#Dla każdej litery program musi zdecydować czy litera kolejna w ciągu jest >= od niej
s = 'abcdefgabcdddd'

licznik = 0
maxlicznik = 0
result = 0

for c in range(len(s) - 1):          
    if (s[c] <= s[c + 1]):           
        licznik += 1                
        if licznik > maxlicznik:    
            maxlicznik = licznik     
            result = c + 1           
    else:                            
        licznik = 0
start = result - maxlicznik          

print('Longest substring in alphabetical order is:', s[start:result + 1])