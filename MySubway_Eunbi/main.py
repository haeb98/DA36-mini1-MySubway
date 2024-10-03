'''
요구사항

'''
from login_menu import LoginMenu
from order_menu import OrderMenu

def run_program():
    while True: # 로그인 후 장바구니 화면에서 '주문취소' 누르면 메인 화면으로 돌아올 수 있도록 함.
        # 로그인
        login_menu = LoginMenu().login()
        user = login_menu.get_user()
        print("오늘도 Subway를 이용해주셔서 감사합니다.")

        # 팀원이 제공할 Cart
        cart = []

        # 주문 메뉴 실행
        order_menu = OrderMenu(user, cart)
        order_menu.display_menu()


if __name__ == '__main__':
    # 로그인 화면으로 돌아가는 흐름 유지
    run_program()





