import pickle
from entity.user_entity import UserEntity

# 유저 정보 리스트를 UserEntity 객체로 변경 (login_id 포함)
user_info = [
    UserEntity(1,"haebin", "Haebin Kim", "female", 2000, []),
    UserEntity(2,"soovin", "Soovin Choi", "male", 2000, []),
    UserEntity(3,"eunbi", "Eunbi Jo", "female", 2000, []),
    UserEntity(4,"hangyeol", "Hangyeol Kang", "male", 2000, []),
    UserEntity(5,"youngjun", "Youngjun Yoo", "male", 2000, []),
    UserEntity(6,"jinsu", "Jinsu Kim", "male", 2000, []),
    UserEntity(7,"yejin", "Yejin Lee", "female", 2000, []),
    UserEntity(8,"minha", "Minha Jeon", "female", 2000, []),
    UserEntity(9,"chaeyeon", "Chaeyeon Heo", "female", 2000, []),
    UserEntity(10,"jeongseok", "Jeongseok Sim", "male", 2000, []),
    UserEntity(11,"hyeyoung", "Hyeyoung Kim", "female", 2000, [])
]

# 피클 파일에 UserEntity 객체들을 저장
with open("user_info.pkl", "wb") as file:
    pickle.dump(user_info, file)