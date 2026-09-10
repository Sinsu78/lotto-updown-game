import random

class UpDownGame:

    def __init__(self, name , level_range):
        self.name = name
        self.level_range = level_range
        self.count = 0
        self.answer = random.randint(1,level_range)
        

    def play(self):
        while True:
            i = int(input("숫자를 입력하세요\n>> "))
            self.count += 1

            if self.answer > i:
                print("더 높은 숫자입니다\n")

            elif self.answer < i:
                print("더 낮은 숫자입니다\n")

            elif self.answer == i:
                print(f"{self.answer} -> 정답입니다\n")
                print(f"{self.count}번 만에 성공!")

                return self.count
