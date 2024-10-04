from MySubway_soovin.service.admin_service import AdminService

class AdminMenu:
    def __init__(self):
        self.admin_service = AdminService()

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
        3. 유저 아이디 수정
        4. 유저 아이디 조회
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

    # 유저 아이디 관리
    def admin_user_id(self):
        while True:
            choice = input(self.admin_user_id_str)
            if choice == '1':
                self.add_user_info()
            elif choice == '2':
                self.delete_user_info()
            elif choice == '3':
                self.update_user_info()
            elif choice == '4':
                self.view_user_info()
            elif choice == '0':
                break
            else:
                print("잘못된 선택입니다.")


    def add_user_info(self):
        print("새로운 회원 정보를 입력하세요.")

        login_id = input("로그인 ID를 입력하세요: ")
        user_name = input("이름을 입력하세요: ")
        user_gender = input("성별을 입력하세요 (Male/Female): ")
        user_birth = input("생년을 입력하세요 (YYYY): ")
        my_menu = []

        self.admin_service.add_user(None, login_id, user_name, user_gender, user_birth, my_menu)

        print(f"회원 {user_name}이(가) 추가되었습니다.")

    def delete_user_info(self):
        user_id = input('삭제할 회원의 유저 id를 입력하세요 : ')
        result = self.admin_service.delete_user(user_id)
        if result:
            print(f"회원 ID {user_id}가 삭제되었습니다.")
        else:
            print('오류가 발생했습니다.')

    def update_user_info(self):
        user_id = int(input('수정할 회원의 유저 id를 입력하세요 : '))
        user = self.admin_service.find_by_id(user_id)
        if user:
            print("수정할 정보를 입력하세요 (수정하지 않으려면 아무 것도 입력하지 않고 Enter를 누르세요) : ")
            login_id = input(f"로그인 ID ({user.get_login_id()}): ")
            user_name = input(f"이름 ({user.get_user_name()}): ")
            user_gender = input(f"성별 (Male/Female, 현재: {user.get_user_gender()}): ")
            user_birth = input(f"생년 (YYYY, 현재: {user.get_user_birth()}): ")
            my_menu = input(f"메뉴 (현재: {user.get_my_menu()}): ")

            updated_info = {
                'login_id': login_id if login_id else None,
                'user_name': user_name if user_name else None,
                'user_gender': user_gender if user_gender else None,
                'user_birth': user_birth if user_birth else None,
                'my_menu': my_menu if my_menu else None
            }
            result = self.admin_service.update_user_info(user_id, updated_info)
            if result:
                print(f'{user_id}번 회원의 정보가 수정되었습니다.')
            else:
                print('오류가 발생했습니다.')
        else:
            print(f'{user_id}번 회원은 존재하지 않습니다.')

    def view_user_info(self):
        user_info = self.admin_service.get_user_info()
        self.paginate(user_info)

    def display_user_info(self, user_info, page, page_size=5):
        start = (page - 1) * page_size
        end = start + page_size
        return user_info[start:end]

    def paginate(self, user_info):
        page = 1
        page_size = 5
        num_pages = (len(user_info) + page_size - 1) // page_size
        while True:
            current_page_user_info = self.display_user_info(user_info, page, page_size)

            print(f'======== {page} 페이지 / {num_pages} 페이지 ==========')
            for user in current_page_user_info:
                print(f'User ID : {user.get_user_id()}')
                print(f'Login ID : {user.get_login_id()}') #
                print(f'Name : {user.get_user_name()}')
                print(f'Gender : {user.get_user_gender()}')
                print(f'Birth : {user.get_user_birth()}')
                print(f'My menu : {user.get_my_menu()}')
                print('-' * 26)

            choice = input('''
    ----------------------
    1. 이전 페이지로
    2. 다음 페이지로
    3. 유저 정보 조회 종료
    ''')
            match choice:
                case '1':
                    if page > 1:
                        page -= 1
                case '2':
                    if page < num_pages:
                        page += 1
                case '3':
                    return
                case _:
                    print('잘못 입력하셨습니다. 다시 입력해주세요.')

            print(f'======== {page} 페이지 / {num_pages} 페이지 ==========')
            for user in current_page_user_info:
                print(f'User ID : {user.get_user_id()}')
                print(f'Login ID : {user.get_login_id()}')
                print(f'Name : {user.get_user_name()}')
                print(f'Gender : {user.get_user_gender()}')
                print(f'Birth : {user.get_user_birth()}')
                print(f'My menu : {user.get_my_menu()}')
                print('-' * 26)

# 인스턴스 생성 및 실행
admin_menu_instance = AdminMenu()
admin_menu_instance.run()
