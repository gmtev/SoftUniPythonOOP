from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    TIME_TO_CATCH = 180

    def __init__(self, name, points):
        super().__init__(name, points, DeepSeaFish.TIME_TO_CATCH)

    def fish_details(self):
        return f"{DeepSeaFish.__name__}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"