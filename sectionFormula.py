#section formula program
print('\nSection formula')
print('\nmX2+nX1/m+n,mY2+nY1/m+n')

x1=input('\nEnter the value of x1: ')
x1=int(x1)

x2=input('\nEnter the value of x2: ')
x2=int(x2)

y1=input('\nEnter the value of y1: ')
y1=int(y1)

y2=input('\nEnter the value of y2: ')
y2=int(y2)

m=input('\nEnter the value of m: ')
m=int(m)

n=input('\nEnter the value of n: ')
n=int(n)

x=((m * x2) + (n * x1))/(m + n)
y=((m * y2) + (n * y1))/(m + n)

print('x,y= '+str(x)+' , '+str(y))
