import re
import sys

# --- Strings
s = 'Hello, World!'
print(s.find('ld'))

print(dir(s))
print(help(s.rjust)) # get documentation about method

msg = """ aaa bbb'''bbbb""bbb'bbbccccc"""
print(msg)

str1 = "Hello, Python world"
print(re.match('Hello,[ \t]*(.*)world', str1).group(1))
print(str1[::-1]) # Reverse

reply = """
Greetings...
Hello %(name)s!
Your age squared is %(age)s
"""
values = {'name': 'Bob', 'age': 40}
print(reply % values)

template1 = '{0}, {1} and {2}'
print(template1.format('spam', 'ham', 'eggs'))

template2 = '{motto}, {pork} and {food}'
print(template2.format(motto='spam', pork='ham', food='eggs'))

print('My {config[spam]} runs {sys.platform}'.format(sys=sys, config={'spam': 'laptop'}))

# --- Lists
simple_list = ['aa', 'bb', 'cc']
simple_list.sort()
print(simple_list)
simple_list.reverse()
print(simple_list)

matrix_as_list = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
print(matrix_as_list)
col2 = [row[1] for row in matrix_as_list]
print(col2)
col3 = [row[2] for row in matrix_as_list if row[2] >= 6]
print(col3)
diag = [matrix_as_list[i][i] for i in [0, 1, 2]]
print(diag)
rows_sum = (sum(row) for row in matrix_as_list)
print(next(rows_sum))
print(next(rows_sum))
print(next(rows_sum))
print(list(map(sum, matrix_as_list)))

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)

# --- Dictionaries
dic1 = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(dic1['color'])
print(dic1['quantity'] + 1)

dic2 = {}
dic2['name'] = 'Bob'
dic2['job'] = 'dev'
dic2['age'] = 40
print(dic2['age'])

rec = {'name': {'first': 'Bob', 'last': 'Smith'},
       'job': ['dev', 'mgr'],
       'age': 40.5}
print(rec)
print('last name is ' + rec['name']['last'])
rec['job'].append('janitor')
print(rec['job'])

for key in rec:
    print(key, '=>', rec[key])
for char in 'Spam':
    print char * 2

i = 5
while i > 0:
    print '*' * i
    i -= 1

squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)
print(squares)

dic3 = {'a': 1, 'b': 2, 'c': 3}
dic3['d'] = 4
print(dic3['d'])
if 'e' not in dic3:
    print('Element is absent')
val1 = dic3['f'] if 'f' in dic3 else 0
print(val1)

# --- Tuples
tuple1 = (1, 2, 3)
print(tuple1)
tuple2 = tuple1 + (4, 5)
print(tuple2)

# --- Files
file1 = open('data.txt', 'w')
file1.write('Simple\n')
file1.write('text')
file1.close()

file2 = open('data.txt')
print(file2.read())

# --- Sets
x = set('spam')
y = set('ahm')
print(x, y)
print(x & y)
print(x | y)
print(x - y)

# --- Types
print(type(x))
print(type(file1))
print(type(matrix_as_list))
print(type(type(matrix_as_list)))

if type(file1) == file:
    print('file1 is file')
if type(file1) != tuple:
    print('file1 isn\'t tuple')

# --- Classes
class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)
print(bob.name)
print(sue.lastName())
sue.giveRaise(.10)
print(sue.pay)