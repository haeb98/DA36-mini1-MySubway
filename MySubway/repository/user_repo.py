import pickle


class UserRepo:
    def __init__(self):
        self.user_info = []

    def load_user_info(self, filename='user_info.pkl'):
        with open(filename, 'rb') as f:
            self.user_info = pickle.load(f)

            # if len(self.user_info) > 0:
            #     UserEntity.next_id = self.user_info[-1].get_user_id() + 1

            print("user_info.pkl이 로드되었습니다.")

    def create_user_info(self, info):
        self.user_info.append(info)
        return 1

    def find_all(self):
        return self.user_info

    def find_by_user_id(self, user_id):
        for info in self.user_info:
            if info.get_user_id() == user_id:
                return info

    def update_user_info(self, user_id, attr, new_value):
        info = self.find_by_user_id(user_id)
        if info:
            match attr:
                case 'user_id':
                    info.set_user_id(new_value)
                case 'login_id':
                    info.set_user_login_id(new_value)
                case 'user_name':
                    info.set_user_name(new_value)
                case 'user_gender':
                    info.set_user_gender(new_value)
                case 'user_birth':
                    info.set_user_birth(new_value)
                case 'my_menu':
                    info.set_my_menu(new_value)
                case _:
                    raise AttributeError(f'{attr}속성은 존재하지 않습니다.')
            return 1
        else:
            return 0

    def remove_user_info(self, user_id):
        user_id = int(user_id)
        return self.user_info.pop(user_id + 1)

user_repo = UserRepo()
user_repo.load_user_info()
print(user_repo.find_all())