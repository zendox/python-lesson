#merge dictionary
D1 = {'a':100, 'b':200}
D2 = {'x':300, 'y':200}
D = D1.copy()
D.update(D2)
print(D)
