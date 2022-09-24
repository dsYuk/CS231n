from nis import cat
from xmlrpc.server import DocCGIXMLRPCRequestHandler


t = True
f = False
print(type(t))  # class 'bool'
print(t and f)  # False
print(t or f)   # True
print(not t)    # False
print(t != f)   # True

hello = 'hello'
world = 'world'
print(hello)    # hello
print(len(hello)) # 5
hw = hello + ' ' + world
print(hw) # hello world
hw12 = '%s %s %d' % (hello, world, 12)
print(hw12) # hello world 12

s = "hello"
print(s.capitalize()) # Hello
print(s.upper()) # HELLO
print(s.rjust(7)) # "  hello"
print(s.center(7)) # " hello "
print(s.replace('l', '(ell)')) # he(ell)(ell)o
print('  world '.strip()) # world

xs = [3, 1, 2]
print(xs, xs[2]) # [3, 1, 2] 2
print(xs[-1]) # 2
xs[2] = 'foo'
print(xs) # [3, 1, 'foo']
xs.append('bar')
print(xs) # [3, 1, 'foo', 'bar']
x = xs.pop() # 맨 마지막 요소 추출
print(x, xs) # bar [3, 1, 'foo']

nums = list(range(5))
print(nums) # [0, 1, 2, 3, 4]
print(nums[2:4]) # [2, 3]
print(nums[2:]) # [2, ,3, 4]
print(nums[:2]) # [0, 1]
print(nums[:]) # [0, 1, 2, 3, 4]
print(nums[: -1]) # [0, 1, 2, 3]
nums[2: 4] = [8, 9]
print(nums) # [0, 1, 2, 8, 9]

animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
    # cat dog monkey 한 줄에 하나씩 출력

for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
    # #1: cat #2: dog #3: monkey 한 줄에 하나씩 출력

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares) # [0, 1, 4, 9, 16]

squares = [x ** 2 for x in nums]
print(squares) # [0, 1, 4, 9, 16]

even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares) # [0, 4, 16]

d = {'cat': 'cute', 'dog': 'furry'}
print(d['cat']) # cute
print('cat' in d) # True
d['fish'] = 'wet'
print(d['fish']) # wet
print(d.get('monkey', 'N/A')) # N/A
print(d.get('fish', 'N/A')) # wet
del d['fish']
print(d.get('fish', 'N/A')) # N/A

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))
    # A person has 2 legs
    # A cat has 4 legs
    # A spider has 8 legs

for animal, legs in d.items():
    print('A %s has %d legs' % (animal, legs))
    # A person has 2 legs
    # A cat has 4 legs
    # A spider has 8 legs

nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square) # {0: 0, 2: 4, 4: 16}

animals = {'cat', 'dog'}
print('cat' in animals) # True
print('fish' in animals) # False
animals.add('fish')
print('fish' in animals) # True
print(len(animals)) # 3
animals.add('cat')
print(len(animals)) # 3
animals.remove('cat') # cat 삭제
print(len(animals)) # 2

animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
    # #1: dog #2: fish #3: cat 한 줄에 하나씩 출력

from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums) # {0, 1, 2, 3, 4, 5}

d = {(x, x + 1): x for x in range(10)}
t = 5, 6
print(type(t)) # <class 'tuple'>
print(d[t]) # 5
print(d[(1, 2)]) # 1

def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'
for x in [-1, 0, 1]:
    print(sign(x))
    # negative zero positive 한 줄에 하나씩 출력

def hello(name, loud=False):
    if loud:
        print('HELLO, %s!' % name.upper())
    else:
        print('Hello, %s' % name)
hello('Bob') # Hello, Bob
hello('fred', loud = True) # HELLO, FRED!

class Greeter(object):
    def __init__(self, name):
        self.name = name # instance variable 생성
    def greet(self, loud = False):
        if loud:
            print('HELLO, %s!' % self.name.upper())
        else:
            print('Hello, %s' % self.name)
g = Greeter('Fred')
g.greet() # Hello, Fred
g.greet(loud = True) # HELLO, FRED!