try:
    with open('emps.pkl', 'rb') as f:
        self.emps = pickle.load(f)

        if len(self.emps) > 0:
            # Emp.next_id값을 마지막 사원 아이디 +1로 지정
            Emp.next_id = self.emps[-1].get_id() + 1

        print('> emps.pkl이 로드되었습니다.')
except FileNotFoundError:
    # 파일일 존재하지 않는 경우
    self.emps = []


def __del__(self):
    """
    소멸자 메소드 : 인스턴스가 메모리에서 해제될때 호출되는 메소드
    """
    with open('emps.pkl', 'wb') as f:
        pickle.dump(self.emps, f)
        print('️☺️☺️️☺️ 사원정보를 성공적으로 저장했습니다. 다음에 만나요... ☺️☺️☺️')