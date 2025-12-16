#Задача 1 (Наследование).

#Создайте базовый (родительский) класс с именем Animal. У этого класса должен быть конструктор __init__, который принимает один аргумент (после self) — name (имя животного) и сохраняет его в атрибут объекта.

#У класса Animal должен быть метод с именем speak(), который выводит на экран строку: "[name] издает звук.".

#Затем создайте дочерний класс с именем Dog, который наследуется от класса Animal. В этом классе переопределите метод speak(), чтобы он выводил строку: "[name] гавкает.".

#После создания классов:

#Создайте объект родительского класса Animal с именем "Неизвестное животное" и вызовите его метод speak().

#Создайте объект дочернего класса Dog с именем "Барсик" и вызовите его метод speak().

#Ваша задача — написать код: оба класса, их методы, создание объектов и вызов методов.

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} издает звук.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} гавкает.")

my_animal = Animal("Неизвестное животное")
my_animal.speak()
my_dog = Dog("Барсик")
my_dog.speak()

#Задача 2 (Наследование).

#Создайте базовый (родительский) класс с именем Vehicle (Транспортное средство). У этого класса должен быть конструктор __init__, который принимает два аргумента (после self):

#brand (марка транспортного средства)

#max_speed (максимальная скорость)

#и сохраняет их в атрибуты объекта.

#У класса Vehicle должен быть метод с именем info(), который выводит на экран строку: "Марка: [brand], Макс. скорость: [max_speed] км/ч.".

#Затем создайте дочерний класс с именем Car, который наследуется от класса Vehicle. В классе Car:

#Добавьте новый атрибут в конструктор — doors (количество дверей). Конструктор должен принимать три аргумента: brand, max_speed, doors.

#Переопределите метод info(), чтобы он выводил строку: "Марка: [brand], Макс. скорость: [max_speed] км/ч, Двери: [doors].".

#После создания классов, создайте объект дочернего класса Car с аргументами "Toyota", 200 и 4. Вызовите у этого объекта метод info().

#Ваша задача — написать код: оба класса, их методы, создание объекта Car и вызов метода.

class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed
    def info(self):
        print(f"Марка: {self.brand}, Макс. скорость: {self.max_speed} км/ч.")

class Car(Vehicle):
    def doors(self,doors,brand, max_speed):
        self.doors = doors
        self.brand = brand
        self.max_speed = max_speed
    def info(self):
        print(f"Марка: {self.brand}, Макс. скорость: {self.max_speed} км/ч, Двери: {self.doors}.")

my_car = Car("Toyota", 200, 4)
my_car.info()
#Хорошее начало, но есть ключевая ошибка в понимании конструктора дочернего класса.

#В дочернем классе Car:

#Не нужно создавать отдельный метод doors. Атрибут doors должен добавляться в конструктор __init__ класса Car.

#Конструктор дочернего класса Car должен:

#Принимать аргументы для всех атрибутов (brand, max_speed, doors).

#Вызывать конструктор родительского класса Vehicle, чтобы инициализировать унаследованные атрибуты (brand, max_speed). Это делается с помощью super().__init__(brand, max_speed).

#Инициализировать свой собственный атрибут self.doors.

#Исправь класс Car: добавь ему конструктор __init__, который вызывает родительский конструктор и создает атрибут doors.

#дай решение
#Решение задачи 2 (Наследование).

#Вот корректный код для обоих классов:

python
class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed
    def info(self):
        print(f"Марка: {self.brand}, Макс. скорость: {self.max_speed} км/ч.")

class Car(Vehicle):
    def __init__(self, brand, max_speed, doors):
        super().__init__(brand, max_speed)
        self.doors = doors
    def info(self):
        print(f"Марка: {self.brand}, Макс. скорость: {self.max_speed} км/ч, Двери: {self.doors}.")

my_car = Car("Toyota", 200, 4)
my_car.info()

#Задача 3 (Наследование).

#Создайте базовый (родительский) класс с именем Employee (Сотрудник). У этого класса должен быть конструктор __init__, который принимает два аргумента (после self):

#name (имя сотрудника)

#salary (зарплата)
#и сохраняет их в атрибуты объекта.

#У класса Employee должен быть метод с именем show_info(), который выводит на экран строку: "Сотрудник: [name], Зарплата: [salary] руб.".

#Затем создайте дочерний класс с именем Manager, который наследуется от класса Employee. В классе Manager:

#Добавьте новый атрибут в конструктор — department (отдел). Конструктор должен принимать три аргумента: name, salary, department.

#Переопределите метод show_info(), чтобы он выводил строку: "Менеджер: [name], Зарплата: [salary] руб., Отдел: [department].".

#После создания классов, создайте объект родительского класса Employee с аргументами "Иван" и 50000. Вызовите его метод show_info().

#Затем создайте объект дочернего класса Manager с аргументами "Анна", 80000 и "Продажи". Вызовите его метод show_info().

#Ваша задача — написать код: оба класса, их методы, создание объектов и вызов методов.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def show_info(self):
        print(f"Сотрудник: {self.name}, Зарплата: {self.salary} руб.")

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
    def show_info(self):
        print(f"Менеджер: {self.name}, Зарплата: {self.salary} Отдел: {self.department}.")
my_employee = Employee("Иван", 50000)
my_employee.show_info()
my_manager = Manager("Анна", 80000, "Продажи")
my_manager.show_info()

#Задача 4 (Наследование).

#Создайте базовый (родительский) класс с именем Shape (Фигура). У этого класса должен быть метод с именем area(), который просто возвращает число 0.

#Затем создайте дочерний класс с именем Rectangle (Прямоугольник), который наследуется от класса Shape. В классе Rectangle:

#Добавьте конструктор __init__, который принимает два аргумента (после self): width (ширина) и height (высота), и сохраняет их в атрибуты объекта.

#Переопределите метод area(), чтобы он вычислял и возвращал площадь прямоугольника по формуле: width * height.

#После создания классов, создайте объект класса Rectangle с аргументами 5 и 3. Вызовите у этого объекта метод area(), сохраните результат в переменную и выведите её на экран.

#Ваша задача — написать код: оба класса, их методы, создание объекта и вызов метода.

class Shap:
    def area(self):
        return 0
class Rectangle(Shap):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
my_rectangle = Rectangle(5, 3)
result = my_rectangle.area()
print(result)
#Код почти идеален! Есть лишь небольшая опечатка в названии родительского класса: Shap вместо Shape. Исправь это, и задача будет решена безупречно.

class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
my_rectangle = Rectangle(5, 3)
result = my_rectangle.area()
print(result)