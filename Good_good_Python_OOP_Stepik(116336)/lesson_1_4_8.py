"""https://stepik.org/lesson/701974/step/8?unit=702075"""


import sys


class StreamData:   # здесь объявляется класс StreamData
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):  # Если кол-во элементов fields и lst_values равны то
            for field, value in zip(fields, lst_values):    # локальные свойства экз-ра класса будут создоваться
                setattr(self, field, value)                 # из эл-тов fields и lst_values
            # self.__dict__ = dict(zip(fields, lst_values))  # локальные свойства экз-ра класса будут создоваться
                                                             # из эл-тов fields и lst_values и устан. в  self.__dict__
                return True
        return False


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        # lst_in = ['10', 'Питон - основы мастерства', '512']
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()   # создается экземпляр sd класса StreamData и он ссылается на локальные сво-ва self.__dict__
        res = sd.create(self.FIELDS, lst_in)    # переменная res ссылается на True либо False
        return sd, res   # создается кортедж. tuple(sd, res). Возвращает tuple[0] = sd который ссылается
                         # на локальные сво-ва self.__dict__ экземпляра sd класса StreamData,
                         # Возвращает tuple[1] = True либо False


sr = StreamReader()   # создается экземпляр sr класса StreamReader
data, result = sr.readlines()   # Из sr.readlines() вернеться ссылка на кортеж. data будет ссылаться на tuple[0]
                                # result будет ссылаться на tuple[1]

# print(data, result)
