"""https://stepik.org/lesson/701973/step/6?unit=702074"""


class Car:  # объявляем пустой класс Car
    pass


setattr(Car, 'model', 'Тойота')  # добавляем в класс атрибуты
setattr(Car, 'color', 'Розовый')
setattr(Car, 'number', 'П111УУ77')

print(Car.__dict__['color'])  # выводим атрибуты класса Car используя словарь __dict__
