first=input('Введи первое число: ')
second=input('Введи второе число: ')
third=input('Введи третье число: ')
if first==second and first==third:
    print('3')
elif first==second or first==third or second==third:
    print(2)
else: print(0)



