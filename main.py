#------------------1----------------------
class Lightbulb:
    def __init__(self, bulb_type: str, base_size: str, year: int, lifespan: int):
        self.bulb_type = bulb_type  # тип лампочки
        self.base_size = base_size  # размер цоколя
        self.year = year  # год выпуска
        self.lifespan = lifespan  # ожидаемый ресурс работы в часах
        self.is_on = False  # начальное состояние лампочки (выключена)

    def toggle(self):
        #переключает состояние лампочки
        self.is_on = not self.is_on #тип меняем на противоположное
        state = "включена" if self.is_on else "выключена"
        print(f"Лампочка {state}.")

    def __str__(self):
        #возвращает строковое представление информации о лампочке
        state = "включена" if self.is_on else "выключена"
        return (f"Тип: {self.bulb_type}, Размер цоколя: {self.base_size}, Год выпуска: {self.year}, "
                f"Ресурс: {self.lifespan} часов, Состояние: {state}")



bulb = Lightbulb("Светодиодная", "E27", 2023, 15000)
print(bulb)  # вывод информации о лампочке
bulb.toggle()  # включение лампочки
print(bulb)  # вывод обновленной информации
bulb.toggle()  # выключение лампочки
print(bulb)  # вывод обновленной информации

print()
print()


#-------------------2--------------------
class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            #выдаем ошибку и останавливаем программу
            raise ValueError("Знаменатель не может быть равен нулю")
        self.numerator = numerator
        self.denominator = abs(denominator)  # тк знаменатель всегда натуральное число
        if denominator < 0:
            self.numerator = -self.numerator  # делаем чтоб минус был в числителе а не в знаменателе
        self.sokrashenie()

    def nod(self, a: int, b: int):
        # aлгоритм Евклида для нахождения НОД
        while b:
            a, b = b, a % b
        return abs(a)

    def sokrashenie(self):
        #cокращает дробь
        nod = self.nod(abs(self.numerator), self.denominator)
        self.numerator //= nod
        self.denominator //= nod

    def __str__(self):
        #возвращает строковое представление дроби
        return f"{self.numerator}/{self.denominator}"

    #название этих математические операторы можно найти в инете
    def __add__(self, other):
        #cложение дробей
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        #вычитание дробей
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        #yмножение дробей
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        # деление дробей
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __neg__(self):
        # нахождение противоположного числа
        return Fraction(-self.numerator, self.denominator)

    def __eq__(self, other):
        # сравнение на равенство
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        # меньше
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        # меньше или равно
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __float__(self):
        # приведение к float
        return self.numerator / self.denominator

    def __int__(self):
        # приведение к int
        return self.numerator // self.denominator


f1 = Fraction(3, 4)
f2 = Fraction(2, 5)
print(f"f1: {f1}, f2: {f2}")
print(f"Сложение: {f1 + f2}")
print(f"Вычитание: {f1 - f2}")
print(f"Умножение: {f1 * f2}")
print(f"Деление: {f1 / f2}")
print(f"Противоположное число f1: {-f1}")
print(f"Сравнение f1 < f2: {f1 < f2}")
print(f"Приведение f1 к float: {float(f1)}")
print(f"Приведение f1 к int: {int(f1)}")


print()
print()


#-------------------3--------------------
class Vehicle:
    def __init__(self, wheels: int, max_speed: int, model: str):
        self.wheels = wheels
        self.max_speed = max_speed
        self.model = model

    def __str__(self):
        return f"Модель: {self.model}, Кол-во колёс: {self.wheels}, Макс. скорость: {self.max_speed} км/ч"


class Truck(Vehicle):#в скобках пишем то от чего наследуемся
    #наследование это значит какие методы были в классе от которого наследуемся
    # то такие же будут и в классе в который наследуем
    def __init__(self, wheels: int, max_speed: int, model: str, load_capacity: float):
        super().__init__(wheels, max_speed, model)
        self.load_capacity = load_capacity  # грузоподъёмность

    def __str__(self):
        return (f"Грузовик: {self.model}, Кол-во колёс: {self.wheels}, "
                f"Макс. скорость: {self.max_speed} км/ч, Грузоподъёмность: {self.load_capacity} т")



tractor = Vehicle(4, 200, "blue tractor")
truck = Truck(6, 120, "6 колесный гелик", 25)

print(tractor)
print(truck)



print()
print()


#-------------------4--------------------
import math


class Number:
    def __init__(self, value: float):
        self._value = value

    def __mul__(self, other):
        #смотрим чтобы вторая переменная была какие то числом
        if isinstance(other, (int, float)):
            return Number(self._value * other)
        raise TypeError("Умножение возможно только на число")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль невозможно")
            return Number(self._value / other)
        raise TypeError("Деление возможно только на число")

    def get_value(self):
        return self._value


class Circle(Number):
#добавилось двойное нижнее подчеркивание в название переменной
#изза этого она теперь считается приватной и мы не сможешь вывести ее без класса для вывода
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.__radius = radius

    def set_radius(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def circumference(self):
        return 2 * math.pi * self.__radius




num = Number(10)
circle = Circle(5)

print(f"Число: {num.get_value()}")
print(f"Радиус круга: {circle.get_radius()}")
print(f"Площадь круга: {circle.area()}")
print(f"Длина окружности: {circle.circumference()}")

circle.set_radius(7)
print(f"Новый радиус: {circle.get_radius()}")


try:
    print(circle.__radius)  # Ошибка, так как __radius теперь скрыт
except AttributeError:
    print("Ошибка: Доступ к радиусу напрямую запрещён")


print()
print()


#-------------------5--------------------
#перепишем задание 2 и просто добавим обработку ошибок
class FractionError(Exception):
    #просто добавляем ошибку чтобы вывводить потом ее
    # в скобках получаем сообщение(ну тип ошибку) которое надо будет вывести в консоль
    def __init__(self, message):
        super().__init__(message)

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Числитель и знаменатель должны быть целыми числами")
        if denominator == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю")
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        self.numerator = numerator
        self.denominator = denominator
        self.sokrashenie()

    def nod(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def sokrashenie(self):
        nod = self.nod(abs(self.numerator), self.denominator)
        self.numerator //= nod
        self.denominator //= nod

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise FractionError("Можно складывать только объекты типа Fraction")
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise FractionError("Можно вычитать только объекты типа Fraction")
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise FractionError("Можно умножать только объекты типа Fraction")
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise FractionError("Можно делить только объекты типа Fraction")
        if other.numerator == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        if not isinstance(other, Fraction):
            raise FractionError("Можно сравнивать только объекты типа Fraction")
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        if not isinstance(other, Fraction):
            raise FractionError("Можно сравнивать только объекты типа Fraction")
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return self.numerator // self.denominator



#трай тип пытаемся выполнить но если выдаст ошибку то мы словим ее и выведем в консоль
try:
    f1 = Fraction(3, 4)
    f2 = Fraction(2, 5)
    print(f"f1: {f1}, f2: {f2}")
    print(f"Сложение: {f1 + f2}")
    print(f"Вычитание: {f1 - f2}")
    print(f"Умножение: {f1 * f2}")
    print(f"Деление: {f1 / f2}")
    print(f"Противоположное число f1: {-f1}")
    print(f"Сравнение f1 < f2: {f1 < f2}")
    print(f"Приведение f1 к float: {float(f1)}")
    print(f"Приведение f1 к int: {int(f1)}")
    f3 = Fraction(5, 0)  # проверка исключения деления на ноль
except FractionError as fe: # ошибка которую мы сами создали и сможем теперь ловить
    print("Ошибка (FractionError):", fe)
except ZeroDivisionError as zde: # встроенная ошибка
    print("Ошибка (ZeroDivisionError):", zde)
except Exception as e: # ловим другие, неизвестные нам ошибки
    print("Неизвестная ошибка:", e)
