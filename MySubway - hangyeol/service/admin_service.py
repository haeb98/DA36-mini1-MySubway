from repository.admin_repo import AdminRepo
from repository.user_repo import UserRepo
from entity.user_entity import UserEntity
# from entity.order_entity import OrderNo

class AdminService:

    def __init__(self) :
        self.admin_repo = AdminRepo()
        self.sales_data = []
        self.user_repo = UserRepo()
        # self.order_no = OrderNo()

    def add_user(self, user_id=None, login_id=None, user_name=None, user_gender=None, user_birth=None, my_menu=None):

        if user_id is None:
            user_id = UserEntity.next_id
        if my_menu is None:
            my_menu = []
        user = UserEntity(user_id, login_id, user_name, user_gender, user_birth, my_menu)
        self.user_repo.add_user(user)

    def delete_user(self, user_id):
        delete = self.user_repo.delete_user(user_id)
        if delete:
            print(f'{user_id}번 회원 정보를 삭제했습니다.')
        else:
            print(f'{user_id}번 회원은 존재하지 않습니다.')

    def get_user_info(self):
        return self.user_repo.get_all_user_info()

    def find_by_id(self, user_id):
        return self.user_repo.find_by_user_id(user_id)

    def update_user_info(self, user_id, updated_info):
        return self.user_repo.update_user(user_id, updated_info)

    ###################################################################
    # 얘네는 오더가 피클파일에 저장이 돼야 만들 수가 있네..
    # def view_orders(self):
    #     pass
    #
    # def today_sales(self):
    #     order_no = self.order_no.generate_order_no()
    #     order_date = order_no[:8]