# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 17:36:55 2021

@author: avarm
"""

coins=input('Enter the number of coins:\n >>>')
coins_list=[]


i=0
while i<int(coins):
    #print('H')
    coins_list.append('H')
    i+=1
#print(coins_list)
#print(len(coins_list))

q=0
while q in range(len(coins_list)-1):
    p=1+q
    while p in range(len(coins_list)):
        #print(p)
        if coins_list[p]=='H':
            coins_list[p]='T'
        elif coins_list[p]=='T':
            coins_list[p]='H'
        p+=2+q
    q+=1
#print(coins_list)

heads=[]
tails=[]
for char in coins_list:
    if char=='H':
        heads.append(char)
    elif char=='T':
        tails.append('T')
        
# for c,i in enumerate(coins_list):
#     if i=='H':
#         print(c, i)
       
print(f'For {coins} coins, there are {len(heads)} heads and {len(tails)} tails in the end')
    

