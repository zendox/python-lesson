#To innumber and find out whether the number inserted is true or false
n = int(input("enter n: "))
ans = True
for i in range(2, n):
    if n % i == 0:
        ans = False
        break
print(ans)
