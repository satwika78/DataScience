def check(n):
    for i in range(2,n):
        if(n%i==0):
            print("not prime")
            return
    print("Prime")
    return

num=int(input("enter a number: "))
if(num%2==0):
    print("even")
    print("not prime")
else:
    print("odd")
    print(check(num))

if(num%5==0):
    print("divisible by 5")
else:
    print("Not divisible by 5")

sum=(num*(num+1))/2
print("sum is ",sum)
