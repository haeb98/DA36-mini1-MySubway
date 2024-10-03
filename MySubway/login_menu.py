from service.login_service import LoginService
from user_menu import UserMenu
from admin_menu import AdminMenu


class LoginMenu:
    user_login_id = ['sample', 'sample2', 'sample3']
    # user_password = 'password'
    admin_id = 'admin'
    admin_password = 'ds36'
    def __init__(self):
        self.login_service = LoginService()
        self.user_menu = UserMenu()
        self.admin_menu = AdminMenu()

    def login(self):
        while True:
            login_id = input('Enter your id: ')

            if login_id in self.user_login_id:
                self.user_menu.user_menu()

            elif login_id == self.admin_id:
                password = input('Enter admin password: ')
                if password == self.admin_password:
                    self.admin_menu.admin_menu()
                else:
                    return

            else:
                print(f'No such user with id "{login_id}"')
                pass


