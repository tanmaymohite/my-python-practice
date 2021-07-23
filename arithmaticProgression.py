print('A.P')
a = input('enter the first term: ')
a = float(a)

d = input('enter the common difference: ')
d = float(d)

e = input('how many terms do you want: ')
e = float(e)

i=1
print(a)
while i < e:
  t2 = a + d
  print(t2)
  a=t2
  i = i + 1