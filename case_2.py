# Стилистическое преобразование чисел:

#print(20,"December", 1988, sep="/")
# Напишите программу, которая запрашивает у пользователя последовательно день его рождения, месяц и год

print("Date")
print(input())
print("Month")
print(input())
print("Year")
print(input())


# Напишите функцию, которая определяет какому дню недели соответствует эта дата?

import datetime 
def day_of_week(year, month, day): 

date = datetime.date(year, month, day)

weekday_num = date.weekday() 

days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
  return days[weekday_num]

year = int(input("Введите год: "))
month = int(input("Введите месяц: "))
day = int(input("Введите день: "))

result = day_of_week(year, month, day)
print(f"Это {result}.")

#создаем функцию, которая принимает три аргумента: год, месяц и день
#создаем объект даты на основе переданных аргументов
#Получаем день недели в числовом формате (0 - понедельник, 6 - воскресенье)




#Напишите функцию, которая определяет сколько сейчас лет пользователю;

def calculate_age(birth_year):
  age = current_year - birth_year
  return age
birth_year = int(input("Введите ваш год рождения: ")) 
current_year = int(input("Введите текущий год"))
your_age = calculate_age(birth_year) 
print("Вам", your_age, "лет")  




#Реализуйте вывод в консоль даты рождения пользователя в формате дд мм гггг, 
# где цифры прорисованы звёздочками (*), как на электронном табло.

def print_digit(digit):
    if digit == 0:
        print("  ***  ")
        print(" *   * ")
        print(" *   * ")
        print(" *   * ")
        print("  ***  ")
    elif digit == 1:
        print("   *   ")
        print("  **   ")
        print(" * *   ")
        print("   *   ")
        print("   *   ")
    elif digit == 2:
        print("  ***  ")
        print("     * ")
        print("  ***  ")
        print(" *     ")
        print("  ***  ")
    elif digit == 3:
        print("  ***  ")
        print("     * ")
        print("  ***  ")
        print("     * ")
        print("  ***  ")
    elif digit == 4:
        print(" *   * ")
        print(" *   * ")
        print("  ***  ")
        print("     * ")
        print("     * ")
    elif digit == 5:
print("  ***  ")
        print(" *     ")
        print("  ***  ")
        print("     * ")
        print("  ***  ")
    elif digit == 6:
        print("  ***  ")
        print(" *     ")
        print("  ***  ")
        print(" *   * ")
        print("  ***  ")
    elif digit == 7:
        print("  ***  ")
        print("     * ")
        print("    *  ")
        print("   *   ")
        print("   *   ")
    elif digit == 8:
        print("  ***  ")
        print(" *   * ")
        print("  ***  ")
        print(" *   * ")
        print("  ***  ")
    elif digit == 9:
        print("  ***  ")
        print(" *   * ")
        print("  ***  ")
        print("     * ")
        print("  ***  ")
    print()  # Пустая строка для разделения цифр

def print_date(day, month, year):
  
    print_digit(day // 10)  # Выводим первую цифру дня
    print_digit(day % 10)  # Выводим вторую цифру дня
    print("  ") # Пробел между днем и месяцем
    print_digit(month // 10)  # Выводим первую цифру месяца
    print_digit(month % 10)  # Выводим вторую цифру месяца
    print("  ") # Пробел между месяцем и годом
    print_digit(year // 1000)  # Выводим первую цифру года
    print_digit(year // 100 % 10)  # Выводим вторую цифру года
    print_digit(year // 10 % 10)  # Выводим третью цифру года
    print_digit(year % 10)  # Выводим четвертую цифру года


day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))
year = int(input("Введите год рождения: "))

print_date(day, month, year)
