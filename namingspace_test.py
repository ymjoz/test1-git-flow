
x = 'global'

def outer_func():
  x = 'outer'
  print(x)

  def inner_func():
    x = 'inner'
    print(x)
    
  inner_func()
  
outer_func()

print(x)