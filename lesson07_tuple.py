# touple
"""
タプルは値の代入をサポートしていない
listはブラケット[]で定義するが
tupleは、パレンティス()、もしくはパランティスも無しのカンマ区切りでで定義する
tupleは、再代入できないのでほぼ読み込み専用




ただし、tupleにはlistを入れられるので
listの一部であれば、再代入による変更が可能


>>> t = (1,2,3,4,5)
>>> t
(1, 2, 3, 4, 5)
>>> type(t)
<class 'tuple'>
>>> t[0] =100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
>>> t = ([1,2,3],[4,5,6])
>>> t
([1, 2, 3], [4, 5, 6])
>>> t[0] = [11,12,13]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t[0][0] = 19
>>> t
([19, 2, 3], [4, 5, 6])
>>>
>>> t1 = 1,
>>> t2 0 2,
  File "<stdin>", line 1
    t2 0 2,
       ^
SyntaxError: invalid syntax
>>> t2 = 2,
>>> type(t1)
<class 'tuple'>
>>> type(t2)
<class 'tuple'>
>>> new_t = t1 + t2
>>> new_t
(1, 2)
"""


