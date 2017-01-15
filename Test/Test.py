# First Python scenario
#!/usr/bin/env python
import sys
import TestModule
from TestModule import subject
import Threenames

print(sys.platform)
print(2 ** 100) # 2 to the power 100
x = 'Spam'
print(x * 8)

print(TestModule.title)
print(subject)
print(dir(Threenames)) # get list of names in module