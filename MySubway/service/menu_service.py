from MySubway.repository.menu_repo import MenuRepo


class MenuService:
    def __init__(self):
        self.menu_repo = MenuRepo()

    def my_menu(self, login_id):
        print('=====Displaying MyMenu=====')
        return self.menu_repo.my_menu(login_id)

    def add_to_cart(self, selected_menu):
        return self.menu_repo.add_to_cart(selected_menu)