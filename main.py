# Description: This is another module that imports my_module

import add_module
import feature3_2 
import pkg1.module1 as module1
import pkg1.module2 as module2



car = module1.AutoCar('tesla')
car.run()

cb650 = module2.Scooter('red', 'cb650')
cb650.drive()

module1.test('jack')