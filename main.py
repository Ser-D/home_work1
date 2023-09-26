import os


    
# def find_it(seq):
#     for i in seq:
#         print(i, seq.count(i) % 2)
#         if seq.count(i) % 2 != 0:
#             print(i, seq.count(i) % 2)
#             return i
            
#     return None

path = input('Введіть шлях до папки, що потребує сортування: ')

if os.listdir(path):
    print(os.listdir(path))
else:
    print("aaa")