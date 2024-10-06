

class MenuEntity:
    def __init__(self, sandwich, bread, cheese, veggies, sauce):
        self.__sandwich = sandwich
        self.__bread = bread
        self.__cheese = cheese
        self.__veggies = veggies
        self.__sauce = sauce

    def get_sandwich(self):
        return self.__sandwich

    def set_sandwich(self, sandwich):
        self.__sandwich = sandwich

    def get_bread(self):
        return self.__bread

    def set_bread(self, bread):
        self.__bread = bread

    def get_cheese(self):
        return self.__cheese

    def set_cheese(self, cheese):
        self.__cheese = cheese

    def get_veggies(self):
        return self.__veggies

    def set_veggies(self, veggies):
        self.__veggies = veggies

    def get_sauce(self):
        return self.__sauce

    def set_sauce(self, sauce):
        self.__sauce = sauce

    def __repr__(self):
        return (f'sandwich= {self.__sandwich},bread ={self.__bread}'
                f',cheese ={self.__cheese}, veggies ={self.__veggies}, sauce ={self.__sauce}')


class MenuSelection:
    def __init__(self, id, type, item, price):
        self.__id = id
        self.__type = type
        self.__item = item
        self.__price = price

    def get_item(self):
        return self.__item
    def get_price(self):
        return self.__price

class MenuOption:
    def __init__(self, id, type, item):
        self.__id = id
        self.__type = type
        self.__item = item

    def get_item(self):
        return self.__item


