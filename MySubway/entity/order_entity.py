
import datetime
from MySubway.repository.order_repo import OrderRepo

class OrderEntity:
    def __init__(self, order_no, total_price, user_id, cart):
        self.order_no = order_no  # 주문번호
        self.total_price = total_price  # 총 금액
        self.user_id = user_id  # 사용자 ID
        self.cart = cart

    def get_order_no(self):
        return self.order_no
    def get_total_price(self):
        return self.total_price
    def get_user_id(self):
        return self.user_id
    def get_cart(self):
        return self.cart

class OrderNo:
    def __init__(self):
        self.counter = None
        self.order_repo = OrderRepo()

    def generate_order_no(self):
        today = datetime.datetime.now().strftime("%Y%m%d")
        order_no_list = []

        for order in self.order_repo.orders:
            order_no_list.append(order.get_order_no())

        if order_no_list:
            last_order_no = order_no_list[-1]
        else:
            last_order_no = None

        if  last_order_no is None or (str(last_order_no))[:8] != today:
            self.counter = 1
        else:
            self.counter = int((str(last_order_no))[8:]) + 1

        #주문번호 생성 (ex. 20241003001)
        order_no = int(f"{today}{self.counter:03d}")
        return order_no

    def increment_counter(self):
        self.counter += 1
