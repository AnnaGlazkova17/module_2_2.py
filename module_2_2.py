first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second == third: # проверка на равенство 3 чисел
    print('3')
elif third == second or third == first or second == first: # проверка по парам на равенство
    print('2')
else:
    print('0') # выводим ноль, если нет равных значений

