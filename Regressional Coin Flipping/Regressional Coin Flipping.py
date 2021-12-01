# -*- coding: utf-8 -*-
"""
@author: avarm030
"""

# Take the required number of coins

coins = input('Enter the number of coins:\n >>>')
coins_list=[]


# loop to make N+=1

i=0
while i<int(coins):
    coins_list.append('H')
    i+=1
# loop to flip every N'th coin
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

    
# count the total occurences of H and T and print them

heads_count = [char for char in coins_list if char == 'H']
tails_count = [char for char in coins_list if char == 'T']
       
print(f'For {coins} coins, there are {len(heads_count)} heads and {len(tails_count)} tails in the end')

