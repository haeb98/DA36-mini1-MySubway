from MySubway.service.order_service import OrderService  # 절대 경로
# from MySubway.user_menu import UserMenu

class OrderMenu:
    """주문 메뉴 클래스"""
    def __init__(self, user, cart):
        self.user = user
        self.cart = cart

    def display_menu(self):
        """주문 메뉴를 화면에 표시"""
        print("1. 결제 하기")
        print("0. 되돌아가기")

        choice = input("Enter number: ")

        if choice == '1':
            order_service = OrderService()
            order_service.order_now(self.user, self.cart)
            print("결제가 완료되었습니다. 메인 화면으로 돌아갑니다.")
            return  # 결제 후 메인 while 루프로 복귀(로그인창)

        elif choice == '2':
            print("주문이 취소되었습니다.")
            return  # 취소 시에도 메인 while 루프로 복귀(로그인창)