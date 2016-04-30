#coding=utf8
"""AB猜数字游戏
"""
import random
max_try = 5
c = 3
allow_number_str = '1234567890'
goal_str = ''.join(random.sample(allow_number_str,c))
print goal_str
try_count = 0
while 1:
    raw_str =  raw_input('input %d difference numbers in 0-9 like "678"\n>>>'%c).strip()
    # 在Python中可以使用a == b == c连等的判定条件
    if not (c == len(raw_str) == len(set(raw_str) & set(allow_number_str))):
        print 'invalid input format,LOOK THE HINT!!!'
        continue
    try_count += 1
    a_count,b_count = 0,0
    for r, g in zip(raw_str, goal_str):
        if r == g:
            a_count += 1
        elif r in goal_str:
            b_count += 1
    print '%dA%dB' % (a_count, b_count)
    if a_count == c and b_count == 0:
        print 'you win!'
        break
    if try_count == max_try:
        print 'you fail'
        break
