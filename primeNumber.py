
n = input("\nEnter a number: ")
n = int(n)

d = 2

while d < n:
    if n % d == 0:
        break
    d = d + 1

if d == n:
    print("\nNumber is prime")
else:
    print("\nNumber is not prime")
