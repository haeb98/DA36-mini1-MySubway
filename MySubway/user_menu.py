from MySubway.entity.menu_entity import MenuEntity, MenuOption, MenuSelection
from MySubway.repository.menu_repo import MenuRepo
from MySubway.service.menu_service import MenuService


class UserMenu:
    def __init__(self):
        self.menu_service = MenuService()
        self.menu_repo = MenuRepo()

    def user_menu(self):
        print('안녕하세요. MySubway를 방문해주셔서 감사합니다.')
        user_menu_str = '''
=====MySuby Menu=====
1. MyMenu로 주문
2. 새로 주문
0. 되돌아가기
=====================
Enter number: '''
        choice = int(input(user_menu_str))
        match choice:
            case 1:
                self.menu_service.my_menu()
            case 2:
                selected_menu = self.start_menu()
                cart = self.menu_service.add_to_cart(selected_menu)
                # print(result[0].get_selected_menu_name())
                self.print_cart(cart)
            case 0:
                return
            case _:
                print('잘못 입력하셨습니다')
                pass
                

    def start_menu(self):
        print('> 주문을 시작합니다')
        sandwich_key = int(input("num: "))#TODO MenuRepo에서 불러와서 메뉴 출력
        bread_key = int(input("num: "))
        cheese_key = int(input("num: "))
        veggies_key = int(input("num: "))
        sauce_key = int(input("num: "))
        selected_menu = MenuEntity(self.menu_repo.sandwich_dict[sandwich_key],
                                   self.menu_repo.bread_dict[bread_key],
                                   self.menu_repo.cheese_dict[cheese_key],
                                   self.menu_repo.veggies_dict[veggies_key],
                                   self.menu_repo.sauce_dict[sauce_key])
        return selected_menu

    def print_cart(self, cart):
        for item in cart:
            print( f'{item.get_sandwich()._MenuSelection__item}\n'
                   f' 빵: {item.get_bread()._MenuOption__item}\n'
                   f' 치즈: {item.get_cheese()._MenuOption__item}\n'
                   f' 야채: {item.get_veggies()._MenuOption__item}\n'
                   f' 소스: {item.get_sauce()._MenuOption__item}\n'
                   f' 가격: {item.get_sandwich()._MenuSelection__price}'
                   '가 카트에 추가되었습니다')
