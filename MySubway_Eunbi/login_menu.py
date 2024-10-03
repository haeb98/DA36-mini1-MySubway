from service.login_service import LoginService
from user_menu import UserMenu
from admin_menu import AdminMenu


class LoginMenu:
    my_login_id = 'sample'
    my_password = 'password'
    admin_id = 'admin'
    admin_password = 'password'
    def __init__(self):
        self.login_service = LoginService()
        self.user_menu = UserMenu()
        self.admin_menu = AdminMenu()

    def login(self):

        login_id = input('Enter your id: ')
        password = input('Enter your password: ')

        if login_id == self.my_login_id and password == self.my_password:
            self.user_menu.user_menu()

        elif login_id == self.admin_id and password == self.admin_password:
            self.admin_menu.admin_menu()

        else:
            print('Wrong id or password!')
            pass


