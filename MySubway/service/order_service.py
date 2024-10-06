
from MySubway.entity.order_entity import OrderEntity, OrderNo  # 절대 경로
from MySubway.repository.order_repo import OrderRepo # 절대 경로

class OrderService:
    """주문 및 결제 처리 서비스 클래스"""
    def __init__(self):
        self.order_no = OrderNo()
        self.order_repo = OrderRepo()

    def order_now(self, user, cart):
        """장바구니 항목을 불러와서 주문 처리. user랑 cart는 호출 시에만 전달됨"""
        total_price = 0
        # 장바구니에 담긴 item에 대하여 총 결제금액 계산
        for item in cart:
            total_price += item.get_sandwich()._MenuSelection__price
        print(f"💲총 결제 금액: {total_price}원")

        # 주문번호 생성
        order_no = self.order_no.generate_order_no()
        self.order_no_up()
        print(f"🧾주문 번호: {order_no}")
        print("🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒🛒")

        # TODO 주문 리스트에 담기
        order = OrderEntity(order_no, total_price, user, cart)
        self.select_payment_method()
        self.add_order(order) # repo.orders에 order를 추가하고, pkl 쓰기 작업
        self.reset_cart(cart) #
        return 1

    def add_order(self, order):
        return self.order_repo.add_order(order)

    def reset_cart(self, cart):
        return cart.clear()

    def select_payment_method(self):
        return self.order_repo.select_payment_method()

    def order_no_up(self):
        # 결제가 완료되면 주문번호 카운터 1 증가
        self.order_no.increment_counter()

    def view_order_info(self):
        self.order_repo.view_order_info()