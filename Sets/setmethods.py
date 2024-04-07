#Union Gives All the distinct elements from both sets
#combines elements from both sets ,removing Duplicates
a={1,2,3,45,6,67,8787,4}
b={232,344,23,23,4,6}
c=a|b
print(f'Union ==={c}')

#Intersection ---> Contains Comman elements from both sets

d=a&b
print(f'intersection=={d}')

# Symetric Difference------> Finds elements that are in either of the sets but not in both
e=a^b
print(e)


#Add new element
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}



# Remove  Removes the specified element from the set. Raises a KeyError if the element is not present.
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

# discard(element): Removes the specified element from the set if it is present. If the element is not present, it does nothing.
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}


# clear(): Removes all elements from the set.
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()


# copy(): Returns a shallow copy of the set.
my_set = {1, 2, 3}
copy_set = my_set.copy()





