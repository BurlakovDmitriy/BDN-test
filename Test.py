
### Задача 1. Переменные и типы данных
# 1\. Создайте переменную `number` со значением 42.
# 2\. Преобразуйте её в строку и сохраните в переменную `number_str`.
# 3\. Создайте переменную `text` со значением "The answer is: ".
# 4\. Объедините строку `text` и строку `number_str` и сохраните результат в переменную `result`.
# 5\. Выведите на экран:
# \- значение и тип данных `number`,
# \- значение и тип данных `number_str`,
# \- значение и тип данных `text`,
# \- значение и тип данных `result`.

# number = 42
# number_str = str(number)
# text = "The answer is: "
# result = text + number_str
# print(number, type(number))
# print(number_str, type(number_str))
# print(text, type(text))
# print(result, type(result))

# ### Задача 2. Строки
# Даны две переменные:
# name = "внесите ваше имя сюда"
# age = введите ваш возраст.
# Используя f-строку, выведите на экран сообщение: "Меня зовут ваше имя, мне ваш возраст лет."

# name = "Дмитрий"
# age = 41
# print (f'Меня зовут {name}, мне {age} лет.')

# ### Задача 3. Списки
# Дан список my_list = [1, 2, 3].
# Создайте копию этого списка, измените первый элемент копии на 10 и выведите оба списка.

# my_list = [1, 2, 3]
# copy_my_list = my_list.copy()
# copy_my_list[0] = 10
# print(my_list)
# print(copy_my_list)

# ### Задача 4. Условные операторы
# Напишите программу, которая принимает число от пользователя и проверяет:
# - Если число больше 0, выведите "Положительное".
# - Если число равно 0, выведите "Ноль".
# - Если число меньше 0, выведите "Отрицательное".

# x = int(input("Введите число:"))
# if x > 0:
#     print(f'Положительное')
# elif x == 0:
#     print(f'Ноль')
# elif x < 0:
#     print(f'Отрицательное')



# ### Задача 5. Словари
# Дан словарь:
# person = {
#       "name": {
#           "first_name": "Иван",
#           "last_name": "Иванов"
# },
#    "address": {
#        "city": "Москва",
#       "country": "Россия"
#     }
# }
# Обновите значение ключа "city" на "Санкт-Петербург" и добавьте новый ключ "postal_code" со значением "333777" в словарь "address".
# Выведите значение через print.
# Затем удалите ключ "city" из вложенного словаря "address" и снова выведите значение через print.

# person = {
#       "name": {
#           "first_name": "Иван",
#           "last_name": "Иванов"
#       },
#    "address": {
#        "city": "Москва",
#       "country": "Россия"
#    }
# }
# person["address"]["city"] = "Санкт-Петербург"
# person["address"]["postal_code"] = "333777"
# print(person["address"])
# del person["address"]["postal_code"]
# print(person["address"])

### Задача 6. Циклы
# Напишите цикл while, который выводит числа от 1 до 20, но пропускает числа, которые делятся на 4 (используйте continue)



# ### Задача 7. Файлы
# Создайте файл с именем "fruits.txt" и запишите в него названия фруктов:
# "яблоко", "банан", "апельсин" (каждое с новой строки).
# Затем откройте этот файл, прочитайте все строки и выведите на экран только те строки, которые начинаются с буквы "а".

# with open("fruits.txt","w" ) as fruits:
#     fruits.write("яблоко")
#     fruits.write("банан")
#     fruits.write("апельсин")


# ### Задача 8. Функции
# Напишите функцию greet_user, которая приветствует пользователя в зависимости от его роли и имени. Функция должна принимать два параметра:
# user_role (обязательный) — строка, указывающая роль пользователя (например, "Администратор", "Гость", "Модератор").
# user_name (необязательный) — строка с именем пользователя. По умолчанию должно быть None.
# Логика работы функции:
# - Если имя пользователя передано (user_name не None и не пустая строка), функция должна вывести: "Привет, {user_name}! Ваша роль: {user_role}."
# - Если имя не передано (user_name равно None или пустая строка), функция должна вывести: "Привет, Гость! Ваша роль: {user_role}."


# def great_user(user_role, user_name):
#     if user_name == True and user_role == True:
#         print(f'Привет, {user_name}! Ваша роль: {user_role}.")
#     elif user_name == False:
#         print ())

### Задача 9. ООП ч.1
# Создайте класс `Student`.
# У класса должны быть атрибуты `name`  и `age`, которые задаются при создании объекта через конструктор `__init__`.
# Создай объект класса `Student` с вашим именем и вашим возрастом.
# Выведи на экран имя и возраст студента.

# class Student():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# student1 = Student("Дмитрий", 41)
# print(student1.name)
# print(student1.age)

### Задача 10. ООП ч.2
# Создайте класс Animal с атрибутами:
# name (кличка животного)
# species (вид животного, например "собака")
# И методами:
# eat()
# sleep()
# Затем создайте дочерний класс Dog, который:
# Наследует все от класса Animal
# Имеет дополнительный метод bark() (лаять)
# Задание:
# - Создайте объект my_dog класса Dog с любым именем
# - Вызовите все три метода eat(), sleep(), bark() и выведите результаты

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def eat(self):
        return "Животное ест"
    def sleep(self):
        return "Животное спит"
class Dog(Animal):
        def bark():
            return "Животное делает Гав-Гав"
my_dog = Dog("Dog", "Tuz")
my_dog.eat()
my_dog.sleep()
my_dog.bark()
print(my_dog.eat())
print(my_dog.sleep())
print(my_dog.bark())

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} eat")

    def sleep(self):
        print(f"{self.name} sleep")

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def bark(self):
        print("woof woof!")

my_dog = Dog("Sharik", "Dachshund")
my_dog.eat()
my_dog.sleep()
my_dog.bark()

