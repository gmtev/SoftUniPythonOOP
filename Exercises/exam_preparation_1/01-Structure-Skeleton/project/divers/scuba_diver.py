from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    OXYGEN_LEVEL = 540

    def __init__(self, name):
        super().__init__(name, oxygen_level=self.OXYGEN_LEVEL)

    def miss(self, time_to_catch):
        used = round(time_to_catch * 0.3)

        if self.oxygen_level < used:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= used

    def renew_oxy(self):
        self.oxygen_level = self.OXYGEN_LEVEL