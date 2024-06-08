
class AutoCar:
    def __init__(self, name):
        self.name = name
        print(f"pkg1.module1.AutoCar({name}) called")
        
    def run(self):
        print(f"pkg1.module1.AutoCar.run() called")
        
    def stop(self):
        print(f"pkg1.module1.AutoCar.stop() called")
        
    def __del__(self):
        print(f"pkg1.module1.AutoCar({self.name}) destroyed")




def test(name="module1"):
    print(f"pkg1.module1.test({name}) called")
    
if __name__ == '__main__':
    test('james')