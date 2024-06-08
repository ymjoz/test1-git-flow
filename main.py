# Description: This is another module that imports my_module

import info 
import pkg1.module1 as module1
import pkg1.module2 as module2



teslaCar = module1.AutoCar('tesla')
teslaCar.run()

cb650 = module2.Scooter('red', 'cb650')
cb650.drive()

module1.test('孫女訪問中')


print(info.tesla)

print(info.embraer)

first, second, third = info.vehicle_model
print(first, second, third)