## Лабораторная работа 1

### Задание 1

```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```

![01_greeting](/images/01_greeting.png)

### Задание 2

```python
a = input('a: ').replace(',', '.')
b = input('b: ').replace(',', '.')
a = float(a)
b = float(b)
print(f'sum={"{:.2f}".format(a+b)}; avg={"{:.2f}".format((a+b)/2)}')
```

![02_sum_avg](/images/02_sum_avg.png)

### Задание 3

```python
price = float(input('Цена: '))
discount = float(input('Скидка: '))
vat = float(input('НДС: '))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

text = ['База после скидки:', 'НДС:', 'Итого к оплате:']
nums = ["{:.2f}".format(base), "{:.2f}".format(vat_amount), "{:.2f}".format(total)]

for text, nums in zip(text, nums):
    print(f'{text:<{20}} {nums:>{1}} ₽')
```

![03_discount_vat](/images/03_discount_vat.png)

### Задание 4

```python
mins = int(input('Минуты: '))
hrs = mins//60
mins %= 60
print(f'{hrs}:{mins:02d}')
```

![04_minutes_to_hhmm](/images/04_minutes_to_hhmm.png)

### Задание 5

```python
name = input('ФИО: ')
name = name.split()
initials = [name[i][0] for i in range(len(name))]
initials = ''.join(initials)

name = ' '.join(name)
symbols = len(name)

print(f'Инициалы: {initials}.')
print(f'Длина символов: {symbols}')
```

![05_initials_and_len](/images/05_initials_and_len.png)


## Лабораторная работа 2

### Задание 1

```python
def min_max(n):
    n_sort = list()
    if len(min_max_l) == 0:
        raise ValueError('ValueError')
    else:
        for item in n:
            if '-' in item:
                item1 = item[1:]
            else:
                item1 = item
            if item1.isdigit():
                n_sort.append(int(item))
            else:
                n_sort.append(float(item))
    res = (min(n_sort), max(n_sort))
    return res

def unique_sorted(n):
    n_sort = list()
    for item in n:
        if '-' in item:
            item1 = item[1:]
        else:
            item1 = item
        if item1.isdigit():
            n_sort.append(int(item))
        else:
            n_sort.append(float(item))
    res = sorted(set(n_sort))
    return res

def flatten(n):
    n_flat = list()
    for item in n:
        if not isinstance(item, (list, tuple)):
            raise TypeError("строка не строка строк матрицы")
        if len(item) > 0:
            for i in range(len(item)):
                n_flat.append(item[i])
    return n_flat
    


#min_max
min_max_l = list(map(str, input('min_max: ').split()))
try:
    min_max_res = min_max(min_max_l)
    print(min_max_res)
except ValueError as e:
    print(e)

#unique_sorted
unique_sorted_l = list(map(str, input('unique_sorted: ').split()))
unique_sorted_res = unique_sorted(unique_sorted_l)
print(unique_sorted_res)

#flatten
flat1 = [[1, 2], [3, 4]]
flat2 = ([1, 2], (3, 4, 5))
flat3 = [[1], [], [2, 3]]
flat4 = [[1, 2], "ab"]
#выбираем любой из вариантов
print(f'flatten: {flat4}')
try:
    print(flatten(flat4))
except TypeError as e:
    print(f'TypeError: {e}')
```

![01_arrays_test1](/images/01_arrays_test1.png)

![01_arrays_test2](/images/01_arrays_test2.png)

![01_arrays_test3](/images/01_arrays_test3.png)

![01_arrays_test4](/images/01_arrays_test4.png)