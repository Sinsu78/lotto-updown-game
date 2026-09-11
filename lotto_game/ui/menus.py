class Menu:
    @staticmethod
    def main_menu():
        print("\n======== 메뉴 선택 ========")
        print("1. 모드 선택")
        print("2. 기록 보기")
        print("3. 프로그램 종료\n")

    @staticmethod
    def mode_select():
        print("\n======== 모드 선택 ========")
        print("1. 로또번호 추첨")
        print("2. 업앤다운 게임\n")


    @staticmethod
    def lotto_menu():
        print("\n======== 로또번호 추첨 ========")              
        print("1. 추첨 방식 선택")
        print("2. 추첨 이력 보기")
        print("3. 추첨 이력 클리어")
        print("4. 종료하기\n")     


    @staticmethod
    def lotto_menu2():
        print("\n======== 추첨 방식 선택 ========") 
        print("1. 자동")
        print("2. 수동")
        print("3. 반자동\n")

    @staticmethod
    def up_down_menu():
        print("\n======== 업앤다운 게임 ========")
        print("1. 게임 시작")
        print("2. 종료하기\n")

    @staticmethod
    def up_down_level():
        print("\n======== 게임 난이도 선택 ========")
        print("1. 상")
        print("2. 중")
        print("3. 하\n")

    @staticmethod
    def hs_rank():
        print("\n======== 기록 보기 ========")
        print("1. 로또번호 추첨 이력")
        print("2. 업앤다운 게임 랭킹\n")
