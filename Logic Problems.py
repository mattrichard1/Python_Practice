# Problem 1:
# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
# Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → True

Weekdays = 'Monday, Tuesday, Wednesday, Thursday'
Weekends = 'Friday, Saturday, Sunday'
def party_success(cigars, day):
    day_finder = Weekends.find(day)
    if cigars > 40 and cigars < 60 and day_finder == -1:
        return True
    if cigars > 40 and day_finder > -1:
        return True
    else:
        return False
    return
# print("Party Success Problem:")
# print(party_success(50, 'Monday'))
# print(party_success(30, 'Monday'))
# print(party_success(70, 'Monday'))
# print(party_success(70, 'Saturday'))




# Problem 2:
# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes.
# The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes).
# With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
# date_fashion(5, 10) → 2
# date_fashion(5, 2) → 0
# date_fashion(5, 5) → 1

def table_chance(you, date):
    if you < 3 or date < 3:
        return 0
    if you > 7 or date > 7:
        return 2
    else:
        return 1
    return
# print('\n'"Getting a Table Problem:")
# print(table_chance(0, 5))
# print(table_chance(3, 5))
# print(table_chance(9, 5))



# Problem 3:
# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90.
# Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True

summer = 0
fall = 1
winter = 1
spring = 1
def squirrel_play(temp, season):
    if season > 0:
        if temp >= 60 and temp <= 90:
            return True
        else:
            return False
    else:
        if temp >= 60 and temp <= 100:
            return True
        else:
            return False
    return
# print('\n'"Squirrel Playing Problem:")
# print(squirrel_play(50, fall))
# print(squirrel_play(80, winter))
# print(squirrel_play(95, spring))
# print(squirrel_play(80, summer))
# print(squirrel_play(95, summer))
# print(squirrel_play(105, summer))



# Problem 4:
# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket.
# If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0

def ticket_price(speed, bday):
    limit = 60
    if bday == True:
        limit += 5
    if speed <= limit:
        return 0
    if speed > limit and speed <= (limit + 20):
        return 1
    else:
        return 2
    return
# print('\n'"Ticket Price Problem:")
# print(ticket_price(50, False))
# print(ticket_price(50, True))
# print(ticket_price(61, False))
# print(ticket_price(61, True))
# print(ticket_price(81, False))
# print(ticket_price(81, True))
# print(ticket_price(90, False))
# print(ticket_price(90, True))



# Problem 5:
# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
# sorta_sum(3, 4) → 7
# sorta_sum(9, 4) → 20
# sorta_sum(10, 11) → 21

def sorta_sum(a, b):
    y = a + b
    if y >= 10 and y <= 19:
        y = 20
    return y
# print("Strange Sums Problem:")
# print(sorta_sum(2, 4))
# print(sorta_sum(5, 9))
# print(sorta_sum(11, 1))
# print(sorta_sum(15, 6))
# print(sorta_sum(25, -3))
# print(sorta_sum(21, -4))



# Problem 6:
# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring.
# Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
# alarm_clock(1, False) → '7:00'
# alarm_clock(5, False) → '7:00'
# alarm_clock(0, False) → '10:00'

Weekdays = 'Monday, Tuesday, Wednesday, Thursday, Friday'
Weekends = 'Saturday, Sunday'
def alarm(day, vacation):
    day_finder = Weekends.find(day)
    if vacation == True:
        if day_finder < 0:
            return '10:00'
        else:
            return 'off'
    if vacation == False:
        if day_finder < 0:
            return '7:00'
        else:
            return '10:00'
    return
# print('\n''Alarm Time Problem:')
# print(alarm('Monday', False))
# print(alarm('Tuesday', True))
# print(alarm('Saturday', False))
# print(alarm('Sunday', True))



# Problem 7:
# The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6.
# Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
# love6(6, 4) → True
# love6(4, 5) → False
# love6(1, 5) → True

def love6(a, b):
    if abs(a + b) == 6 or (a - b) == 6 or (b - a) == 6:
        return True
    if a == 6 or b == 6:
        return True
    else:
        return False
    return
# print('\n''Ways to Find 6 Problem:')
# print(love6(6, 4))
# print(love6(6, 5))
# print(love6(5, 4))
# print(love6(-4, 4))
# print(love6(-6, 12))



# Problem 8:
# Given a number n, return True if n is in the range 1..10, inclusive.
# Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
# in1to10(5, False) → True
# in1to10(11, False) → False
# in1to10(11, True) → True

def in1to10(n, reverse_mode):
    if reverse_mode == False:
        if n >= 1 and n <= 10:
            return True
        else:
            return False
    else:
        if n <= 1 or n >= 10:
            return True
        else:
            return False
    return
# print('\n''In Range Problem:')
# print(in1to10(1, False))
# print(in1to10(11, False))
# print(in1to10(1, True))
# print(in1to10(28, True))



# Problem 9:
# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each).
# Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.
# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

def make_row(num_small_avail, num_big_avail, goal):
    small = 1   #in.
    big = 5     #in.
    row = 0
    num_small_used = 0
    num_big_used = 0
    while row < goal:
        if goal > (row + big):
            row += big
            num_big_avail -= 1
            num_big_used += 1
            if row < goal and num_small_avail == 0:
                return 'Can not complete row, can only make', row, 'in. long'
        else:
            row += small
            num_small_avail -= 1
            num_small_used += 1
            if row < goal and num_small_avail == 0:
                return 'Can not complete row, can only make', row, 'in. long'
    if row == goal:
        return True, row, 'Small:', num_small_used, 'Big:', num_big_used
# print('\n''Making Bricks Problem:')
# print(make_row(3, 4, 18))
# print(make_row(3, 4, 19))
# print(make_row(3, 4, 18))
# print(make_row(1000000, 1000, 1000100))

def make_bricks(sm, lg, goal):
    small = 1
    big = 5
    lg_req = goal // big
    sm_req = goal % (big * lg_req)
    if goal > big * lg + sm:
        return False, 'order more bricks'
    if sm_req > sm:
        return False, 'order more small bricks'
    else:
        return True, 'Large Bricks:', lg_req, 'Small Bricks:', sm_req
# print(make_bricks(3,1,8))
# print(make_bricks(3,1,9))
# print(make_bricks(3,2,10))
# print(make_bricks(3,2,8))
# print(make_bricks(3,2,9))



# Problem 10:
# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
# lone_sum(1, 2, 3) → 6
# lone_sum(3, 2, 3) → 2
# lone_sum(3, 3, 3) → 0

def lone_sum(a, b, c):
    if a == b and b == c:
        sum = 0
        return sum
    if a == b or a == c:
        a = -a
    if b == c:
        b = -b
    sum = a + b + c
    return sum
# print('\n''Lone Sum Problem:')
# print(lone_sum(1,2,3))
# print(lone_sum(3,2,3))
# print(lone_sum(3,3,3))
# print(lone_sum(9,2,2))



# Problem 11:
# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

def lucky_sum(a, b, c):
    unlucky = 13
    if a == unlucky and b == unlucky:
        sum = 0
        return sum
    if a == unlucky:
        a = 0
        b = 0
    if b == unlucky:
        b = 0
        c = 0
    if c == unlucky:
        c = 0
    sum = a + b + c
    return sum
# print('\n''Lucky Sum Problem:')
# print(lucky_sum(1,2,3))
# print(lucky_sum(1,2,13))
# print(lucky_sum(1,13,3))
# print(lucky_sum(1,13,13))
# print(lucky_sum(6,5,2))
# print(lucky_sum(13,2,3))
# print(lucky_sum(13,2,13))
# print(lucky_sum(13,13,2))
# print(lucky_sum(9,4,13))
# print(lucky_sum(8,13,12))



# Problem 12:
# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens.
# Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
    array = [a, b, c]
    sum = 0
    for i in range(len(array)):
        if array[i] == 15 or array[i] == 16:
            pass
        else:
            if array[i] >= 13 and array[i] <= 19:
                array[i] = 0
        sum += array[i]
    return sum
# print('\n''No Teen Sum Problem:')
# print(no_teen_sum(1,2,3))
# print(no_teen_sum(2,13,1))
# print(no_teen_sum(2,1,14))
# print(no_teen_sum(2,1,15))
# print(no_teen_sum(16,17,18))



# Problem 13:
# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20.
# Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values.
# To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().
# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10

def round_sum(a, b, c):
    nums = [a, b, c]
    total = 0
    def round_num(n):
        tens = n // 10
        ones = n % 10
        if ones < 5:
            ones = 0
        if ones % 10 >= 5:
            ones = 10
        n = ones + tens * 10
        return n
    for i in range(len(nums)):
        total += round_num(nums[i])
    return total
# print('\n''Rounding Sum Problem:')
# print(round_sum(5, 4, 9))
# print(round_sum(16, 17, 18))
# print(round_sum(6, 4, 4))



# Problem 14:
# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more.
# Note: abs(num) computes the absolute value of a number.
# close_far(1, 2, 10) → True
# close_far(1, 2, 3) → False
# close_far(4, 1, 3) → True

def close_far(a, b, c):
    