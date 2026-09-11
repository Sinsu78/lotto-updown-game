from .updown.ranking import Player

class LottoStorage:
    def save(self, history):
        with open("lotto_history.txt", "w", encoding="utf-8") as file:
            for i in history:
                file.write(",".join(str(n) for n in i)+"\n")

    def load(self):
        try:
            with open("lotto_history.txt", "r", encoding="utf-8") as file:
                content = []

                for line in file:
                    content.append([int(n) for n in line.strip().split(",")])

            return content

        except FileNotFoundError:
            return []


class RankingStorage:
    def save(self, players):
        with open("ranking_history.txt", "w", encoding="utf-8") as file:
            for player in players:
                file.write(f"{player.name}, {player.tries}\n")


    def load(self):
        try:
            with open("ranking_history.txt", "r", encoding="utf-8") as file:
                content2 = []

                for line in file:
                    parts = line.strip().split(",")
                    name = parts[0]
                    tries = int(parts[1])
                    n = Player(name, tries)
                    content2.append(n)

            return content2
                

        except FileNotFoundError:
            return []