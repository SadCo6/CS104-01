names = []
for x in range (10):
    name = input ('enter names: ')
    names.append(name)
print (names)
for x in range (10):
    print (names.pop(0))
print (names)
