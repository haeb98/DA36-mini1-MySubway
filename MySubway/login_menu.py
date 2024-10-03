from service.login_service import LoginService
from user_menu import UserMenu
from admin_menu import AdminMenu


class LoginMenu:
    my_login_id = ['sample', 'sample2', 'sample3']
    # my_password = 'password'
    admin_id = 'admin'
    # admin_password = 'password'
    def __init__(self):
        self.login_service = LoginService()
        self.user_menu = UserMenu()
        self.admin_menu = AdminMenu()

    def login(self):
        while True:
            login_id = input('Enter your id: ')
            # password = input('Enter your password:')

            if login_id in self.my_login_id:
                self.user_menu.user_menu()

            elif login_id == self.admin_id:
                self.admin_menu.admin_menu()

            else:
                print(f'No such user with id "{login_id}"')
                pass


