from MySubway.entity.menu_entity import MenuEntity, MenuOption, MenuSelection
from MySubway.repository.menu_repo import MenuRepo
from MySubway.service.menu_service import MenuService
from MySubway.service.order_service import OrderService

# from MySubway.order_menu import OrderMenu

# user_Login_id로 로그인 시 UserMenu 실행
class UserMenu:
    def __init__(self):
        self.menu_service = MenuService()
        self.menu_repo = MenuRepo()

    def user_menu(self):
        print('🏠안녕하세요. MySubway를 방문해주셔서 감사합니다.🏠')
        user_menu_str = '''
=====MySubway Menu=====
1. MyMenu로 주문
2. 새로 주문
0. 되돌아가기
=======================
>Enter number: '''
        choice = int(input(user_menu_str))
        match choice:
            case 1:
                self.menu_service.my_menu()
            case 2:
                while True:
                    selected_menu = self.start_menu()
                    self.print_selected_menu(selected_menu)
                    cart = self.menu_service.add_to_cart(selected_menu)

                    order_more_yn = input("> 추가 주문할 것이 있나요?(y/n) ")
                    if order_more_yn != 'y':
                        print(">>> 결제창으로 넘어갑니다.카트를 확인해주세요")
                        self.print_cart(cart)
                        while True:
                            order_now_yn = input("> 이대로 주문할까요?(y/n) ")
                            if order_now_yn == 'y':
                                order_service = OrderService()
                                result = order_service.order_now(user=self.get_current_user(), cart=cart)
                                self.print_result(result)
                                break
                            else:
                                break

                            # order_menu = OrderMenu(user, cart)
                            # order_menu.display_menu()
            case 0:
                return
            case _:
                print('>>>잘못 입력하셨습니다')
                pass
                
#     bread_str = '''
# 🥖빵을 골라주세요🥖
# 1. 화이트(White Bread
# 2. 파마산 오레가노(Parmesan Oregano
# 3. 위트(Whole Wheat
# 4. 허니 오트(Honey Oat
# 5. 하티(Hearty
# 6. 플랫 브레드(Flat Bread)
# Enter number: '''
    # 메뉴는 어드민에 의해 변경 가능하므로 menu_repo의 dict에서 불러옴
    def generate_menu_str(self, type_dict): #start_menu에서 보여줄 menu_str릏 menu_repo로 부터 불러와서 만듦
        menu_str = ''
        for i, menu in type_dict.items():
            menu_str += f"{i}. {menu.get_item()}\n"
        menu_str += '> Enter number: '
        return menu_str

    def start_menu(self): # 샌드위치, 빵, 치즈, 야채, 소스 순서로 입력받아 selected_menu 출력
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

    def print_selected_menu(self, selected_menu):
        print(f' 🥪샌드위치: {selected_menu.get_sandwich()._MenuSelection__item}\n'
              f' 🥖빵: {selected_menu.get_bread()._MenuOption__item}\n'
              f' 🧀치즈: {selected_menu.get_cheese()._MenuOption__item}\n'
              f' 🥗야채: {selected_menu.get_veggies()._MenuOption__item}\n'
              f' 🧂소스: {selected_menu.get_sauce()._MenuOption__item}\n'
              ' 를 카트에 담았습니다🛒.')

    def print_cart(self, cart):
        print("\n🛒🛒🛒🛒🛒🛒🛒Cart🛒🛒🛒🛒🛒🛒🛒")
        for index, item in enumerate(cart, start=1):
            print( f'{index}. 🥪{item.get_sandwich()._MenuSelection__item}'
                   f' 💲{item.get_sandwich()._MenuSelection__price}원\n'
                   f'(🥖{item.get_bread()._MenuOption__item}, '
                   f'🧀{item.get_cheese()._MenuOption__item}, '
                   f'🥗{item.get_veggies()._MenuOption__item}, '
                   f'🧂{item.get_sauce()._MenuOption__item})')
        print("🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒")

    def get_current_user(self):
        pass

    def print_result(self, result):
        if result > 0:
            print('주문해주셔서 감사합니다. 샌드위치가 만들어질 동안 잠시만 기다려주새요~')
        else:
            print('결제 실패')

