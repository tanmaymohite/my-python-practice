print('******************Candy machine******************')

x = input('How many Candies do you want: ')
x = int(x)

i = 1
while i<=x:
    print('Dairy milk')
    i+=1

    if x > 50:
        t = 1
        while t<=50:
            print('chocobar')
            t +=1
        print('Out of stock')
        break