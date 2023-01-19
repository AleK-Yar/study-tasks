"""https://stepik.org/lesson/701973/step/5?unit=702074"""


class Goods:  # объявляем класс Goods с атрибутами
    title = 'Мороженое'
    weight = 154
    tp = 'Еда'
    price = 1024


Goods.price = 2048  # меняем атрибут price
setattr(Goods, 'inflation', 100)  # добавляем в класс Goods атрибут inflation
