
class AdminMenu:
    def __init__(self):
        self.order_service = None

    def admin_menu(self):
        print('어드민으로 로그인되었습니다')

    def view_order_info(self):
        self.order_service.view_order_info()