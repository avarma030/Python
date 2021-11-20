# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 15:09:42 2021

@author: avarm
"""

card=input('Please enter your card number:\n >>>')
#print(card)

if len(card)==16:
    required_digits=card[-2::-2]
    required_digits=list(required_digits)
    
    a=[]
    for i in range(len(required_digits)):
        mul_2=2*int(required_digits[i])
        a.append(mul_2)
    #print(a)
    
    a_str = ''.join([str(elem) for elem in a])
    #print(a_str)
    
    required_digits_list=[]
    for i in a_str:
        required_digits_list.append(int(i))
    #print(required_digits_list)
    
    remaining_digits=card[::-2]
    #print(remaining_digits)
    
    remaining_digits_list=[]
    for i in remaining_digits:
        p=int(i)
        remaining_digits_list.append(p)
    #print(remaining_digits_list)
    
    total_required=sum(required_digits_list)
    #print(total)
    total_remaining=sum(remaining_digits_list)
    #print(total_1)
    final=total_required+total_remaining
    #print(final)
    
    if final%10==0:
        print('It is a valid credit card!')
    else:
        print('Sorry! Your credit card number is invalid. Please enter a valid card number')
else:
    print('Please make sure you have enetred a valid 16 digit card number')
    


    
    

    