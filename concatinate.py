#concatinate multiple dictionaries
d1 = {'john':76,'hom':65}
d2 = {'yam':89,"tam":97}
d3 = {}
for d in (d1,d2):
    d3.update(d)
    print(d3)
