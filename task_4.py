# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} Машина поехала'

    def stop(self):
        return f'{self.name} Машина остановилась'

    def turn_left(self):
        return f'{self.name} Машина повернула на лево '

    def turn_right(self):
        return f'{self.name} Машина повернула на право '

    def show_speed(self):
        return f'Текущая скорость автомобиля  {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, collor, name, is_police):
        super().__init__(speed, collor, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобила равна {self.name} is {self.speed}')
        if self.speed > 60:
            return f'Скорость {self.name} привышена'
        else:
            return f'Скорость у {self.name} оптимальная для города'


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, collor, name, is_police):
        super().__init__(speed, collor, name, is_police)

    def policecar(self):
       pass


class WorkCar(Car):
    def __init__(self, speed, collor, name, is_police):
        super().__init__(speed, collor, name, is_police)

    def show_speed(self):
        print(f'Скорость автомобила равна {self.name} равна {self.speed}')
        if self.speed > 40:
            return f'Скорость {self.name} привышена'
        else:
            return f'Скорость у {self.name} оптимальная для города'


carsport = SportCar(200, 'Синий', 'carsport', True)
cartown = TownCar(40, 'Красный', 'cartown', False)
karwork = WorkCar(65, 'Зеленый', 'karwork', True)
carpolice = PoliceCar(200, 'Черно-белый', 'Police', False)

print(karwork.turn_right())
print(carsport.stop())
print(carsport.show_speed())
print(carpolice.show_speed())
print(cartown.go())
print(cartown.show_speed())
print(f'{cartown.name} окрашена в {cartown.color} цвет')
# ну и все в таком духе. вот.