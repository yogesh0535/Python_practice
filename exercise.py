'''
 # to find given number is even or not

num=int(input("enter the number: "))
if(num%2==0):
    print("{num} is even")
else:
    print(f"{num} is odd")
'''
'''
#temperature from centigrate to faheranhite

c=int(input("Enter the temperature: "))
f=(9*(c)/5)+32
print(f)
'''

#average of a set of integers
count=int(input("Enter the number of integers: \n"))
sum=0
i=0
while(i<count):
    num=int(input(f"Enter the {i+1} integer : "))
    sum=sum+num
    i=i+1
avg=sum/count
print(f"averge of numbers is : {avg}")

'''
# product of integers
count=int(input("Enter the number of integers: \n"))
product=1
i=0
while(i<count):
    num=int(input(f"Enter the {i+1} integer : "))
    product=product*num
    i=i+1
print(f"product of numbers is : {product}")
'''
'''
import math
#area and circumference of circle
r=float(input("Enter the radius of circle: "))
area=math.pi*r*r
circ=math.pi*r*2
print(f"area of circle is :{area} and circumference of circle is :{circ}")
'''

#display number in reverse order
num=int(input("enter the number: "))
new=0
#6534
while(num!=0):
    r=num%10
    new=new*10+r
    num=num//10
print(new)
'''

#sum of digits of number
num=int(input("enter the integer: "))
sum=0
while(num!=0):
    rem=num%10
    sum=sum+rem
    num=num//10
print(f"sum of digits of number is : {sum}")
'''
'''
#multiples of 3 between 10 and 50
for i in range(10,51):
    if(i%3==0):
        print(i)
'''
'''
ls=[]
for i in range (100,151):
    sum=0
    while(i!=0):
        rem=i%10
        sum=sum+rem

        if(sum%2==0):
            ls.append(i)
        i=i//10


print(ls)
    
    '''