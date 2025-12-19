# Python. ООП ч.2
#
# Задача №1 (Тема: ООП часть 2. Раздел: Наследование)
# Создай родительский класс Vehicle (Транспортное средство) с конструктором __init__, который принимает один параметр:
# brand (марка, строка)
# и создаёт атрибут self.brand.
# Создай дочерний класс Car (Автомобиль), который:
# Наследуется от Vehicle
# В своём конструкторе __init__ принимает два параметра:
# brand (марка) — должен передаваться в родительский конструктор
# doors (количество дверей, целое число) — создаётся как атрибут объекта
# Создай объект класса Car с параметрами: brand="Toyota", doors=4.
# Выведи на экран оба атрибута этого объекта: марку и количество дверей.
    # class Vehicle:
    #     def __init__(self, brand):
    #         self.brand = brand
    # class Car(Vehicle):
    #     def __init__(self, brand, doors):
    #         super().__init__(brand)
    #         self.doors = doors
    # car1 = Car(brand="Toyota", doors=4)
    # print(car1.brand, car1.doors)

# Задача №2 (Тема: ООП часть 2. Раздел: Наследование)
# Создай родительский класс Animal (Животное) с методом speak(), который возвращает строку "Животное издает звук".
# Создай два дочерних класса, которые наследуются от Animal:
# Dog (Собака) — переопределяет метод speak(), чтобы он возвращал строку "Гав-гав!".
# Cat (Кошка) — переопределяет метод speak(), чтобы он возвращал строку "Мяу!".
# Создай по одному объекту каждого дочернего класса:
# dog = Dog()
# cat = Cat()
# Выведи на экран результат вызова метода speak() для каждого объекта (каждый результат с новой строки).
    # class Animal():
    #     def __init__(self, name, age):
    #         self.name = name
    #         self.age = age
    #     def speak(self):
    #         return "Животное издает звук"
    # class Dog(Animal):
    #     def speak(self):
    #         return "Гав-гав!"
    # class Cat(Animal):
    #     def speak(self):
    #         return "Мяу!"
    # dog = Dog("Tuzik", "5")
    # cat = Cat("Ryzhiy", "3")
    # print(dog.speak())
    # print(cat.speak())

# Задача №3 (Тема: ООП часть 2. Раздел: Наследование)
# Создай родительский класс Person (Человек) с конструктором __init__, который принимает:
# name (имя, строка)
# age (возраст, целое число)
# и создаёт соответствующие атрибуты объекта.
# Создай дочерний класс Student (Студент), который:
# Наследуется от Person
# В своём конструкторе __init__ принимает три параметра:
# name (должен передаваться в родительский конструктор)
# age (должен передаваться в родительский конструктор)
# student_id (номер студенческого билета, строка) — новый атрибут
# # Добавь в класс Student метод get_info(), который возвращает строку в формате:
# # "Студент: {name}, Возраст: {age}, ID: {student_id}"
# Создай объект класса Student с параметрами: name="Алексей", age=20, student_id="S12345".
# Выведи на экран результат вызова метода get_info() для этого объекта.
    # class Person:
    #     def __init__(self, name, age):
    #         self.name = name
    #         self.age = age
    # class Student(Person):
    #     def __init__(self, name, age, student_id):
    #         super().__init__(name, age)
    #         self.student_id = student_id
    #     def get_info(self):
    #         return f'Студент: {self.name}, Возраст: {self.age}, ID: {self.student_id}'
    # student1 = Student(name="Алексей", age=20, student_id="S12345")
    # print (student1.get_info())
