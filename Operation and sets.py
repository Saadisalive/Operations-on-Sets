#Differencetypes of sets in python 
#set of integers
my_set = {1,2,3}
print(my_set)

#set f mixed data types
my_set = {1.0,"Hello",(1,2,3)}
print(my_set)
#set cannot have duplicates
my_set = {1,2,3,4,3,2}
print(my_set)

#we can make set from a list
my_set = set([1,2,3,2])
print(my_set)

#remove a number from a seet 
num_set = set([0 , 1 ,3 ,4 ,5])
print(my_set,"\n")
print(num_set)
num_set.pop()
print("After removing the first element from the set")
print(num_set,"\n")