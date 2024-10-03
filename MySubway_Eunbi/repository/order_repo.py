
class OrderRepo:
    """주문 저장소 클래스"""
    def __init__(self):
        self.orders = []  # OrderEntity 객체들을 저장할 리스트

    def add_order(self, order):
        """새로운 주문을 저장"""
        self.orders.append(order)

    def get_all_orders(self):
        """저장된 모든 주문을 반환"""
        return self.orders


class Payment:
    """결제 모듈 클래스"""
    #amount는 결제 금액을 나타내는 변수로,
    # order_service.py에서 total_price라는 이름으로 계산된 뒤에
    # Payment 클래스에 전달됨

    def __init__(self, amount):
        self.amount = amount

    def process_card_payment(self):
        print(f"{self.amount} 원이 신용/체크카드로 결제됩니다.")
        print("카드를 삽입하여 주십시오.")
        print("결제가 완료됐습니다.")

    def process_apple_samsung_pay(self):
        print(f"{self.amount}원이 Apple/Samsung Pay로 결제됩니다.")
        print("핸드폰을 가까이 대주세요.")

    def process_mobile_pay(self):
        print(f"{self.amount}원이 모바일 페이로 결제됩니다.")
        print("바코드를 인식시켜 주세요.")

    def select_payment_method(self):
        """결제 방법 선택"""
        print("결제 방법을 선택하세요:")
        print("1. 신용/체크카드")
        print("2. Apple/Samsung Pay")
        print("3. 모바일 페이")

        payment_choice = input("결제 방법의 번호를 입력하세요: ")

        if payment_choice == "1":
            self.process_card_payment()
        elif payment_choice == "2":
            self.process_apple_samsung_pay()
        elif payment_choice == "3":
            self.process_mobile_pay()
        else:
            print("잘못된 선택입니다.")
            self.select_payment_method()
