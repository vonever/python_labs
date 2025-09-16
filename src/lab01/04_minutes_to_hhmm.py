mins = int(input('Минуты: '))
hrs = mins//60
mins %= 60
print(f'{hrs}:{mins:02d}')