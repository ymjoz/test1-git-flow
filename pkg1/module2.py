

class Scooter:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        
    def drive(self):
        print('Scooter is driving')
        
    def stop(self):
        print('Scooter is stopped')
        
    def __del__(self):
        print(f"Scooter({self.color}, {self.model}) destroyed")

def m2test():
    print('m2test()')
    
    
if __name__ == '__main__':
    m2test()
    print('module2.py is executed as a script')