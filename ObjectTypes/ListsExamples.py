l = []
print(l)

l = [0, 1, 2]
print('Original: ' + str(l))
print(l[1])
l.reverse()
print('Reverse: ' + str(l))

l = ['abc', ['def', 'ghi']]
print(l)

l = list('spam')
print(l)
print(l[1:3])
print(len(l))

l = list(range(-4, 4))
print(l)
print(3 in l)
print('a' in l)

for x in l : print(x)

del l[:]
l.append('text')
print(l)

list_generator = [c * 4 for c in 'SPAM']
print(list_generator)

l = ['spam', 'Spam', 'SPAM!']
print(l)
l[1] = 'eggs'
print(l)
l[0:2] = ['eat', 'more']
print(l)

l = [1, 2]
l.extend([3, 4, 5])
print(l)
print(l.pop())
l.reverse()
print(l)
print(list(reversed(l)))
l.insert(3, 'test')
print(l)
l.remove('test')
print(l)
l.pop(0)
print(l)