from typing import List
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[FreeDiver or ScubaDiver] = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        try:
            diver = next(filter(lambda d: d.name == diver_name, self.divers))
            if diver:
                return f"{diver_name} is already a participant."
        except StopIteration:
            new_diver = self.DIVER_TYPES[diver_type](diver_name)
            self.divers.append(new_diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            fish = next(filter(lambda f: f.name == fish_name, self.fish_list))
            if fish:
                return f"{fish_name} is already permitted."
        except StopIteration:
            new_fish = self.FISH_TYPES[fish_type](fish_name, points)
            self.fish_list.append(new_fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self._get_diver(diver_name)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = self._get_fish(fish_name)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} hits a {fish.points:.1f}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} hits a {fish.points:.1f}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.oxygen_level = diver.OXYGEN_LEVEL
                diver.has_health_issue = False
                count += 1
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = self._get_diver(diver_name)
        details = '\n'.join(fish.fish_details() for fish in diver.catch)
        return f"**{diver_name} Catch Report**\n" \
               f"{details}"

    def competition_statistics(self):
        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]
        sorted_divers = sorted(healthy_divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))

        result = "**Nautical Catch Challenge Statistics**\n"
        result += "\n".join(str(d) for d in sorted_divers)
        return result

    # helpers
    def _get_diver(self, diver_name: str):
        diver = [d for d in self.divers if d.name == diver_name]
        return diver[0] if diver else None

    def _get_fish(self, fish_name: str):
        fish = [f for f in self.fish_list if f.name == fish_name]
        return fish[0] if fish else None
