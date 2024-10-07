from MySubway.entity.menu_entity import MenuOption, MenuSelection
from MySubway.repository.user_repo import UserRepo


class MenuRepo:
    sandwich_dict = {
        1: MenuSelection(1, 'sandwich', '에그마요(Egg Mayo)', 5_000),
        2: MenuSelection(2, 'sandwich', '비엘티(B.L.T.)',6_000),
        3: MenuSelection(3, 'sandwich', '이탈리안 비엠티(ltalian B.M.T.)',6_500),
        4: MenuSelection(4, 'sandwich', '스파이시 이탈리안(Spicy ltalian)',6_500),
        5: MenuSelection(5, 'sandwich', '치킨 데리야끼(Chicken Teriyaki)', 6_500)
    }

    # sandwich_list = ['에그마요(Egg Mayo)', '비엘티(B.L.T.)', '이탈리안 비엠티(ltalian B.M.T.)', '스파이시 이탈리안(Spicy ltalian)',
    #                     '치킨 데리야끼(Chicken Teriyaki)', '써브웨이 클럽(Subway Club)', '폴드 포크 바비큐(Pulled Pork Barbecue)',
    #                     'K-바비큐(K-BBQ)', '로티세리 바비큐 치킨(Rotisserie Barbecue Chicken)']
    # sandwich_dict = {i + 1: sandwich for i, sandwich in enumerate(sandwich_list)}

    # bread_list = ['화이트(White Bread)', '파마산 오레가노(Parmesan Oregano)', '위트(Whole Wheat)', '허니 오트(Honey Oat)', '하티(Hearty)',
    #               '플랫 브레드(Flat Bread)']
    # bread_dict = {i + 1: bread for i, bread in enumerate(bread_list)}
    # print(bread_dict)
    bread_dict = {
        1: MenuOption(1, 'bread','화이트' ),
        2: MenuOption(2, 'bread', '파마산 오레가노'),
        3: MenuOption(3, 'bread', '위트'),
        4: MenuOption(4, 'bread', '허니 오트'),
        5: MenuOption(5, 'bread', '하티'),
        6: MenuOption(6, 'bread', '플랫 브레드')
    }

    # cheese_list = ['아메리칸 치즈(American Cheese)', '슈레드 치즈(Shredded Cheese)', '모차렐라 치즈(Mozzarella Cheese)', '치즈 제외']
    # cheese_dict = {i + 1: cheese for i, cheese in enumerate(cheese_list)}
    cheese_dict = {
        1: MenuOption(1, 'cheese', '아메리칸 치즈'),
        2: MenuOption(2, 'cheese', '슈레드 치즈'),
        3: MenuOption(3, 'cheese', '모차렐라 치즈'),
        4: MenuOption(4, 'cheese', '치즈 제외')
    }

    # veggies_list = ['양상추', '토마토', '오이', '피망', '양파', '피클', '올리브', '할라피뇨', '모두 넣기', '모두 빼기']
    # veggies_dict = {i + 1: veggies for i, veggies in enumerate(veggies_list)}
    veggies_dict = {
        1: MenuOption(1, 'veggies', '양상추'),
        2: MenuOption(2, 'veggies', '토마토'),
        3: MenuOption(3, 'veggies', '오이'),
        4: MenuOption(4, 'veggies', '피망'),
        5: MenuOption(5, 'veggies', '양파'),
        6: MenuOption(6, 'veggies', '피클'),
        7: MenuOption(7, 'veggies', '올리브'),
        8: MenuOption(8, 'veggies', '할라피뇨'),
        9: MenuOption(9, 'veggies', '모두 넣기'),
        10: MenuOption(10, 'veggies', '모두 빼기')
    }

    # sauce_list = ['랜치(Ranch)', '스위트 어니언(Sweet Onion)', '마요네즈(Mayonnaise)', '스위트 칠리(Sweet Chill)', '스모크 바비큐(Smoked BBQ)',
    #               '핫 칠리(Hot Chill)', '허니 머스타드(Honey Mustard)', '사우스웨스트 치폴레(Southwest Chipotle)', '홀스래디쉬(Horseradish)',
    #               '머스타드(Mustard)', '올리브 오일(Olive oil)', '레드와인 식초(Red wine vinegar)', '소금(salt)', '후추(pepper)', '소스 제외']
    # sauce_dict = {i + 1: sauce for i, sauce in enumerate(sauce_list)}
    sauce_dict = {
        1: MenuOption(1, 'sauce', '랜치'),
        2: MenuOption(2, 'sauce', '스위트 어니언'),
        3: MenuOption(3, 'sauce', '스위트 칠리'),
        4: MenuOption(4, 'sauce', '사우스웨스트 치폴레'),
        5: MenuOption(5, 'sauce', '홀스래디쉬'),
        6: MenuOption(6, 'sauce', '올리브 오일'),
        7: MenuOption(7, 'sauce', '레드와인 식초'),
        8: MenuOption(8, 'sauce', '소금'),
        9: MenuOption(9, 'sauce', '후추'),
        10: MenuOption(10, 'sauce', '소스 제외')
    }

    def __init__(self):
        self.cart = []
        self.user_repo = UserRepo()

    def add_to_cart(self, selected_menu):
        self.cart.append(selected_menu)
        return self.cart

    def my_menu(self,login_id):
        user_id = self.user_repo.find_user_id_by_login_id(login_id)
        info = self.user_repo.find_by_user_id(user_id)
        my_menu_info = info.get_my_menu()
        return my_menu_info
