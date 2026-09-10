import random

class UpDownGame:

    def __init__(self, name , level_range):
        self.name = name
        self.level_range = level_range
        self.count = 0
        self.answer = random.randint(1,level_range)
        

    def play(self):
        print(f"1에서 {self.level_range}까지 숫자 중에 하나를 맞혀보세요")

        while True:
            try:
                i = int(input("숫자 입력: "))
            except ValueError:
                print("숫자로 입력해주세요.")
                continue

            self.count += 1

            if self.answer > i:
                print("더 높이")

            elif self.answer < i:
                print("더 낮게")

            elif self.answer == i:
                print("정답")
                print(f"{self.count}번 만에 성공!")

                return self.count
