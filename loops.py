'''
array of 3*4 or matrix of 3*4
progarm that accepts string and counts the numbr of digits and letters
even numbers from 100 to 400
programs to print alphabetic pattern of 'A','D','G','L','M','o','P','R','S' by stars
to check alphabet is vowel or constant
to convert month name to number of days in that month
to check triangle is equilateral ,isosceles or scalene
to find median of three values
to calculate sum and average of n integer numbers
to print multiplication table of number

#  1
#  22
#  333
#  4444
#  55555
#  666666

                                    #  *
                                    #  **
                                    #  ***
                                    #  ****
                                    #  ***
                                    #  **
                                    #  *    



'''

'''                
                     #numbers divsible by 7 and 5 b/w 1500 and 2700

list=[]
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        list.append(i)
    else:
        pass
print(list)
'''                     
'''                        #to guess a number from 1 to 9 
while(True):
    import random
    guess=random.randint(1,9)
    num=int(input("\nEnter your guess from 1 to 9: \n"))
    if (num==guess):
        print("done!")

    else:
        print("miss")
'''


'''       #program that accepts word from user and reverse it
n=int(input("Enter number:\n"))
r=0
while(n!=0):
    r=r*10+n%10
    n=n/10

print(f"number is {r}")
'''

'''          #to count number of even and odd numbers from a series(1,2,3...9)
num=[1,2,3,4,5,6,7,8,9]
count_even=0
count_odd=0
for i in num:
    if (i%2==0):
        count_even+=1
    else:
        count_odd+=1
print(f"Number of Even numbers is: {count_even} \t\t\t Odd numbers is:{count_odd}")
'''
             
'''           #by using 'contine' satement print numbres from 0 to 8 except 3 and 6
               
num=[1,2,3,4,5,6,7,8,9]
for i in num:
    if((i== 3) or (i==6)):
        continue
    else:
        print(i)
'''
'''
                #to get fabonacci series from o to 50 (0,1,1,2,3,5,8,13,21,34)
n=int(input("Enter the last digit:\n"))
first=int(input("Enter the first number:\n"))
second=int(input("Enter the second digit:\n"))
print(first)
print(second)
third=first+second
while(third<=n):
    third=first+second
    print(third)
    first=second
    second=third


'''