"""Bot."""


class Team:
    coeffs = {
        "Form": 0.25,
        "Head-to-head": 0.2,
        "Absent players": 0.15,
        "Home/away": 0.15,
        "Standings": 0.10,
        "Rest": 0.05,
        "Motivation": 0.05,
        "Mood": 0.05,
    }

    def __init__(self, name):
        self.name = name

    def set_form(self, form):
        self.form = form

    def set_head_to_head(self, head_to_head):
        self.head_to_head = head_to_head

    def set_absent_players(self, absent_players):
        self.absent_players = absent_players

    def set_home_away(self, home_away):
        self.home_away = home_away

    def set_table(self, table):
        self.table = table

    def set_standings(self, standings):
        self.standings = standings

    def set_rest(self, rest):
        self.rest = rest

    def set_motivation(self, motivation):
        self.motivation = motivation

    def set_mood(self, mood):
        self.mood = mood

    def chance(self, coeffs):
        self.chance = (
            self.form * coeffs["Form"]
            + self.head_to_head * coeffs["Head-to-head"]
            + self.absent_players * coeffs["Absent players"]
            + self.home_away * coeffs["Home/away"]
            + self.table * coeffs["Table"]
            + self.standings * coeffs["Standings"]
            + self.rest * coeffs["Rest"]
            + self.motivation * coeffs["Motivation"]
            + self.mood * coeffs["Motivation"]
        )

    def predict(self, opponent):
        pass

    def change_coeffs(self, new_coeffs):
        self.coeffs = new_coeffs


if __name__ == "__main__":
    pass
