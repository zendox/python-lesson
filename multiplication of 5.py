# 1,2,3,4,5,6,]=[sunday,monday,tuesday,wednesday,thursday,friday]
days = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
number = int(input("number"))
print(days[number - 1])
if number == 0 or number == 6:
    print("Holiday")
    print([0])
