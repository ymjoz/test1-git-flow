# Description: Decorator to add domain to email

# https://youtu.be/LG-VhiWOKG8?si=FK3FlzSqcCzNkBe6

def f():
  x = 1
  a = locals()
  x = 2
  b = locals()
  print(a,b)
  print(id(a), id(b))

# f()

def double(x):
  return x*2
def triple(x):
  return x*3

# def calc(func, x):
#   print(func(x))

# calc(double, 3)
# calc(triple, 3)

# def get_multiple_func(n):
#   def f(x):
#     return x*n
#   return f

# double = get_multiple_func(2)
# triple = get_multiple_func(3)

# print(double(3))
# print(triple(3))


def multiDomainEmailDecorator(func):
  def wrapper(name, domain='d'):
    if domain == 'g':
      return func(name, domain) + '@gmail.com'
    elif domain == 'y':
      return func(name, domain) + '@yahoo.com'
    elif domain == 'o':
      return func(name, domain) + '@outlook.com'
    return func(name, domain) + '@duck.com'
  return wrapper
  
@multiDomainEmailDecorator
def urmail(name,domain):
  return name 


if __name__ == '__main__':
  print(urmail('john', 'o'))
  print(urmail('tom'))
