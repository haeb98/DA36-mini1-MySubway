import pickle
import os
from MySubway.entity.user_entity import UserEntity

class UserRepo:
    def __init__(self):
        self.user_info = []
        self.load_user_info()

    def get_user_info(self):
        return self.user_info

    def load_user_info(self, filename='user_info.pkl'):
        path = os.path.join(os.path.dirname(__file__), filename)
        with open(path, 'rb') as f:
            self.user_info = pickle.load(f)

            if len(self.user_info) > 0:
                UserEntity.next_id = self.user_info[-1].get_user_id() + 1

            # print("user_info.pkl이 로드되었습니다.")

    def add_user(self,user_info):
        self.user_info.append(user_info)
        self.save_user()

    def save_user(self): #TODO 닫을 때마다 dump 하게끔 수정 필요
        with open('user_info.pkl', 'wb') as f:
            pickle.dump(self.user_info, f)

    def delete_user(self, user_id):
        user_id = int(user_id)
        len_user_info = len(self.user_info)
        self.user_info = [user for user in self.user_info if user.get_user_id() != user_id]
        if len(self.user_info) < len_user_info:
            self.save_user()
            return True
        else:
            return False


    def update_user(self, user_id, updated_info):
        user = self.find_by_user_id(user_id)
        if user:
            if updated_info.get('user_id'):
                user.set_user_id(updated_info['user_id'])
            if updated_info.get('user_name'):
                user.set_user_name(updated_info['user_name'])
            if updated_info.get('user_gender'):
                user.set_user_gender(updated_info['user_gender'])
            if updated_info.get('user_birth'):
                user.set_user_birth(updated_info['user_birth'])
            if updated_info.get('my_menu'):
                user.set_my_menu(updated_info['my_menu'])
            self.save_user()
            return True
        return False


    def get_all_user_info(self):
        return self.user_info


    def find_by_user_id(self, user_id):
        for info in self.user_info:
            if info.get_user_id() == user_id:
                return info

    def find_user_id_by_login_id(self, login_id):
        for info in self.user_info:
            if info.get_login_id() == login_id:
                user_id = info.get_user_id()
                return user_id

