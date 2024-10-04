
class UserEntity:
    next_id = 1
    def __init__(self, user_id, login_id, user_name, user_gender, user_birth, my_menu):
        self.__user_id = user_id
        self.__user_login_id = login_id
        self.__user_name = user_name
        self.__user_gender = user_gender
        self.__user_birth = user_birth
        self.__my_menu = my_menu
        UserEntity.next_id += 1

    def get_login_id(self):
        return self.__user_login_id
    def get_user_id(self):
        return int(self.__user_id)
    def get_user_name(self):
        return self.__user_name
    def get_user_gender(self):
        return self.__user_gender
    def get_user_birth(self):
        return self.__user_birth
    def get_my_menu(self):
        return self.__my_menu

    def set_user_id(self,user_id):
        self.__user_id = user_id
    def set_user_name(self,user_name):
        self.__user_name = user_name
    def set_user_gender(self,user_gender):
        self.__user_gender = user_gender
    def set_user_birth(self,user_birth):
        self.__user_birth = user_birth
    def set_my_menu(self,my_menu):
        self.__my_menu = my_menu


    def __repr__(self):
        return f'{{id={self.__user_id}, name={self.__user_name}, gender={self.__user_gender}, birth={self.__user_birth}, my menu={self.__my_menu}}}'


