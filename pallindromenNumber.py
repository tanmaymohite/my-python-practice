#cheak weather number is pallindrome or not

p=input('enter the number: ')
p=int(p)

tempP=p

rev=0
while p > 0:
     r = p % 10
     rev = rev * 10 +r
     p = p // 10
print(rev)

if rev == tempP:
    print('The number is  pallindrome  ')
elif rev != tempP:
    print('The number is not  pallindrome ')

