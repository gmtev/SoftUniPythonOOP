from typing import List
from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str) -> str:
        try:
            player = next(filter(lambda pl: pl.name == player_name, self.players))
            player.guild = "Unaffiliated"

            return f"Player {player_name} has been removed from the guild."

        except StopIteration:
            return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        info = '\n'.join(player.player_info() for player in self.players)
        return f"Guild: {self.name}\n{info}"


