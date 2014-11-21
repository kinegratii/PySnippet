#coding=utf8
"""
for-else 实例
"""
s = ('pat','cheh','fa','yas')

print 'Q1----------'

for food in s:
    print food
    if food == 'yas':
        break
else:
    #这个不会执行
    print 'else in Q1'



print 'Q2-----------'
for food in s:
    if food == 'ccc':
        break
else:
    #这个会被执行
    print 'else in Q2'
