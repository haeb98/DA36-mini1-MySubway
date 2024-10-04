
import datetime

class OrderEntity:
    def __init__(self, order_no, total_price, user_id, cart):
        self.order_no = order_no  # 주문번호
        self.total_price = total_price  # 총 금액
        self.user_id = user_id  # 사용자 ID
        self.cart = cart

class OrderNo:
    """주문번호"""
    def __init__(self):
        self.current_date = None  # 주문번호 생성된 현재 날짜 저장
        self.counter = 1  # 각 날짜별로 주문번호를 001부터 시작

    def generate_order_no(self):
        """주문번호를 날짜와 함께 생성"""
        today = datetime.datetime.now().strftime("%Y%m%d")

        if self.current_date != today:
            # 날짜가 바뀌면 카운터는 001로 초기화 함
            self.current_date = today
            self.counter = 1

        #주문번호 생성 (ex. 20241003001)
        order_no = int(f"{self.current_date}{self.counter:03d}")
        return order_no

    def increment_counter(self):
        """결제가 완료되면 카운터를 1씩 증가"""
        self.counter += 1
