L=[1,2,3,4,5,6,7,8,9,10,11,12,13]
#delete three elements from last using loop
for i in range(len(L) - 1, len(L) - 4, -1):
    L.pop()
    print(L)
