class Animal:
    """
    Базовый класс для животных.
    """

    def __init__(self, name: str, age: int):
        """
        Инициализация животного.
        :param name: Имя животного
        :param age: Возраст животного
        """
        self._name = name
        self.age = age

    def make_sound(self) -> str:
        """
        Метод, который должен быть реализован в дочерних классах.
        :return: строка, представляющая звук животного
        """
        return "Some sound"

    def __str__(self) -> str:
        return f"Животное {self._name}, возраст {self.age} лет"

    def __repr__(self) -> str:
        return f"Animal(name={self._name!r}, age={self.age!r})"


class Dog(Animal):
    """
    Дочерний класс для собаки.
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Инициализация собаки.
        :param name: Имя собаки
        :param age: Возраст собаки
        :param breed: Порода собаки
        """
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self) -> str:
        """
        Переопределение метода make_sound, так как собаки лают.
        :return: Звук, который издает собака
        """
        return "гав"

    def __str__(self) -> str:
        return f"Собака {self._name}, порода {self.breed}, возраст {self.age} лет"

    def __repr__(self) -> str:
        return f"Dog(name={self._name!r}, age={self.age!r}, breed={self.breed!r})"


class Cat(Animal):
    """
    Дочерний класс для кошки.
    """

    def __init__(self, name: str, age: int, color: str) -> None:
        """
        Инициализация кошки.
        :param name: Имя кошки
        :param age: Возраст кошки
        :param color: Цвет шерсти
        """
        super().__init__(name, age)
        self.color = color

    def make_sound(self) -> str:
        """
        Переопределение метода make_sound, так как кошки мяукают.
        :return: Звук, который издает кошка
        """
        return "мяу"

    def __str__(self) -> str:
        return f"Кошка {self._name}, цвет {self.color}, возраст {self.age} лет"

    def __repr__(self) -> str:
        return f"Cat(name={self._name!r}, age={self.age!r}, color={self.color!r})"


if __name__ == "__main__":
    dog = Dog("Рекс", 3, "Овчарка")
    cat = Cat("Барски", 2, "Черный")

    print(dog)
    print(cat)

    print(dog.make_sound())
    print(cat.make_sound())
