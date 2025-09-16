name = input('ФИО: ')
name = name.split()
initials = [name[i][0] for i in range(len(name))]
initials = ''.join(initials)

name = ' '.join(name)
symbols = len(name)

print(f'Инициалы: {initials}.')
print(f'Длина символов: {symbols}')