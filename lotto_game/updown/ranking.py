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


    def show_ranking(self, top_n=5):
        ranked = sorted(self.players, key=lambda p: p.tries)
        ranked = ranked[:top_n]
        print()
        for rank, player in enumerate(ranked, start=1):
            print(f"{rank}등 {player.name} {player.tries}")
