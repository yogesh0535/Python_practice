file="learning_python.txt"

with open(file,'r') as object:
    for line in object:
        print(line)
    # print(object)

filename = 'learning_python.txt'
with open(filename) as file_object:

    for line in file_object:
        print(line)