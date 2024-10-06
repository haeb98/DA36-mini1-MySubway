
from MySubway.user_menu import UserMenu
from MySubway.admin_menu import AdminMenu
from MySubway.repository.user_repo import UserRepo


class LoginMenu:
    admin_id = 'admin'
    admin_password = 'ds36'
    def __init__(self):
        self.result = None
        self.login_id = None
        self.user_menu = UserMenu()
        self.admin_menu = AdminMenu()
        self.user_repo = UserRepo()

        # user_info.pkl에 저장된 유저 정보 중 login_id를 불러옴
        self.user_login_ids = []
        for user_info in self.user_repo.get_user_info():
            user_login_id = user_info.get_login_id()
            self.user_login_ids.append(user_login_id)

    def login(self):
        while True:
            login_id = input('Enter your id: ')

            # 유저로 로그인 시 유저 메뉴로 이동함
            if login_id in self.user_login_ids:
                self.login_id = login_id
                result = self.user_menu.user_menu(login_id)
                return result

            # 어드민으로 로그인 시, 비밀번호 요구하며 어드민 메뉴로 이동함
            elif login_id == self.admin_id:
                password = input('Enter admin password: ')
                if password == self.admin_password:
                    result = self.admin_menu.admin_main()
                    return result
                else:
                    print('❌Passwords do not match')
                    pass

            elif login_id == "end":
                result = 0
                return result

            else:
                print(f'No such user with id "{login_id}"')
                pass

            if self.result == 0:
                break





