from service.user_service import UserService
from admin_repo import AdminRepo
from entity.user_entity import UserEntity
from user_repo import UserRepo
class MenuRepo:

    def __init__(self):
        self.user_service = UserService()


    class AdminMenu:
        def __init__(self):
            self.admin_repo = AdminRepo

            # 메뉴에 대한 메시지를 미리 정의
            self.admin_main_str = """
            1. 로그인 관리
            2. 메뉴 관리
            3. 매장 통계
            0. 뒤로 가기
            -------------------
            입력 : 
            """
            self.admin_lgn_str = """ 
            1. 관리자 아이디 관리
            2. 유저 아이디 관리
            0. 뒤로 가기 
            """
            self.admin_admin_id_str = """
            1. 관리자 아이디 수정
            0. 뒤로가기 
            """
            self.admin_user_id_str = """
            1. 유저 아이디 추가
            2. 유저 아이디 삭제
            0. 뒤로가기
            """
            self.admin_menu_str = """
            1. 새로운 메인 메뉴 추가
            2. 기존 메뉴 삭제
            0. 뒤로 가기
            """
            self.admin_newmanu_str = """
            1. 메뉴 추가하기
            0. 뒤로 가기
            """
            self.admin_oldmanu_str = """
            1. 메뉴 삭제하기
            0. 뒤로 가기
            """
            self.admin_stats_str = """
            1. 순수익 조회
            2. 순지출 조회
            3. 일자별 매출 조회
            4. 주간 매출 조회
            5. 주간별 매출 조회
            0. 뒤로 가기
            """

        def run(self):
            # 메인 루프
            while True:
                choice = input(self.admin_main_str)
                if choice == '1':
                    self.admin_lgn()
                elif choice == '2':
                    self.admin_menu()
                elif choice == '3':
                    self.admin_stats()
                elif choice == '0':
                    print("프로그램을 종료합니다.")
                    break
                else:
                    print("잘못된 선택입니다.")

        # 로그인 관리
        def admin_lgn(self):
            while True:
                choice = input(self.admin_lgn_str)
                if choice == '1':
                    self.admin_admin_id()
                elif choice == '2':
                    self.admin_user_id()
                elif choice == '0':
                    break
                else:
                    print("잘못된 선택입니다.")

        # 관리자 아이디 관리
        def admin_admin_id(self):
            while True:
                choice = input(self.admin_admin_id_str)
                if choice == '1':
                    input("수정할 관리자 아이디를 입력해주세요 : ")
                elif choice == '0':
                    break
                else:
                    print("잘못된 선택입니다.")

        # 유저 아이디 관리
        def admin_user_id(self):
            while True:
                choice = input(self.admin_user_id_str)
                if choice == '1':
                    user_id = 1
                    login_id = input("추가할 로그인 아이디를 입력해주세요 : ")
                    user_name = input("이름을 입력해주세요 : ")
                    user_gender = input("성별을 입력해주세요 : ")
                    user_birth = int(input("생년을 입력해주세요 : "))

                    new_user = UserEntity(user_id, login_id, user_name, user_gender, user_birth, [])
                    ur = UserRepo()
                    ur.load_user_info(filename='user_info.pkl')
                    ur.create_user_info()
                elif choice == '2':
                    input("삭제할 유저 아이디를 입력해주세요 : ")
                elif choice == '0':
                    break
                else:
                    print("잘못된 선택입니다.")

        # 메뉴 관리
        def admin_menu(self):
            while True:
                choice = input(self.admin_menu_str)
                if choice == '1':
                    self.admin_newmenu()
                elif choice == '2':
                    self.admin_oldmenu()
                elif choice == '0':
                    break
                else:
                    print("잘못된 선택입니다.")

        # 새로운 메인 메뉴 추가
        def admin_newmenu(self):
            input("추가할 메뉴의 이름을 입력해 주세요 : ")

        # 기존 메뉴 삭제
        def admin_oldmenu(self):
            input("삭제할 메뉴의 번호를 입력해 주세요 : ")

        # 매장 통계 관리
        def admin_stats(self):
            while True:
                choice = input(self.admin_stats_str)
                if choice == '1':
                    print("순수익 조회")
                    # 여기에 순수익 조회 기능 추가
                elif choice == '2':
                    print("순지출 조회")
                    # 여기에 순지출 조회 기능 추가
                elif choice == '3':
                    print("일자별 매출 조회")
                    AdminRepo.total_sales()
                    # 여기에 일자별 매출 조회 기능 추가
                elif choice == '4':
                    print("주간 매출 조회")
                    # 여기에 주간 매출 조회 기능 추가
                elif choice == '5':
                    print("주간별 매출 조회")
                    # 여기에 주간별 매출 조회 기능 추가
                elif choice == '0':
                    break
                else:
                    print("잘못된 선택입니다.")

    # 인스턴스 생성 및 실행
    admin_menu_instance = AdminMenu()
    admin_menu_instance.run()

    def main_menu(self):
        menu_str = """
        1. 로그인 관리
        2. 메뉴 관리
        3. 매장 통계
        0. 뒤로 가기
        -------------------
        입력 : 
        """

