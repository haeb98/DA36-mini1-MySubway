from MySubway.service.login_service import LoginService
from MySubway.user_menu import UserMenu
from MySubway.admin_menu import AdminMenu
from MySubway.repository.user_repo import UserRepo


class LoginMenu:
    # user_login_id = ['sample', 'sample2', 'sample3']
    # user_password = 'password'
    admin_id = 'admin'
    admin_password = 'ds36'
    def __init__(self):
        self.login_id = None
        self.login_service = LoginService()
        self.user_menu = UserMenu()
        self.admin_menu = AdminMenu()
        self.user_repo = UserRepo()

        self.user_login_ids = []
        for info in self.user_repo.get_user_info():
            user_login_id = info.get_login_id()
            self.user_login_ids.append(user_login_id)

    def login(self):
        while True:
            login_id = input('Enter your id: ')

            if login_id in self.user_login_ids:
                self.login_id = login_id
                self.user_menu.user_menu(login_id)

            elif login_id == self.admin_id:
                password = input('Enter admin password: ')
                if password == self.admin_password:
                    self.admin_menu.admin_main()
                else:
                    return

            else:
                print(f'No such user with id "{login_id}"')
                pass


