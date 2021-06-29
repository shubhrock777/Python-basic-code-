

#############Q1

## A)list1=[1,5.5,(10+20j),’data science’].. Print default functions and parameters exists in list1.

list1=[1, 5.5, (10+20j), 'data science']
print(list1)

len(list1) #length of list

#Access values in the variable using index numbers
print(list1[0])



#### B)How do we create a sequence of numbers in Python.

num = list(range(0,11,1))
num

#### C)Read the input from keyboard and print a sequence of numbers up to that number

n= int(input('Please enter a number :'))
if n>0: 
    print (list(range(0,n+1)))
    
   
    
    
    
#############22.	Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
#list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
# Create a dictionary such that list2 are keys and list 1 are values..

list1=list(range(0,10))
list1

list2=['zero','one','two','three','four','five','six','seven','eight','nine']
list2

dict_1={'List_1' : list1,
        'List_2' : list2}
dict_1

#############3Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10 to the even number and multiply with 5 if it is odd number in the list1..

list1=[3,4,5,6,7,8]

list2 = [x+10 for x in list1 if x%2==0] + [x*5 for x in list1 if x%2==1]
list2



################4

#######i)) It should accept both name of person and message you want to deliver.

name=input('Please enter your name : ')
message=input('Message you want to deliver : ') 
sentance = "Hello "+ name + " your message : "+ message 
print(sentance)      
    



#######ii) If no message is provided, it should greet a default message ‘How are you’

name=input('Please enter your name : ')
message=input('Message you want to deliver : ') 

if message =="" :
    print( "Hello "+ name + " How are you ")

else:
    print("Hello "+ name + " your message : "+ message)


