
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

my_dic1 = {'name': 'John', 'age': 25, 'city': 'New York'}

boeing, airbus, embraer = ['747', 'A380', 'Phenom 300'] # sequence unpacking
tesla, honda, bmw = {'tesla': 'model s', 'honda': 'civic', 'bmw': 'x5'}.values() # iterable unpacking
vehicle_model = ('bus', 'train', 'plane') # tuple unpacking


def my_func():
    print(my_dic1['city'])

    for i in my_list:
        print(i)

    for k, v in my_dic.items():
        print(k, v)



if __name__ == '__main__':
    print('This is info.py')
