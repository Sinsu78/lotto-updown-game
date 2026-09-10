import random

class LottoGenerator:

    def __init__(self):
        self.history = []

    def lotto_auto(self):
        lt = random.sample(range(1, 45), 6)
        lt.sort()
        self.history.append(lt)
        print("\n======== 자동 번호 입력 ========")
        print(f"추첨 번호: {lt}")

    def lotto_manual(self):
        lt2 = []
        print("\n======== 수동 번호 입력 ========")
        while len(lt2) < 6:
            ltn = int(input("번호를 입력하세요\n>> "))
            lt2.append(ltn)

        print(f"\n추첨 번호: {lt2}")
        self.history.append(lt2)

    def lotto_half_auto(self):
        lt3 = []
        print("\n======== 반자동 번호 입력 ========")
        print("0 입력시 번호 입력을 종료합니다\n")
        while len(lt3) < 6: # 3 - 1 반자동 수동번호 추출
            ltn2 = int(input("번호를 입력하세요\n>> "))                          
            lt3.append(ltn2)

            if ltn2 == 0:
                break

        while len(lt3) < 6: # 3 - 2 남은 번호 자동설정
            ltm = random.randint(1,45)

            if ltm not in lt3:
                lt3.append(ltm)

        lt3.sort()
        self.history.append(lt3)

        print(f"\n추첨 번호: {lt3}")

    def history_list(self):
        for i in self.history[-5:]:
            print(i, end=", ")