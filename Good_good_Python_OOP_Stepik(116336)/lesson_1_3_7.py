"""https://stepik.org/lesson/701973/step/7?unit=702074"""


class Notes:  # объявляем класс Notes с атрибутами
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2


print(getattr(Notes, 'author'))  # выводим значение атрибута author
