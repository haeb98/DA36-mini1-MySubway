from MySubway.entity.menu_entity import MenuEntity, MenuOption, MenuSelection
from MySubway.repository.menu_repo import MenuRepo
from MySubway.service.menu_service import MenuService
from MySubway.service.order_service import OrderService
from MySubway.repository.user_repo import UserRepo


# user_Login_id로 로그인 시 UserMenu 실행
class UserMenu:
    def __init__(self):
        self.menu_service = MenuService()
        self.menu_repo = MenuRepo()
        self.order_service = OrderService()
        self.user_repo = UserRepo()

    def user_menu(self, login_id):
        user_menu_str = '''
=====MySubway Menu=====
1. MyMenu로 주문
2. 새로 주문

0. 종료 하기
=======================
> Enter number: '''
        while True:
            choice = int(input(user_menu_str))
            match choice:
                case 1: #1. MyMenu로 주문
                    my_menu = self.menu_service.my_menu(login_id)
                    self.print_selected_menu(self.my_menu(my_menu))
                    cart = self.my_menu_process(my_menu)
                    if len(cart) == 0:
                        pass
                    else:
                        # 주문완료후 결제
                        print(">>> 결제창으로 넘어갑니다.영수증을 확인해주세요")
                        self.print_cart(cart)
                        # 결제 시작
                        current_user = self.user_repo.find_user_id_by_login_id(login_id)
                        result = self.order_service.order_now(user=current_user, cart=cart)
                        self.print_result(result)


                case 2: #2. 새로 주문
                    cart = self.new_menu_process()
                    # 주문완료후 결제
                    print(">>> 결제창으로 넘어갑니다.영수증을 확인해주세요")
                    self.print_cart(cart)
                    # 결제 시작
                    current_user = self.user_repo.find_user_id_by_login_id(login_id)
                    result = self.order_service.order_now(user=current_user, cart=cart)
                    self.print_result(result)

                case 0:
                    return 0
                case _:
                    print('❌잘못된 입력입니다.')
                    pass
                

    # 메뉴는 어드민에 의해 변경 가능하므로 menu_repo의 dict에서 불러옴
    def generate_menu_str(self, type_dict): #start_menu에서 보여줄 menu_str릏 menu_repo로 부터 불러와서 만듦
        menu_str = ''
        for i, menu in type_dict.items():
            menu_str += f"{i}. {menu.get_item()}\n"
        menu_str += '> Enter number: '
        return menu_str

    def new_menu(self): # 샌드위치, 빵, 치즈, 야채, 소스 순서로 입력받아 selected_menu 출력
        sandwich_str = self.generate_menu_str(self.menu_repo.sandwich_dict)
        bread_str = self.generate_menu_str(self.menu_repo.bread_dict)
        cheese_str = self.generate_menu_str(self.menu_repo.cheese_dict)
        veggies_str = self.generate_menu_str(self.menu_repo.veggies_dict)
        sauce_str = self.generate_menu_str(self.menu_repo.sauce_dict)

        print("=====Processing Order=====")
        sandwich_key = int(input(f'🥪샌드위치를 골라주세요🥪\n{sandwich_str}'))
        bread_key = int(input(f'🥖빵을 골라주세요🥖\n{bread_str}'))
        cheese_key = int(input(f'🧀치즈를 골라주세요🧀\n{cheese_str}'))
        veggies_key = int(input(f'🥗야채를 골라주세요🥗\n{veggies_str}'))
        sauce_key = int(input(f'🧂소스를 골라주세요🧂\n{sauce_str}'))
        print("=========================")
        #TODO 틀린 번호 입력 시 재입력
        selected_menu = MenuEntity(self.menu_repo.sandwich_dict[sandwich_key],
                                   self.menu_repo.bread_dict[bread_key],
                                   self.menu_repo.cheese_dict[cheese_key],
                                   self.menu_repo.veggies_dict[veggies_key],
                                   self.menu_repo.sauce_dict[sauce_key])
        return selected_menu

    def my_menu(self, my_menu):
        sandwich_key = my_menu[0]
        bread_key = my_menu[1]
        cheese_key = my_menu[2]
        veggies_key = my_menu[3]
        sauce_key = my_menu[4]

        selected_menu = MenuEntity(self.menu_repo.sandwich_dict[sandwich_key],
                                   self.menu_repo.bread_dict[bread_key],
                                   self.menu_repo.cheese_dict[cheese_key],
                                   self.menu_repo.veggies_dict[veggies_key],
                                   self.menu_repo.sauce_dict[sauce_key])
        return selected_menu


    def print_selected_menu(self, selected_menu):
        print(f'🥪샌드위치: {selected_menu.get_sandwich()._MenuSelection__item}\n'
              f'🥖빵: {selected_menu.get_bread()._MenuOption__item}\n'
              f'🧀치즈: {selected_menu.get_cheese()._MenuOption__item}\n'
              f'🥗야채: {selected_menu.get_veggies()._MenuOption__item}\n'
              f'🧂소스: {selected_menu.get_sauce()._MenuOption__item}')

    def print_cart(self, cart):
        print("\n🛒🛒🛒🛒🛒🛒🛒Receipt🛒🛒🛒🛒🛒🛒🛒")
        for index, item in enumerate(cart, start=1):
            print( f'{index}. 🥪{item.get_sandwich()._MenuSelection__item}'
                   f' 💲{item.get_sandwich()._MenuSelection__price}원\n'
                   f'(🥖{item.get_bread()._MenuOption__item}, '
                   f'🧀{item.get_cheese()._MenuOption__item}, '
                   f'🥗{item.get_veggies()._MenuOption__item}, '
                   f'🧂{item.get_sauce()._MenuOption__item})')
            print('-----------------------------------')

    def print_result(self, result):
        if result > 0:
            print('주문해주셔서 감사합니다. 샌드위치가 만들어질 동안 잠시만 기다려주세요~')
        else:
            print('결제 실패하였습니다. 다시 결제해주세요')

    def new_menu_process(self):
        while True:
            selected_menu = self.new_menu()
            self.print_selected_menu(selected_menu)
            print('를 카트에 담았습니다🛒.')
            # 선택한 메뉴 카트에 담기
            cart = self.menu_service.add_to_cart(selected_menu)
            # 추가 주문 여부 묻기
            order_more_yn = input("> 추가 주문할 것이 있나요?(y/n) ")
            if order_more_yn != 'y':
                # 주문 완료한 경우
                return cart
            else:
                # 추가주문 하려는 경우
                pass
    def my_menu_process(self, my_menu):
        # print(f'My Menu: {my_menu}')
        # self.print_selected_menu(my_menu)

        order_yn = input("My Menu를 주문하시겠습니까?(y/n) ")
        if order_yn == 'y':
            selected_menu = self.my_menu(my_menu)
            self.print_selected_menu(selected_menu)
            print('를 카트에 담았습니다🛒.')
            # 선택한 메뉴 카트에 담기
            cart = self.menu_service.add_to_cart(selected_menu)
            # 추가 주문 여부 묻기
            order_more_yn = input("> 추가 주문할 것이 있나요?(y/n) ")
            if order_more_yn != 'y': # 주문 완료한 경우
                return cart
            else: # 추가주문 하려는 경우는 새로 주문 프로세스 시작
                cart = self.new_menu_process()
                return cart
        else:
            cart = []
            return cart
