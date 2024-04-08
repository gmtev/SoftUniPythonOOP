from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    OXYGEN_LEVEL = 120

    def __init__(self, name):
        super().__init__(name, FreeDiver.OXYGEN_LEVEL)

    def miss(self, time_to_catch):
        used = round(time_to_catch * 0.6)

        if self.oxygen_level < used:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= used

    def renew_oxy(self):
        self.oxygen_level = FreeDiver.OXYGEN_LEVEL
