income=int(input("enter the income: "))
hre=int(input("enter rent: "))
ded=int(input("enter deduction: "))
t=income-(hre+ded)
print(t)
t=t-300000
if(t>300000 and t<600000):
    i=(t*10)/100
    print("tax is",i)
elif(t>600000 and t<1000000):
    i=(t*15)/100
    print("tax is",i)
else:
    i=(t*20)/100
    print("tax is",i)