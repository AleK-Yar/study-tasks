"""https://stepik.org/lesson/701974/step/5?unit=702075"""


class MediaPlayer:  # объявляем класс MediaPlayer

    def open(self, file):  # объявляем метод с локальным свойством filename
        self.filename = file

    def play(self):  # объявляем метод для "воспроизведения" файла
        print(f'Воспроизведение {self.filename}')


media1 = MediaPlayer()  # создаем экземпляр класса
media2 = MediaPlayer()  # создаем экземпляр класса

media1.open("filemedia1")  # вызываем метод open с аргументом "filemedia1"
media2.open("filemedia2")  # вызываем метод open с аргументом "filemedia2"

media1.play()  # вызываем метод play для экземпляра media1
media2.play()  # вызываем метод play для экземпляра media2
