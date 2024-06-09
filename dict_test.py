# dict test: https://youtu.be/NjeiQY9aNW4?si=RxgZmz8gxQCm2L3B

import timeit

d = {'a': 1, 'b': 2}

# x = d['a'] + 1


# if
if 'a' in d:
  x = d['a'] + 1
else:
  x = 0
# get
x = d.get('a', 0) + 1

# try
try:
  x = d['a'] + 1
except KeyError:
  print('key not found')
  x = 1
  
print(x)