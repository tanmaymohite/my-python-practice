

names = [ 'John', 'Jack', 'Jimmy', 'V', 'Chinu', 'Wosimosi'

                                ]

print( names )
print( names[3] )
names[3] = 'Diana'
print( names )
#-------------For loop--------------

for name in names:
    print(name)

for name in names:
    greeting = 'Hi ' + name
    print(greeting)

for name in names:
    if len(name)>7:
        print(name)
