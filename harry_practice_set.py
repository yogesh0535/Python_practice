'''
class microsoft:
    pass    
    def details(self):
        print(f"id = {self.id}")
        print(f"Name of employee is: {self.name} lives at {self.address}")



emp1=microsoft()
emp2=microsoft()
emp3=microsoft()
emp1.name="yogesh"
emp2.name="bhardwaj"
emp3.name="beniwal"
emp1.address="mathura,india"
emp2.address="chhata,india"
emp3.address="hulwana,india"
emp1.id=1
emp2.id=2
emp3.id=3
emp1.details()
emp2.details()
emp3.details()
'''

'''
class square:
    pass
    def squ_cube(self):
        return (f"square of {self.a} is: {self.a*self.a} and cube of {self.a} is: {self.a*self.a*self.a}" )



s=square()
s.a=int(input("Enter the number: "))
print(s.squ_cube())
'''


'''
class square:
    pass
    def squ_cube(self):
        print(f"Hello, {self.name} sir")
        print(f"the square of {self.a} is: {self.a*self.a}" )
        print(f"the cube of {self.a} is: {self.a*self.a*self.a}")


s=square()
s.name=input("enter your name: ")
s.a=int(input("Enter the number: "))
s.squ_cube()
'''
'''
class train:
    pass
    def train1(self):
        print(f"name: {self.name}")
        print(f"fair: {self.fair}")
        print(f"seats: {self.seats}")

t1=train()
t2=train()
t3=train()
t1.name='janta'
t2.name='super'
t3.name='hero'
t1.fair='Rs.2/km'
t1.seats='100'
t2.fair='Rs.5/km'
t2.seats='50'
t3.fair='Rs.4/km'
t3.seats='80'

i=int(input("Enter train number: "))
if(i==1):
    t1.train1()
elif(i==2):
    t2.train1()
elif(i==3):
    t3.train1()
'''

