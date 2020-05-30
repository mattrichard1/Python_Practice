# Number 1:
#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
    return
print("Problem 1:")
print(sleep_in(0, 0))
print(sleep_in(0, 1))
print(sleep_in(1, 0))
print(sleep_in(1, 1))



# Number 2:
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

def monkey_trouble(a_smile, b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False
    return
print("\n" "Problem 2:")
print(monkey_trouble(0, 0))
print(monkey_trouble(0, 1))
print(monkey_trouble(1, 0))
print(monkey_trouble(1, 1))



# Number 3:
# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'

def string_times(str, n):
    output = str * n
    return output
print("\n" "Problem 3:")
print(string_times('Hi', 4))
print(string_times('what', 3))
print(string_times('donkey', 2))



# Number 4:
# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'

def front_times(str, n):
    output = str[0:3] * n
    return output
print("\n" "Problem 4:")
print(front_times('Hi', 4))
print(front_times('what', 3))
print(front_times('donkey', 2))



# Number 5:
# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'

def string_bits(str):
    output = ''
    for i in range(len(str)):
        if i % 2 == 0:
            output += str[i]
    return output
print("\n" "Problem 5:")
print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('heeololeo'))



# Number 6:
# Given a string, return a string where for every char in the original, there are two chars.
# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'

def double_char(str):
    output = ''
    for i in range(len(str)):
        output += str[i] * 2
    return output
print("\n" "Problem 6:")
print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))



# Number 7:
# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
# first_last6([1, 2, 6]) → True
# first_last6([6, 1, 2, 3]) → True
# first_last6([13, 6, 1, 2, 3]) → False

def first_last6(array):
    if array[0] == 6 or array[-1] == 6:
        return True
    else:
        return False
    return
print("\n" "Problem 7:")
print(first_last6([1, 2, 6]))
print(first_last6([6, 1, 2, 3]))
print(first_last6([13, 6, 1, 2, 3]))