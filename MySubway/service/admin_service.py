from MySubway.repository.order_repo import OrderRepo
from MySubway.repository.user_repo import UserRepo
from MySubway.entity.user_entity import UserEntity

class AdminService:
    def __init__(self):
        self.user_repo = UserRepo()
        self.order_repo = OrderRepo()

    def add_user(self, user_id=None, login_id=None, user_name=None, user_gender=None, user_birth=None, my_menu=None):

        if user_id is None:
            user_id = UserEntity.next_id
        if my_menu is None:
            my_menu = []
        user = UserEntity(user_id, login_id, user_name, user_gender, user_birth, my_menu)
        return self.user_repo.add_user(user)

    def delete_user(self, user_id):
        result  = self.user_repo.delete_user(user_id)
        return result

    def update_user_info(self, user_id, updated_info):
        return self.user_repo.update_user(user_id, updated_info)

    def get_user_info(self):
        return self.user_repo.get_all_user_info()

    def find_by_user_id(self, user_id):
        return self.user_repo.find_by_user_id(user_id)


    def total_sales(self, input_date):
        orders = self.order_repo.get_all_orders()
        sales_of_date_list = []
        for order in orders:
            order_no = order.get_order_no()
            n = len(input_date)
            if str(order_no)[:n] ==input_date:
                sales_of_date_list.append(order.get_total_price())
            if not sales_of_date_list:
                raise ValueError(f'"{input_date}"에 해당하는 주문이 없습니다.')
        return sales_of_date_list




