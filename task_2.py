# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина *
# масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
# Проверить работу метода. Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width * .01

    def mass(self):
        return self._length * self._width


class Roadmass(Road):
    def __init__(self, _length, _width, masum, thickness):
        super().__init__(_length, _width)
        self.masum = masum * .1
        self.thickness = thickness

    def summass(self):
        return self._length * self._width * self.masum * self.thickness


r = Roadmass(20, 5000, 25, 5)
print(f'Масса асфальтного покрытия = {int(r.summass())} т.')
