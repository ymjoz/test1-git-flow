# Description: This is another module that imports my_module

import info 
import pkg1.module1 as module1
import pkg1.module2 as module2
import domain_mail_decorator



teslaCar = module1.AutoCar('tesla')
teslaCar.run()

cb650 = module2.Scooter('red', 'cb650')
cb650.drive()

module1.test('孫女訪問中')


print(info.tesla)

print(info.embraer)

first, second, third = info.vehicle_model
print(first, second, third)

# sandai_mail = domain_mail_decorator.urmail('sandai', 'o')
# osaka_mail = domain_mail_decorator.urmail('osaka', 'g')
# print(sandai_mail)
# print(osaka_mail)

@domain_mail_decorator.multiDomainEmailDecorator
def testmail(name, domain):
  return name

black_mail = testmail('BlackSmith', 'y')
print(black_mail)