# OP01.1 Создать калькулятор — программу, в которой мы вводим 2 числа, и с ними производятся сразу все математические действия, рассмотренные в уроке. 

def operation():
  print("Выберите операцию:")
  print("1. Сложение")
  print("2. Вычитание")
  print("3. Умножение")
  print("4. Деление")
  choice = input("Введите выбор (1/2/3/4): ")
  return choice

def calc():
  num1 = float(input("Введите 1ое число: "))
  num2 = float(input("Введите 2ое число: "))
  choice = operation()
  if choice == '1':
      return num1 + num2
  elif choice == '2':
      return num1 - num2
  elif choice == '3':
      return num1 * num2
  elif choice == '4':
    if num2 == 0:
        return "Error: Division by zero is not allowed, Деление на ноль"
    else:
            return num1/num2
  else:
      return "Error: Invalid operation"

def run():
  while True:
      print(calc())
      cont = input("Продолжим? (yes/no): ")
      if cont.lower() != 'yes':
          break

run()