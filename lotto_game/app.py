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


    def run(self):
        while True:
            Menu.main_menu()
            n = int(input("번호를 선택하세요\n>> "))

            if n == 1:
                Menu.mode_select()
                o = int(input("번호를 선택하세요\n>> "))

                if o == 1:
                    while True:
                        Menu.lotto_menu()
                        p = int(input("번호를 선택하세요\n>> "))

                        if p == 1 :
                            Menu.lotto_menu2()
                            n2 = int(input("번호를 선택하세요\n>> "))

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
                            print("종료")
                            break

                elif o == 2:
                    while True:
                        Menu.up_down_menu()
                        i = int(input("번호를 선택하세요\n>> "))
                        

                        if i == 1:
                            nick = input("\n닉네임을 입력하세요\n>> ")
                            Menu.up_down_level()
                            level = int(input("난이도를 선택하세요\n>> "))
                            print()

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

                        elif i == 2:
                            print("게임 종료")
                            break

            elif n == 2:
                Menu.hs_rank()
                k = int(input("번호를 입력하세요\n>> "))

                if k == 1:
                    self.lotto.history_list()

                elif k == 2:
                    self.ranking.show_ranking()

            elif n == 3:
                print("게임 종료")
                break
