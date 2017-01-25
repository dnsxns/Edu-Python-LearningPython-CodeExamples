# Switch-case alternative
choise = 'ham'
print{'spam': 1.25,
      'ham': 1.99,
      'eggs': 0.99,
      'bacon': 1.10}[choise]

branch = {'spam': 1.25,
          'ham': 1.99,
          'eggs': 0.99}
print branch.get('spam', 'Bad choice')
print branch.get('bacon', 'Bad choice')

choice = 'bacon'
if choise in branch:
    print(branch[choise])
else:
    print('Bad choice')

a = 't' if 'spam' else 'f'
print(a)

x = a or b or c or None
print(x)

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, '=>', d[key])

print(list(range(5)))
print(list(range(2, 5)))
print(list(range(0, 10, 2)))

for i in range(3):
    print(i, 'Pythons')

x = 'spam'
for i in range(len(x)):
    print(x[i])

s = 'qwertyuiop'
print(list(range(0, len(s), 2)))
for i in range(0, len(s), 2):
    print(s[i])

print('-' * 8)
s = 'abcdefghijk'
for c in s[::2]:
    print(c)

l1 = [1, 3, 5, 7, 9]
l2 = [2, 4, 6, 8, 10]
print(zip(l1, l2))

for (x, y) in zip(l1, l2):
    print(x, y, '+', x+y)

t1, t2, t3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
print(list(zip(t1, t2, t3)))

keys = ['spam', 'eggs', 'toast']
vals = [1, 2, 3]
print(dict(zip(keys, vals)))

s = 'spam'
for (offset, item) in enumerate(s):
    print(item, 'appears at offset', offset)
print([c * i for (i, c) in enumerate(s)])