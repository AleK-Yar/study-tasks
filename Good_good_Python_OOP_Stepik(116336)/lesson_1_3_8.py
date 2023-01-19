"""https://stepik.org/lesson/701973/step/8?unit=702074"""


class Dictionary:  # объявляем класс Dictionary с атрибутами
    rus = 'Питон'
    eng = 'Python'


print(getattr(Dictionary, 'rus_word', False))  # выводим значение атрибута rus_word, если его нет выводи False
