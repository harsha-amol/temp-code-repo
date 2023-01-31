'''
num1 = int(input("enter a nuber1"))
num2 = int(input("enter a nuber2"))

num3= num1+num2
print(num3)
print("sum of {0} and {1} is {2}" .format(num1,num2,num3)


a = int(input("enter a nuber1"))
b = int(input("enter a nuber2"))
def maximum(a, b):
      
    if a >= b:
        return a
    else:
        return b
      
print(maximum(a, b))

a=2
b=4
print(a if a >= b else b)

def factorial(n):
    return 1 if (n==0 or n==1) else n* factorial(n-1);


num = 5
print ("factorial of num is",factorial(num))
'''
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
 
# Driver program
starting_range = 2
ending_range = 9
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)
