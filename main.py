x = bool(input('Введите значение X:'))
y = bool(input('Введите значение Y:'))
z = bool(input('Введите значение Z:'))

a = not (x or y or z)
b = not x and not y and not z
if a == b:
    print('Истина')
else:
    print('Ложь')
