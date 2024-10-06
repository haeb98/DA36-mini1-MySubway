import pickle
import os
from MySubway.entity.user_entity import UserEntity

class UserRepo:
    path = os.path.join(os.path.dirname(__file__), 'user_info.pkl')
    def __init__(self):
        self.user_info = []
        self.load_user_info(self.path)

    def get_user_info(self):
        return self.user_info

    def load_user_info(self, path):
        if not os.path.exists(path):
            self.user_info = self.create_user_info_file()

        else:
            with open(self.path, 'rb') as f:
                self.user_info = pickle.load(f)

                if len(self.user_info) > 0:
                    UserEntity.next_id = self.user_info[-1].get_user_id() + 1

    def save_user(self):
        with open('user_info.pkl', 'wb') as f:
            pickle.dump(self.user_info, f)

    def add_user(self,user_info):
        self.user_info.append(user_info)
        self.save_user()
        return 1

    def delete_user(self, user_id):
        user_id = int(user_id)
        len_user_info = len(self.user_info)
        self.user_info = [user for user in self.user_info if user.get_user_id() != user_id]
        if len(self.user_info) < len_user_info:
            self.save_user()
            return 1
        else:
            return 0

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
            return 1
        return 0

    def find_by_user_id(self, user_id):
        for info in self.user_info:
            if info.get_user_id() == user_id:
                return info

    def get_all_user_info(self):
        return self.user_info



    def find_user_id_by_login_id(self, login_id):
        for info in self.user_info:
            if info.get_login_id() == login_id:
                user_id = info.get_user_id()
                return user_id

    def create_user_info_file(self):
        user_info = [
            UserEntity(1, "haebin", "Haebin Kim", "female", 2000, [1,2,1,2,1]),
            UserEntity(2, "soovin", "Soovin Choi", "male", 2000, [3,1,1,9,9]),
            UserEntity(3, "eunbi", "Eunbi Jo", "female", 2000, [1,1,1,1,1]),
            UserEntity(4, "hangyeol", "Hangyeol Kang", "male", 2000, [3,4,4,5,5]),
            UserEntity(5, "youngjun", "Youngjun Yoo", "male", 2000, [2,2,2,2,2]),
            UserEntity(6, "jinsu", "Jinsu Kim", "male", 2000, [2,2,2,2,2]),
            UserEntity(7, "yejin", "Yejin Lee", "female", 2000, [2,2,2,2,2]),
            UserEntity(8, "minha", "Minha Jeon", "female", 2000, [2,2,2,2,2]),
            UserEntity(9, "chaeyeon", "Chaeyeon Heo", "female", 2000, [2,2,2,2,2]),
            UserEntity(10, "jeongseok", "Jeongseok Sim", "male", 2000, [2,2,2,2,2]),
            UserEntity(11, "hyeyoung", "Hyeyoung Kim", "female", 2000, [2,2,2,2,2])
        ]

        # 피클 파일에 UserEntity 객체들을 저장
        with open(self.path, "wb") as file:
            pickle.dump(user_info, file)

        return user_info

