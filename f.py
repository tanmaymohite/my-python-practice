print('Function practice')

print('press the following number for following function')
print('\n')

l = ['Addition = 1','substraction = 2','multiplication = 3','Division = 4']

for k in l:
    print(k)

print('\n')

j = input('Which function do you want : ')
j = int(j)


t = input('enter the first number: ')
t = int(t)

h = input('Enter the second number: ')
h = int(h)


def addition():
    ans=t+h
    print('\nAns: '+str(ans))

def substraction():
    ans1=t-h
    print('\nAns: '+str(ans1))

def mulipication():
    ans2=t*h
    print('\nAns: '+str(ans2))

def division():
    ans3=t/h
    print('\nAns: '+str(ans3))

if j == 1:
    addition()

if j == 2:
    substraction()

if j == 3:
    mulipication()

if j == 4:
    division()