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
            if ltn < 1 or ltn > 45:
                print("[WARN] 1에서 45 사이의 번호를 입력해주세요\n")
            elif ltn in lt2:
                print("[WARN] 중복된 번호입니다\n")
                continue
            else:
                lt2.append(ltn)
            ltn = int(input("수동 번호 입력"))
            if ltn < 1 or ltn > 45:
                print("1에서 45 사이의 숫자를 입력해주세요.")
            elif ltn in lt2:
                print("중복입니다. 다른 숫자를 입력해주세요.")
                continue
            else:
                lt2.append(ltn)

        lt2.sort()
        print(f"\n추첨 번호: {lt2}")
        self.history.append(lt2)

    def lotto_half_auto(self):
        lt3 = []
        print("\n======== 반자동 번호 입력 ========")
        print("0 입력시 번호 입력을 종료합니다\n")
        while len(lt3) < 6: # 3 - 1 반자동 수동번호 추출
            ltn2 = int(input("번호를 입력하세요\n>> "))                          

            if ltn2 == 0:
                break
            elif ltn2 < 1 or ltn2 > 45:
                print("[WARN] 1에서 45 사이의 번호를 입력해주세요\n")
            elif ltn2 in lt3:
                print("[WARN] 중복된 번호입니다\n")
            else:
                lt3.append(ltn2)
            elif ltn2 < 1 or ltn2 > 45:
                print("1에서 45 사이의 숫자를 입력해주세요.")
            elif ltn2 in lt3:
                print("중복입니다. 다른 숫자를 입력해주세요.")
            else:
                lt3.append(ltn2)

        while len(lt3) < 6: # 3 - 2 남은 번호 자동설정
            ltm = random.randint(1,45)

            if ltm not in lt3:
                lt3.append(ltm)

        lt3.sort()
        self.history.append(lt3)

        print(f"추첨 번호: {lt3}")

    def history_list(self):
        if not self.history:
            print("저장된 로또 이력이 없습니다\n")
            return

        print(f"\n로또 이력 총 {len(self.history)}회입니다\n")

        for round_number, numbers in enumerate(self.history, 1):
            print(f"{round_number}회: {numbers}")
        for i in self.history[-5:]:
            print(i, end=", ")
        if not self.history:
            print("저장된 로또 이력이 없습니다.")
            return

        print(f"로또 이력 총 {len(self.history)}회입니다.")

        for round_number, numbers in enumerate(self.history, 1):
            print(f"{round_number}회: {numbers}")
