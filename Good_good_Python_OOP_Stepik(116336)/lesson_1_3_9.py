"""https://stepik.org/lesson/701973/step/9?unit=702074"""


class TravelBlog:  # объявляем класс TravelBlog с атрибутом total_blogs
    total_blogs = 0


tb1 = TravelBlog()  # создаём экземпляр класса
tb1.name = 'Франция'  # задаём экземпляру два локальных свойства
tb1.days = 6
setattr(TravelBlog, 'total_blogs', 1)  # устанавливаем значение атрибута total_blogs

tb2 = TravelBlog()  # создаём экземпляр класса
tb2.name = 'Италия'  # задаём экземпляру два локальных свойств
tb2.days = 5
TravelBlog.total_blogs += 1  # увеличиваем атрибут total_blogs на единицу
