class Player:
    def __init__(self, name, tries):
        self.name = name
        self.tries = tries

    def __repr__(self) -> str:
        return f"Player(name = {self.name}, tries={self.tries})"

class RankingBoard:
    def __init__(self):
        self.players = []

    def add_result(self,player):
        self.players.append(player)

    def show_ranking(self):
        rank_try = sorted(self.players, key = lambda x : (x.tries))
        rank = 0
        for i in rank_try:
            rank += 1
            print(f"{rank}등 {i.name} , {i.tries}회")
