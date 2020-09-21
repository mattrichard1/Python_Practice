# Recursive Solution:
def move_r(f, t):
    print("Step {}:" .format(counter_r), "Move disc from {} to {}" .format(f,t))

counter_r = 1
def hanoi_r(n, source, aux, target):
    global counter_r
    if n == 0:
        return
    else:
        hanoi_r(n-1, source, target, aux)
        move_r(source, target)
        counter_r += 1
        hanoi_r(n-1, aux, source, target)

# Sequential Solution:
# How in the world do you do this???
# def possible(n):
#     system = [list(range(1, n + 1)), [0], [0]]
#     for i in range(3):
#         if system[i] > n:
#             return False
#     return True


# def hanoi_s(n, source, aux, target):
#     counter = 1
#     for i in range(3):




print('Recursive Soln:')
hanoi_r(20, 'A', 'B', 'C')

# print('\n', 'Sequential Soln:', sep='')

# hanoi_S(3, 'A', 'B', 'C')