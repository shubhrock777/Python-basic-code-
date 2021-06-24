# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 13:58:56 2021

@author: SHBHAM
"""
  ###############Assigement 01 Data types ################
###########Q 1

list_a = [7, 8, 1.5, "apple", "lemon", 57j, 85j, True, False]

list_b =["peanut", "coffee", 7, 1.5, 87, 9, 77j, False]

#a
list_ab= list_a + list_b

list_ab

#b
def frequency(list_ab):
    ferq={}
    for ele in list_ab:
        if ele in ferq :
            ferq[ele] +=1
        else:
            ferq[ele]=1
    return ferq

frequency(list_ab)
 
#c 

def reverse(list_ab):
    new_list = list_ab[::-1]
    return new_list 

reverse(list_ab)
    
    
    
    
############Q 2


set_a={x for x in range(1,11)}
print(set_a)

set_b={x for x in range(5,16)}
print(set_b)    
  
####a 
common_elements = [ele for ele in set_a if ele in set_b]
print(common_elements)
    
####b   

uniq_elemets =[ele for ele in set_a if ele not in set_b] + [ele for ele in set_b if ele not in set_a]
print(uniq_elemets)


#####c
set_a.remove(7)
set_a

set_b.remove(7)
set_b

dic = {"State":('Kerala','Maharashtra','Uttar Pradesh','West Bengal','Chhattisgarh'),
       "covid-19 cases":(760933,640045,60000,550000,280000)}

  

