"""https://stepik.org/lesson/701973/step/11?unit=702074"""


class Person:  # объявляем класс Person с атрибутами
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()  # создаём экземпляр класса

print('job' in p1.__dict__)  # проверяем наличие локального свойства job в экземпляре класса
