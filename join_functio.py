num=int(input("enter the number: \n"))
table=[i*num for i in range(1,11)]
print(table)
table2=[]
for i in table:
    table2.append(str(i))
print("\n".join(table2))