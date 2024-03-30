'''to create new dictonary with three different dictoary
write a python script to sort(ascending/ discending order) a dictonary
to check a given key is already present in dictonary
to sum and multiply all items in dictonary
to remove a key from dictonary
to remove duplicate from dictonary
to check Dictonary is empty or not
create dictonary from string (w3resouce)to {'w':1,'3':2,'r':3}

'''

'''                 #to add a key to Directory
dict={}
dict['time']='precious'
print(dict)
'''
'''                
                #to create new dictonary with three different dictoary
dict1={10:100,20:200}                
dict2={10:100,20:400}
dict3={10:5,20:10}
dictionary={}

#dictionary.update(dict1)
#dictionary.update(dict2)
#dictionary.update(dict3)
print(dictionary)
'''
                    
                    #dictonary containing 1 to n in form of {n:n*n}
square = lambda  x:x*x
x=int(input())
dictionary={}
dict={}
i=1
while(i==x):
    dict={x:square(x)}
    dictionary.update(dict)
    i+=1
    print(dictionary)