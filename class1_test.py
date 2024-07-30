class TestClass:
  """
  A simple example class
  """
  rossiValue = 'rossi'
  def f(self):
    return 'hello world'

test_instance = TestClass()    

tif = test_instance.f


print(TestClass.__doc__)
print(TestClass.f)
print(test_instance.f())
print(test_instance.f)
print(TestClass.rossiValue)

test_instance.counter = 1
while test_instance.counter < 10:
  test_instance.counter = test_instance.counter * 2
print(test_instance.counter)
del test_instance.counter


print(tif())
