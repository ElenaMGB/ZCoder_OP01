# 4. Площадь прямоугольника. 
# Написать программу, которая будет запрашивать у пользователя длину и ширину прямоугольника, а затем вычислять площадь.
# lengh=int(input("Введите длину прямоугольника: "))
# width=int(input("Введите ширину прямоугольника: "))            
# print(f"Площадь прямоугольника: {lengh*width}")
                                 
# 5. Написать конвертер валюты. Эта программа будет конвертировать введённую пользователем сумму в другую валюту. Курс валюты можно ввести самостоятельно и один раз.

#   Чтобы курс валюты был настоящий и самостоятельно обновлялся, также можно использовать ChatGPT.

# Ввод курса валюты
base_currency = input("Введите основную валюту (например, RUR): ")
target_currency = input("Введите валюту, в которую хотите конвертировать (например, EUR, USD): ")
base_rate = float(input(f"Введите курс {base_currency} за 1 {target_currency} (например, 89.02): "))

# Функция для конвертации валют
def convert_currency(amount, base_currency, target_currency, base_rate):
    if base_currency == target_currency:
        return amount
    else:
        return amount / base_rate

# Ввод суммы для конвертации
amount = float(input(f"Введите сумму {base_currency} для конвертации в {target_currency}: "))

# Конвертация суммы
converted_amount = convert_currency(amount, base_currency, target_currency, base_rate)

print(f"{amount} {base_currency} равно {converted_amount} {target_currency}")