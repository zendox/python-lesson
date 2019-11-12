L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Delete odd number from the list using loop
for item in L:
    if item % 2 != 0:
        L.remove(item)
print(L)
