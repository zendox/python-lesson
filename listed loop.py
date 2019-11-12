L1 = [1,"red",2,3]
L2 = ["APPLE","ORANGE",]
L3 = ["php","python","java"]
# concatenate L1 and L2
# add L1 in L2
# add a programming language in l3
# remove unwanted data from L1
result = L1+L2
print(result)
L2.extend(L1)
print(L2)

L3.append("c++")
print(L3)
# append (adds element on last of a blog) (only last)

L1.remove("red")

# remove (it removes the element from current element or blog)
print(L1)
