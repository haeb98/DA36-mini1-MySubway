# from user import User  # 나중에 팀원이 작성할 user 모듈을 import
# from cart import Cart  # 나중에 팀원이 작성할 cart 모듈을 import
from MySubway_Eunbi.entity.order_entity import OrderEntity, OrderNo  # 절대 경로
from MySubway_Eunbi.repository.order_repo import OrderRepo, Payment  # 절대 경로
# from repository import order_repo
# from entity import order_entity

class OrderService:
    """주문 및 결제 처리 서비스 클래스"""
    def __init__(self):
        self.order_no_generator = OrderNo()

    def order_now(self, user, cart):
        """장바구니 항목을 불러와서 주문 처리. user랑 cart는 호출 시에만 전달됨"""
        print("주문 확인:")
        total_price = 0
        for i, item in enumerate(cart, 1):
            print(f"{i}. 메뉴: {item['menu']} | 가격: {item['price']}원 | 수량: {item['quantity']}")
            total_price += item['price'] * item['quantity']

        print(f"총 결제 금액은 {total_price}원 입니다.")

        # 주문번호 생성
        order_no = self.order_no_generator.generate_order_no()
        print(f"주문번호: {order_no}")

        # 주문 저장
        order_entity_obj = OrderEntity(order_no, total_price, user.get_user_id())
        order_repo = OrderRepo()
        order_repo.add_order(order_entity_obj)

        # 결제 진행
        amount = total_price
        payment = Payment(amount) #생성자에 amount 전달
        payment.select_payment_method()

        # 결제가 완료되면 주문번호 카운터 1 증가
        self.order_no_generator.increment_counter()

