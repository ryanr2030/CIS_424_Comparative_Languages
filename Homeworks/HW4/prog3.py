#!/usr/bin/python3
#Krishaun Bartlet 2696351 Ryan Reynolds 2693018
from functools import reduce

numbers = (1.0, 2.0, -1.0, 3.0, 25.0, -3.0, 2.5, 2.8)

#using anaymous fuction with map function to repalce negative real numbers with 0.0
print("Map function result")
print(list(map(lambda n: 0.0 if n < 0.0 else n, numbers)))  
        
#using anaymous fuction with the reduce function to find the maximum value in the list
print("Reduce function result")
print(reduce(lambda a,b : a if a < b else b,numbers))

#using anaymous fuction with the filter function to find values between 2.0 and 3.0 in the list
print("Filter function result")
print(list(filter(lambda a : (a <= 3.0 and a >= 2.0),numbers)))


