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


