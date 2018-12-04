#Python Parameters
"""
stack stores: parameters, ret adddress, and local variables
def foo(l):
    l.append(77)

x=[11]
foo(x)
print(x)  #list will be appended [11,77] because l is a pass by address

def bar(l):
    l=[88, 99]

x=[11]
bar(x)

print(x)     #printing this out will only be 11 because the l is a seperate object from
             #x l points to a seperate address the l.append changes x because it is an object
             #referencing the address of x but simply assigning l=[] does not change the value of x
             #it creates a new address for a new list named l seperate from x

"""
