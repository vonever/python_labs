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