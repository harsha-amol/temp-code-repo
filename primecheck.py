#to check number is prime or not
'''
num =11
if num>=1:
    for i in range(2,int(num/2)+1):
        if num%i == 0:
            print("number is not prime")
            break
        else:
             print("number is prime")
             break
else:
    print(num,"is not a prime number")


def fib(n):
    x=0
    y=1
    while(i<=num):
        x,y=y,x+y
        yield(y)
        
value=fib(10)
for i in value:
    print(i)

c="g"
print("asci value of c",ord(c))

def fib(n):
    x=0
    y=1
    while(x<=n):
        x,y=y,x+y
        print(y)

print(fib(11))
'''

arr = [12, 3, 4, 15]
ans=sum(arr)
print ('Sum of the array is ',ans)


sum=0
arr = [12, 3, 4, 15,45]
for i in arr:
    sum=sum+i
print(sum)    
























