            #harry advance python practice set 
'''
while(True):
    files=['1.txt','2.txt','3.txt']

    for file in files:
        try:
            with open(file) as file_object:
                text=file_object.read
        except Exception as e:
            print(e)          
'''
'''
a=[23,4,43,23,234,231,45,65,78]

for index,item in enumerate(a):
    if (index==3 or index == 5 or index == 7):
        print(f"item is {item} in list at {index}")
'''
'''
n=int(input())
table = [n*i for i in range(1,11)]
print(table)    
'''

while(True):
    b=int(input("\nenter the divisor\n"))
    a=int(input("enter the dividend\n"))
    try:
        c=a/b
    
    except ZeroDivisionError as e:
        print("infinity\n")
    
    except ValueError as e:
        print("\nplease check the values entered!")
    else:
        print(f"{a}/{b} = {c}")
    finally:
        print("We have done")


