from project.peaks.base_peak import BasePeak
from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):
    STRENGTH = 150

    def __init__(self, name):
        super().__init__(name, strength=self.STRENGTH)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        dif = 30 * 1.3 if peak.difficulty_level == "Advanced" else 30 * 2.5
        self.strength -= dif
        self.conquered_peaks.append(peak.name)
