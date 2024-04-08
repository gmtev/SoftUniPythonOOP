from project.peaks.base_peak import BasePeak
from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):
    STRENGTH = 200

    def __init__(self, name):
        super().__init__(name, strength=self.STRENGTH)

    def can_climb(self):
        return self.strength >= 100

    def climb(self, peak: BasePeak):
        dif = 20 * 2 if peak.difficulty_level == "Extreme" else 20 * 1.5
        self.strength -= dif
        self.conquered_peaks.append(peak.name)
