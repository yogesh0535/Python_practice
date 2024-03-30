'''
def comparison(a,b,c):
    if(a>b and a>c):
        print(f"{a} is greater.")
    
    elif(b>c and b>a):
        print(f"{b} is greater.")
    else:
        print(f"{c} is greater.")

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
comparison(a,b,c)
'''


num=int(input("Enter the number: "))
function(num)