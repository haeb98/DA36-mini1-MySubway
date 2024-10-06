
from MySubway.service.admin_service import AdminService
from MySubway.service.order_service import OrderService


class AdminMenu:
    def __init__(self):
        self.order_service = OrderService()
        self.admin_service = AdminService()

        self.admin_main_str = """
=====Admin Menu=====
1. 유저 정보 관리
2. 매출 전표 조회

0. 종료 하기
====================
> Enter number: """

        self.admin_user_id_str = """
    =====User info=====
    1. 유저 정보 추가
    2. 유저 정보 삭제
    3. 유저 정보 수정
    4. 유저 정보 조회
    
    0. 뒤로 가기
    ===================
    > Enter number: """

        self.admin_stats_str = """
    =====Sales state=====
    1. 일자별 총 매출 조회
    2. 일자별 순 수익 조회
    3. 주문 내역 전체 조회
    
    0. 뒤로 가기
    =====================
    > Enter number: """

    def admin_main(self):
        print('\n어드민으로 로그인되었습니다.')
        # 메인 메뉴
        while True:
            choice = input(self.admin_main_str)
            if choice == '1':
                self.admin_user_id()
            elif choice == '2':
                self.admin_stats()
            elif choice == '0':
                return 0
            else:
                print("❌잘못된 입력입니다.")
                pass

    # 1. 유저 정보 관리
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
                return
            else:
                print("❌잘못된 입력입니다.")
                pass

    #2.매출 전표 조회
    def admin_stats(self):
        while True:
            choice = input(self.admin_stats_str)
            if choice == '1':
                choose_date = input("> 총 매출을 조회할 날짜를 입력하세요(yyyymmdd): ")
                try:
                    total_sales = self.admin_service.total_sales(choose_date)
                    sales_of_date = sum(total_sales)
                    print(f'{choose_date[:4]}년 {choose_date[4:6]}월 {choose_date[6:]}일의 총 매출은 {sales_of_date}원 입니다.')
                except ValueError as e:
                    print(e)
            elif choice == '2':
                choose_month = input("> 순수익을 계산할 년/월을 입력하세요(yyyymm): ")
                try:
                    total_sales = self.admin_service.total_sales(choose_month)
                    sales_of_month = sum(total_sales)
                    pure_earn_of_month = sales_of_month * 0.104
                    print(f'{choose_date[:4]}년 {choose_date[4:6]}월의 순수익은 {pure_earn_of_month}원 입니다.')
                except ValueError as e:
                    print(e)

            elif choice == '3':
                self.admin_orders_inquiry()
            elif choice == '0':
                return
            else:
                print("❌잘못된 입력입니다.")
                pass

    # 3. 주문 내역 전체 조회
    def admin_orders_inquiry(self):
        self.order_service.view_order_info()

    def add_user_info(self):
        print("\n새로운 회원 정보를 입력하세요.")

        login_id = input("> Login ID를 입력하세요: ")
        user_name = input("> 이름을 입력하세요: ")
        user_gender = input("> 성별을 입력하세요 (male/female): ")
        user_birth = input("> 출생년도를 입력하세요 (YYYY): ")
        my_menu = input("> My_menu 입력하세요 [n,n,n,n,n]:") # 새로 주문하며 MyMenu 담을 수 있도록 디벨롭 필요

        result = self.admin_service.add_user(None, login_id, user_name, user_gender, user_birth, my_menu)
        if result == 1:
            print(f"회원 {user_name}이(가) 추가되었습니다.")

    def delete_user_info(self):
        # TODO 회원정보 전체 출력하는 기능 필요
        user_id = input('\n삭제할 회원의 User ID를 입력하세요 : ')
        result = self.admin_service.delete_user(user_id)
        if result == 1:
            print(f"회원 ID {user_id}가 삭제되었습니다.")
        elif result == 0:
            print(f'❌{user_id}번 회원은 존재하지 않습니다.')
        else:
            print('오류가 발생했습니다.')

    def update_user_info(self):
        user_id = int(input('수정할 회원의 유저 id를 입력하세요 : '))
        user = self.admin_service.find_by_user_id(user_id)
        if user:
            print("수정할 정보를 입력하세요 (수정사항이 없는 항목은 입력 없이 Enter) : ")
            login_id = input(f"Login ID (기존: {user.get_login_id()}): ")
            user_name = input(f"이름 (기존: {user.get_user_name()}): ")
            user_gender = input(f"성별 (male/female, 기존: {user.get_user_gender()}): ")
            user_birth = input(f"출생년도 (YYYY, 기존: {user.get_user_birth()}): ")
            my_menu = input(f"MyMenu (기존: {user.get_my_menu()}): ")

            updated_info = {
                'login_id': login_id if login_id else None,
                'user_name': user_name if user_name else None,
                'user_gender': user_gender if user_gender else None,
                'user_birth': user_birth if user_birth else None,
                'my_menu': my_menu if my_menu else None
            }
            result = self.admin_service.update_user_info(user_id, updated_info)
            if result == 1:
                print(f'{user_id}번 회원의 정보가 수정되었습니다.')
            else:
                print('오류가 발생했습니다.')
        else:
            print(f'❌{user_id}번 회원은 존재하지 않습니다.')

    def view_user_info(self):
        user_info = self.admin_service.get_user_info()
        self.paginate(user_info)

    def display_user_info(self, user_info, page, page_size=3):
        start = (page - 1) * page_size
        end = start + page_size
        return user_info[start:end]

    def paginate(self, user_info):
        page = 1
        page_size = 3
        num_pages = (len(user_info) + page_size - 1) // page_size
        while True:
            current_page_user_info = self.display_user_info(user_info, page, page_size)

            print(f'\n======== {page} 페이지 / {num_pages} 페이지 ==========')
            for user in current_page_user_info:
                print(f'User ID : {user.get_user_id()}')
                print(f'Login ID : {user.get_login_id()}')
                print(f'Name : {user.get_user_name()}')
                print(f'Gender : {user.get_user_gender()}')
                print(f'Birth : {user.get_user_birth()}')
                print(f'My menu : {user.get_my_menu()}')
                print('-' * 26)

            choice = input('''
===============================
1. 이전 페이지로
2. 다음 페이지로

0. "유저 정보 조회" 종료
===============================
> Enter number : ''')
            match choice:
                case '1':
                    if page > 1:
                        page -= 1
                case '2':
                    if page < num_pages:
                        page += 1
                case '0':
                    return
                case _:
                    print('❌잘못된 입력입니다.')

            print(f'======== {page} 페이지 / {num_pages} 페이지 ==========')
            for user in current_page_user_info:
                print(f'User ID : {user.get_user_id()}')
                print(f'Login ID : {user.get_login_id()}')
                print(f'Name : {user.get_user_name()}')
                print(f'Gender : {user.get_user_gender()}')
                print(f'Birth : {user.get_user_birth()}')
                print(f'My menu : {user.get_my_menu()}')
                print('-' * 26)



