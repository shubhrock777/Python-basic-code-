####python code module 4

#########Q1



def age(x):
    if x<=10:
        print ("Children")
    elif x>10 and x<=60:
        print("normal citizen")
    elif x>60:
        print("senior citizen")
    else:
        print("wrong age")

age(6)

age(11)

age(61)


###########Q2
sex = str(input('Sex [Male or Female ] : '))
age = int(input('please enter your age : '))

if sex == 'Male' and age>60 :
    print("70% of fare is applicable")
elif sex == "Female" and age>60:
    print("50% of fare is applicable.")
elif sex == 'Male' and age<=60 :
    print("100% of fare is applicable")
elif sex == "Female" and age<=60:
    print("70% of fare is applicable")
else:
    print("Please inter right informatations")




##########3
def number(x):
    if x%5==0 and x>0:
        print("number is positive and divisible by 5")
    else:
        print("number is not positive or not divisible by 5")
number(455410)
number(25255555501)



