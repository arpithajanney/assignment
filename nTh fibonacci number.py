n=int(input("enter a number:"))

def fib(f1,f2,n):
    f3=0
    for i in range(2,n):
        f3=f1+f2
        f1=f2
        f2=f3
    return f3

print(fib(1,1,n))
