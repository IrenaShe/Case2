#Напишите функцию, которая определяет сколько сейчас лет пользователю;

def calculate_age(birth_year):
  age = current_year - birth_year
  return age
birth_year = int(input("Введите ваш год рождения: ")) 
current_year = int(input("Введите текущий год"))
your_age = calculate_age(birth_year) 
print("Вам", your_age, "лет")  
