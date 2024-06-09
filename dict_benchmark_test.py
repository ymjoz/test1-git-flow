# dict test: https://youtu.be/NjeiQY9aNW4?si=RxgZmz8gxQCm2L3B

import timeit

setup = "d = {'a': 1, 'b': 2}"

"""
key值正常的情況下，if、get、try的效能差異不大:
py dict_benchmark_test.py
0.0662617789930664 (if 最慢)
0.05820659198798239 (get 次之)
0.04346542700659484 (try 最快)

key值不存在的情況下，if的效能最好，get次之，try最差:
py dict_benchmark_test.py
0.03444947101525031
0.05628524400526658
0.2449634749791585 (try 最慢)
"""

# if
check_if = """
if 'a' in d:
  x = d['a'] + 1
else:
  x = 1
"""

# get
check_get = """
x = d.get('a', 0) + 1
"""

# try
check_try = """
try:
  x = d['a'] + 1
except KeyError:
  x = 1
""" 

# 程式執行時間
print(timeit.timeit(stmt=check_if, setup=setup))
print(timeit.timeit(stmt=check_get, setup=setup))
print(timeit.timeit(stmt=check_try, setup=setup))