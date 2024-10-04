'''
요구사항

'''
from login_menu import LoginMenu
from repository.user_repo import UserRepo


if __name__ == '__main__':
    login_menu = LoginMenu().login()
    print("오늘도 Subway를 이용해주셔서 감사합니다.")

