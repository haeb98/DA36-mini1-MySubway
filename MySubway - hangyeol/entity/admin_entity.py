
class AdminEntity:
    id = 1  # 클래스 변수 id (공용)

    def __init__(self,id, logid, name, gender, birthyear,mymenu):
        self.__id = AdminEntity.id  # 클래스 변수 id로부터 채번
        self.__logid = logid
        self.__name = name
        self.__gender = gender
        self.__birthyear = birthyear
        self.__mymenu = mymenu
        AdminEntity.id += 1


    def get_id(self):
        return self.__id

    def get_logid(self):
        return self.__logid

    def set_logid(self, logid):
        self.__logid = logid

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_birthyear(self):
        return self.__birthyear

    def set_birthyear(self, birthyear):
        self.__birthyear = birthyear

    def get_mymenu(self):
        return self.__mymenu

    def set_mymenu(self, mymenu):
        self.__mymenu = mymenu



    def __repr__(self):
        return (f'Emp{{id={self.__id},logid={self.__logid},'
                f'name={self.__name},gender={self.__gender},'
                f'birthyear={self.__birthyear},mymenu={self.__mymenu})}}')
