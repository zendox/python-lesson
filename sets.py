# create a 3 sets for the fruits, with random items,now,i need to get data how many items among the sets are repeated
# how many of them are unique, in total get all unrepeated  items
a = {'apple','ball','cat'}
b = {'apple','dog','fog'}
c= {'strawberry','apple'}
d=a. union(b)
e=d. union(c)
print(e,"union of a,band c ")
f =a.intersection(b)
g =f.intersection(c)
print(g,'intersection of a,b and c')
h =a.difference(f)
i =