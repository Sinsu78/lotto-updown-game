import random

class UpDownGame:

    def __init__(self, name , level_range):
        self.name = name
        self.level_range = level_range
        self.count = 0
        self.answer = random.randint(1,level_range)
        

    def play(self):
        while True:
            i = int(input("숫자입력"))
            self.count += 1

            if self.answer > i:
                print("더높이")

            elif self.answer < i:
                print("더 낮게")

            elif self.answer == i:
                print("정답")
                print(f"{self.count}번 만에 성공!")

                return self.count
