'''
to create symmetric difference 
to remove all items from set 
to find maximum and  minimum Value in set
'''
                
                                   
set={23,453,43,23,54,43,86}         #to create set
set.add(5)                          #to add members in set


# remove items from set if it is present in list
if 41 in set:
    set.remove(41)
else:
    print("Not present")

print(set)

set1={23,42,54,6,65,53}
set2={23,43}
print(set.intersection(set1))           #to create intersection of set
print(set.union(set1))                  #to create union of set
print(set-set1)                         #to create set difference 
print(set2.issubset(set))               #to check set is subset of another set
print(len(set))                                        #to find lenght of set