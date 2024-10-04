# Реализуйте класс House, объекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
# Объект этого класса должен обладать следующими атрибутами:
# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        list_ = []
        for i in range(1, self.number_of_floors + 1):
            list_.append(i)
        if new_floor in list_:
            for j in range(1, new_floor + 1):
                if j != new_floor:
                    print(j)
                else:
                    print(f'Приехали на {new_floor} этаж {self.name}')
                    print()
        else:
            print(f'В {self.name},такого этажа не существует')


dom1 = House('ЖК Эльбрус', 30)
dom2 = House('ЖК Уют', 10)

House.go_to(dom1, 31)
House.go_to(dom2, 0)

print()
print(f'{dom1.name}, количество этажей: {dom1.number_of_floors}')
print(f'{dom2.name}, количество этажей: {dom2.number_of_floors}')
