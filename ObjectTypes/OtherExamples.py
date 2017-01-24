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