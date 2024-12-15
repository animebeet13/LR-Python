import doctest


class Car:
    def __init__(self, brand, max_speed):
        """
        Создание и подготовка к работе объекта "Машина"

        :param brand: Марка машины
        :param max_speed: Максимально развиваемая скорость

        Примеры:
        >>> car = Car("Mercedes", 300) # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError ("Марка машины должна быть типа str")
        if not isinstance(max_speed, (int, float)):
            raise TypeError ("Максимально развиваемая скорость машины должна быть типа int или float")
        if max_speed<0:
            raise ValueError ("Максимально развиваемая скорость машины должна быть больше нуля")
        self.brand=brand
        self.max_speed=max_speed
    def is_car_cool(self):
        """
        Функция которая проверяет является ли машина крутой

        :return: Является ли машина крутой

        Примеры:
        >>> car = Car("Mercedes", 300)
        >>> car.is_car_cool()
        """
        ...
    def is_car_fast(self):
        """
        Функция которая проверяет является ли машина быстрой

        :return: Является ли машина быстрой

        Примеры:
        >>> car = Car("Lada", 150)
        >>> car.is_car_fast()
        """
        ...

class Socks:
    def __init__(self, l_or_r, color):
        """
        Создание и подготовка к работе объекта "Носок"

        :param l_or_r: Левый или правый носок
        :param color: Цвет носка

        Примеры:
        >>> sock = Socks("Left", "white") # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет носка должен быть типа str")
        self.l_or_r=l_or_r
        self.color=color
    def sock_for_washing(self):
        """
        Функция которая проверяет был ли нососк в стирке

        :return: Был ли нососк в стирке

        Примеры:
        >>> sock = Socks("Left", "white")
        >>> sock.sock_for_washing()
        """
        ...
    def est_li_para(self):
        """
        Функция проверяет есть ли пара для носка

        :return: Есть ли пара для носка

        Примеры:
        >>> sock = Socks("Left", "white")
        >>> sock.est_li_para()
        """
        ...

class Pen:
    def __init__(self, number, color):
        """
        Создание и подготовка к работе объекта "Ручка"

        :param number: Количество ручек
        :param color: Цвет ручки

        Примеры:
        >>> pen = Pen(2, "blue") # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет ручки должен быть типа str")
        if not isinstance(number, int):
            raise TypeError("Количество ручек должно быть типа int")
        if number<0:
            raise ValueError("Количество ручек должно быть больше нуля")
        self.number=number
        self.color=color
    def pen_for_ege(self):
        """
        Функция проверяет подходит ли ручка для ЕГЭ

        :return: Подходит ли ручка для ЕГЭ

        Примеры:
        >>> pen = Pen(2, "black")
        >>> pen.pen_for_ege()
        """
        ...
    def enough(self):
        """
        Функция проверяет, хватит ли ручек на весь день

        :return: Хватит ли ручек на весь день

        Примеры:
        >>> pen = Pen(2, "black")
        >>> pen.enough()
        """
        ...
# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
