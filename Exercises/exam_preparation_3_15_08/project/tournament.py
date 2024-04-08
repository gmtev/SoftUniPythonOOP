from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad


class Tournament:
    EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    TEAM_TYPES = {"IndoorTeam": IndoorTeam, "OutdoorTeam": OutdoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.EQUIPMENT_TYPES:
            raise ValueError("Invalid equipment type!")
        eq = self.EQUIPMENT_TYPES[equipment_type]()
        self.equipment.append(eq)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.TEAM_TYPES:
            raise ValueError("Invalid team type!")
        if self.capacity <= 0:
            return "Not enough tournament capacity."

        self.capacity -= 1
        t = self.TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(t)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = self._find_last_equipment_by_type(equipment_type)
        team = self._find_team_by_name(team_name)
        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")
        team.equipment.append(equipment)
        self.equipment.remove(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self._find_team_by_name(team_name)
        if team is None:
            raise Exception("No such team!")
        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.capacity += 1
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        collection = len([eq.increase_price() for eq in self.equipment if eq.TYPE == equipment_type])

        return f"Successfully changed {collection}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._find_team_by_name(team_name1)
        team2 = self._find_team_by_name(team_name2)
        if team1.TYPE != team2.TYPE:
            raise Exception("Game cannot start! Team types mismatch!")
        points1 = team1.advantage + sum(el.protection for el in team1.equipment)
        points2 = team2.advantage + sum(el.protection for el in team2.equipment)
        if points1 > points2:
            team1.win()
            return f"The winner is {team_name1}."
        elif points2 > points1:
            team2.win()
            return f"The winner is {team_name2}."
        else:
            return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"""Tournament: {self.name}
Number of Teams: {len(self.teams)}
Teams:"""]
        [result.append(t.get_statistics()) for t in sorted_teams]
        return '\n'.join(result)

    def _find_last_equipment_by_type(self, equipment_type):
        collection = [eq for eq in self.equipment if eq.TYPE == equipment_type]
        return collection[-1] if collection else None

    def _find_team_by_name(self, team_name):
        collection = [t for t in self.teams if t.name == team_name]
        return collection[0] if collection else None


