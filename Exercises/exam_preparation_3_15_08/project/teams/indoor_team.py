from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    INITIAL_BUDGET = 500.0
    TYPE = "IndoorTeam"

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.INITIAL_BUDGET)

    def win(self):
        self.advantage += 145
        self.wins += 1
