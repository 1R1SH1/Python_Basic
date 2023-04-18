class Property():
    tax = 0

    def __init__(self, __worth):
        self.worth = __worth

    def __str__(self):
        return '{}:\n-Стоимость равняется: {}.\n-Налог на соответствующее имущество {}'

    def get_tax(self):
        return round(self.worth / self.tax, 2)
        pass


class Apartment(Property):
    tax = 1000

    def __str__(self):
        return super().__str__().format('Апартаменты', self.worth, self.get_tax())


class Car(Property):
    tax = 200

    def __str__(self):
        return super().__str__().format('Машина', self.worth, self.get_tax())


class CountryHouse(Property):
    tax = 500

    def __str__(self):
        return super().__str__().format('Дача', self.worth, self.get_tax())


apartment = Apartment(int(input('Введите стоимость квартиры: ')))
car = Car(int(input('Введите стоимость машины: ')))
country_house = CountryHouse(int(input('Введите стоимость дачи: ')))
money = int(input('Cколько у вас есть денег: '))
print(apartment)
print(car)
print(country_house)
sum_tax = round(sum(i_property.get_tax() for i_property in (apartment, car, country_house)))
if sum_tax > money:
    print('Вам не хватает', abs(sum_tax - money))
else:
    print('Собственных средств хватит на покрытие налогов')
