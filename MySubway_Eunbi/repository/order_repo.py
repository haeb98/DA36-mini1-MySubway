import time

# from MySubway.service.order_service import OrderService
# from MySubway.entity.order_entity import OrderEntity, Orde

import pickle
from MySubway_Eunbi.entity.order_entity_eunbi import OrderEntity, OrderNo

class OrderRepo:
    """주문 저장소 클래스"""
    def __init__(self, orders):
        self.orders = []

        try:
            with open('orders.pkl', 'rb') as f:
                self.orders = pickle.load(f)

            if len(self.orders) > 0:
                self.next_order_no = self.orders[-1] + 1
            else:
                self.next_order_no = 1

        except (FileNotFoundError, EOFError):
            self.next_order_no = 1

    def save_orders(self):
        with open('order.pkl', 'wb') as f:
            pickle.dump(self.orders, f)

    def load_orders(self):
        with open('orders.pkl', 'rb') as f:
            return pickle.load(f)

    def add_order(self, order):
        """새로운 주문을 저장"""
        self.orders.append(order)
        print(self.orders)
        self.save_orders()

    def select_payment_method(self):
        """결제 방법 선택"""
        payment_method_str = '''
======Processing payment=======
1. 신용/체크카드
2. Apple/Samsung Pay
3. 모바일 페이
==============================='''
        while True:
            print("결제 방법을 선택하세요.")
            print(payment_method_str)
            payment_choice = input("> Enter number: ")

            if payment_choice == "1":
                print("신용/체크카드를 삽입하여 주십시오.")
                print('...')
                time.sleep(2)
                print('결제가 완료되었습니다')
            elif payment_choice == "2":
                print("핸드폰을 가까이 대주세요.")
                print('...')
                time.sleep(2)
                print('결제가 완료되었습니다')
            elif payment_choice == "3":
                print("바코드를 인식시켜 주세요.")
                print('...')
                time.sleep(2)
                print('결제가 완료되었습니다')
            else:
                print("잘못된 선택입니다.")
                pass
            break


    def get_all_orders(self):
        """저장된 모든 주문을 반환"""
        return self.orders

# class Payment:
#     """결제 모듈 클래스"""
#     #amount는 결제 금액을 나타내는 변수로,
#     # order_service.py에서 total_price라는 이름으로 계산된 뒤에
#     # Payment 클래스에 전달됨
#
#     def __init__(self):
#
#     def select_payment_method(self):
#         """결제 방법 선택"""
#         print("결제 방법을 선택하세요:")
#         print("1. 신용/체크카드")
#         print("2. Apple/Samsung Pay")
#         print("3. 모바일 페이")
#
#         payment_choice = input("결제 방법의 번호를 입력하세요: ")
#
#         if payment_choice == "1":
#             print("신용/체크카드를 삽입하여 주십시오.")
#         elif payment_choice == "2":
#             print("핸드폰을 가까이 대주세요.")
#         elif payment_choice == "3":
#             print("바코드를 인식시켜 주세요.")
#         else:
#             print("잘못된 선택입니다.")
#             return

    # def process_card_payment(self):
    #     # print(f"{self.amount} 원이 신용/체크카드로 결제됩니다.")
    #     print("신용/체크카드를 삽입하여 주십시오.")
    #     print("결제가 완료됐습니다.")
    #
    # def process_apple_samsung_pay(self):
    #     # print(f"{self.amount}원이 Apple/Samsung Pay로 결제됩니다.")
    #     print("핸드폰을 가까이 대주세요.")
    #
    # def process_mobile_pay(self):
    #     # print(f"{self.amount}원이 모바일 페이로 결제됩니다.")
    #     print("바코드를 인식시켜 주세요.")

