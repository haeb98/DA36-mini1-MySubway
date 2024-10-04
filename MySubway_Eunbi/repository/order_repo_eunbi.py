import pickle
import time

# from MySubway.service.order_service import OrderService
from MySubway.entity.order_entity import OrderEntity, OrderNo
from MySubway_Eunbi.service.order_service_eunbi import OrderService

class OrderRepo:
    """주문 저장소 클래스"""
    def __init__(self):
        self.orders = []  # OrderEntity 객체들을 저장할 리스트

    def save_orders(self):
        with open('order.pkl', 'wb') as f:
            pickle.dump(self.orders, f)

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

###########################################

    # def view_order_info(self):
    #     order_info = OrderService.view_order_info()

    def view_order_info(self):
        order_info = OrderService.view_order_info()
        if not self.orders:
            print("저장된 주문이 없습니다.")
            return

        print(f"=== 저장된 주문 {len(self.orders)}건 ===")
        for order in self.orders:
            print(f"주문번호: {order.order_no}")
            print(f"총 금액: {order.total_price}")
            print(f"사용자 ID: {order.user_id}")
            print(f"주문한 메뉴: {[item.get_sandwich()._MenuSelection__name for item in order.cart]}")
            print("-" * 30)

