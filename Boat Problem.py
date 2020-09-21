import numpy as np

def move(left, boat, right):
    print('Step {}:' .format(counter), 'Move {} into boat' .format(occupants))

# counter = 1
# def boats(n, left, boat, right):
#     if n == 0:
#         return
#     else:

def start(n):
    left = set()
    for i in range(1,n+1):
        left.add('dog_{}' .format(i))
        left.add('man_{}' .format(i))
    return left

print(sorted(start(3)))

def move(n, f, t):
    if n > 3:
        return False
    if n == 0:
        return False
