"""https://stepik.org/lesson/701973/step/10?unit=702074"""


class Figure:  # объявляем класс Figure и добавляем два атрибута
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()  # создаём объект класса Figure
fig1.start_pt = (10, 5)  # добавляем локальные атрибуты
fig1.end_pt = (100, 20)
fig1.color = 'blue'

del fig1.color  # удаляем из экземпляра класса атрибут color

print(*fig1.__dict__.keys())  # выводим список свойств, без значений, экземпляра fig1
