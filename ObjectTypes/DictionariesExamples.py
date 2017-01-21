d = {}
print(d)

d = {'spam': 2, 'eggs': 3}
print(d)
print('spam' in d)

d = {'food': {'ham': 1, 'egg': 2}}
print(d)
print(d['food']['ham'])

d = dict(name='Bob', age=40)
print(d)
print(d['name'])

d = dict.fromkeys(['a', 'b'])
print(d)

d = {'ham': 1, 'spam': 2, 'eggs': 3}
d['ham'] = ['grill', 'bake', 'fry']
print(d)
del(d['eggs'])
print(d)
d['brunch'] = 'Bacon'
print(d)
print(d.keys())
print(d.values())

d2 = {'toast': 4, 'muffin': 5}
d.update(d2)
print(d)
d.pop('spam')
print(d)

table = {'Python': 'Guido van Rossum',
         'Perl': 'Larry Wall',
         'Tcl': 'John Ousterhout'}
language = 'Python'
creator = table[language]
print(creator)

for lang in table:
    print(lang, table[lang])

d1 = {'name': 'mel', 'age': 45}
print(d1)
d2 = {}
d2['name'] = 'mel'
d2['age'] = 45
print(d2)
d3 = dict(name='mel', age=45)
print(d3)
d4 = dict([('name', 'mel'), ('age', 45)])
print(d4)