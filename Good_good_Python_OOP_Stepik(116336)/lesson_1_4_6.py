"""https://stepik.org/lesson/701974/step/6?unit=702075"""


class Graph:  # объявляем метод Graph с атрибутом
    LIMIT_Y = [0, 10]

    def set_data(self, data):  # объявляем метод для формирования локального свойства data
        self.data = data

    def draw(self):  # объявляем метод для вывода чисел из списка локального свойства data
                     # входящих в диапазон указанный в атрибутах класса
        print(*[d for d in self.data if min(self.LIMIT_Y) <= d <= max(self.LIMIT_Y)])


graph_1 = Graph()  # создаём экземпляр класса
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])  # вызываем метод set_data и передаем ему список
graph_1.draw()  # вызываем метод draw
