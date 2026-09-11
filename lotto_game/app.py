from .lotto.generator import LottoGenerator
from .updown.game import UpDownGame
from .updown.ranking import RankingBoard, Player
from .ui.menus import Menu
from .storage import LottoStorage, RankingStorage

class GameApp:
    def __init__(self):
        self.lotto = LottoGenerator()
        self.ranking = RankingBoard()
        self.lottostorage = LottoStorage()
        self.rankingstorage = RankingStorage()
        self.lotto.history = self.lottostorage.load()
        self.ranking.players = self.rankingstorage.load()

    def get_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("\n[WARN] 잘못된 입력입니다\n")

    def run(self):
        while True:
            Menu.main_menu()
            n = self.get_int_input("번호를 입력하세요\n>> ")

            if n == 1:
                Menu.mode_select()
                o = self.get_int_input("번호를 입력하세요\n>> ")

                if o == 1:
                    while True:
                        Menu.lotto_menu()
                        p = self.get_int_input("번호를 입력하세요\n>> ")

                        if p == 1 :
                            Menu.lotto_menu2()
                            n2 = self.get_int_input("번호를 입력하세요\n>> ")

                            if n2 == 1:
                                self.lotto.lotto_auto()
                                self.lottostorage.save(self.lotto.history)
                            elif n2 == 2:
                                self.lotto.lotto_manual()
                                self.lottostorage.save(self.lotto.history)
                            elif n2 == 3:
                                self.lotto.lotto_half_auto()
                                self.lottostorage.save(self.lotto.history)

                        elif p == 2 :
                            self.lotto.history_list()

                        elif p == 3:
                            print("\n종료합니다")
                            break
                        else:
                            print("\n[WARN] 메뉴에 없는 번호입니다\n")

                elif o == 2:
                    while True:
                        Menu.up_down_menu()
                        i = self.get_int_input("번호를 입력하세요\n>> ")
                        
                        if i == 1:
                            nick = input("\n닉네임을 입력하세요\n>> ")
                            Menu.up_down_level()
                            level = self.get_int_input("난이도를 선택하세요\n>> ")

                            if level == 1:
                                self.updown = UpDownGame(nick, 1000)
                                tries = self.updown.play()
                                self.ranking.add_result(Player(nick, tries))
                                self.rankingstorage.save(self.ranking.players)
                            elif level == 2:
                                self.updown = UpDownGame(nick, 500)
                                tries = self.updown.play()
                                self.ranking.add_result(Player(nick, tries))
                                self.rankingstorage.save(self.ranking.players)
                            elif level == 3:
                                self.updown = UpDownGame(nick, 100)
                                tries = self.updown.play()
                                self.ranking.add_result(Player(nick, tries))
                                self.rankingstorage.save(self.ranking.players)
                            else:
                                print("\n[WARN] 메뉴에 없는 번호입니다\n")

                        elif i == 2:
                            print("\n게임을 종료합니다")
                            break
                        else:
                            print("\n[WARN] 메뉴에 없는 번호입니다\n")

                else:
                    print("\n[WARN] 메뉴에 없는 번호입니다\n")

            elif n == 2:
                Menu.hs_rank()
                k = self.get_int_input("번호를 입력하세요\n>> ")

                if k == 1:
                    self.lotto.history_list()
                elif k == 2:
                    self.ranking.show_ranking()
                else:
                    print("\n[WARN] 메뉴에 없는 번호입니다\n")

            elif n == 3:
                print("\n프로그램을 종료합니다\n")
                break
            
            else:
                print("\n[WARN] 메뉴에 없는 번호입니다\n")
