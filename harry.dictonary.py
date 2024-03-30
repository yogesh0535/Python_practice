'''
dict={
    "paani":"water",
    "agni":"fire",
    "wayu":"air",
}

print(dict["agni"])
print(dict.get("wayu"))
print(dict.keys())
print(dict.values())
'''
'''
s=set()
for i in range(0,11):
    a=int(input("enter number: "))
    s.add(a)
print(s)
print(len(s))
print(type(s))
'''

dict={}
for i in range(0,4):
    a=input("enter the name: ")
    b=input("enter the colour: ")
    dict.update({a:b})

print(dict)