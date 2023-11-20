class Trails:
    def __init__(self, name):
        self._name = name
        self._total_trails = 0
        self._opened_trails = 0
        self._total_chair_lifts = 0
        self._opened_chair_lifts = 0

    def get_name(self):
        return self._name

    def get_total_trails(self):
        return self._total_trails

    def set_total_trails(self, value):
        self._total_trails = value

    def get_opened_trails(self):
        return self._opened_trails

    def set_opened_trails(self, value):
        self._opened_trails = value

    def get_opened_chair_lifts(self):
        return self._opened_chair_lifts

    def set_opened_chair_lifts(self, value):
        self._opened_chair_lifts = value

    def get_total_chair_lifts(self):
        return self._total_chair_lifts

    def set_total_chair_lifts(self, value):
        self._total_chair_lifts = value
