#age1=int(input("Enter the values of age1"))
#age2=int(input("Enter the values of age2"))
#age3=int(input("Enter the values of age3"))
age1,age2,age3=[int(x) for x in input("Enter three values:").split()]
print(age1,age2,age3)
if age1>age2:
    if age1>age3:
        print(age1)
    elif age2>age3:
        print(age2)
    else:
        print(age3)
if age2>age1:
    if age2>age3:
        print(age2)
    elif age3>age2:
        print(age3)
    else:
        print(age1)
