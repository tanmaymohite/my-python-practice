#This is to print reverse of given number
n=input('enter the number: ')
n=int(n)
s = 0
while n > 0:
    r = n % 10
    s = s + r
    n = n // 10

print(n)
