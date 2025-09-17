# ЛР1

## Лабораторная работа 1

### Задание 1

``name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')``

![01_greeting](/images/01_greeting.png)

### Задание 2

``a = input('a: ').replace(',', '.')
b = input('b: ').replace(',', '.')
a = float(a)
b = float(b)
print(f'sum={"{:.2f}".format(a+b)}; avg={"{:.2f}".format((a+b)/2)}')``

![02_sum_avg](/images/02_sum_avg.png)

### Задание 3

``price = float(input('Цена: '))
discount = float(input('Скидка: '))
vat = float(input('НДС: '))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

text = ['База после скидки:', 'НДС:', 'Итого к оплате:']
nums = ["{:.2f}".format(base), "{:.2f}".format(vat_amount), "{:.2f}".format(total)]

for text, nums in zip(text, nums):
    print(f'{text:<{20}} {nums:>{1}} ₽')``

![03_discount_vat](/images/03_discount_vat.png)

### Задание 4

``mins = int(input('Минуты: '))
hrs = mins//60
mins %= 60
print(f'{hrs}:{mins:02d}')``

![04_minutes_to_hhmm](/images/04_minutes_to_hhmm.png)

### Задание 5

``name = input('ФИО: ')
name = name.split()
initials = [name[i][0] for i in range(len(name))]
initials = ''.join(initials)

name = ' '.join(name)
symbols = len(name)

print(f'Инициалы: {initials}.')
print(f'Длина символов: {symbols}')``

![05_initials_and_len](/images/05_initials_and_len.png)