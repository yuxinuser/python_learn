# a = 11
# # print a
# #
# # q = ['qw', 'ds', 'xc', 'g']
# #
# # print  q
# #
# # l1 = q.__iter__()
# #
# # z = l1.next()
# #
# # print z
#
#
# def cal_sum(*args):
#     def sum():
#         ax = 0
#         for n in  args:
#             ax = ax + n
#         return  ax
#     return sum
# f = cal_sum(1,3,5,7)
# print  f()
# f1 = cal_sum(1,3,5,7)
# f2 = cal_sum(1,2,4,6)
# f1 == f2
#
# l1 = ['x','y','z']
# l2 = [1,23]
# l2 = [1,2,3]
# l3 = [(i,j) for i in l1 for j in l2]
# print  l3
#
#
# def now():
#
#     print('2013-1-2')
#
# f = now()
#
#
# import functools
# int = functools.partial(int,base = 2)
# print int('10000')
from subprocess import call
#
# print  list(map(lambda x : x * x,[1,2,3,4,5,6]))
#
#
# f = lambda x : x + x
# print f(2)
#
# def now():
#     print('20292-2029-2')
#
# f = now()
# #
# print now.__name__
#
# def log(func):
#     def wrapper(*args,**kw):
#         print ('call %s():' % func._name_)
#         return  func(*args,**kw)
#     return wrapper
#

# @log
# def now():
#     print ('2020--2-2-')

# now()
# print call now():

def build(x,y):
    return lambda: x * x + y * y
f =  build(3,2)
print  f()

print abs(100)

