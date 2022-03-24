"""Bot."""


from os import PRIO_PGRP


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
    score = 0

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

    def change_coeffs(self, new_coeffs):
        self.coeffs = new_coeffs

    def predict(self, opponent):
        self.__zip()
        opponent.__zip()

        for _, coeff in enumerate(list(self.coeffs.values())):
            a, b = Team.__chance(self.data[_], opponent.data[_], coeff)
            self.score += a
            opponent.score += b

        return self.score, opponent.score

    def __chance(a, b, coeff):
        if a == b:
            return a, b
        if a < b:
            b /= float(f"1.{int(100 / (a + b) * (b - a) * 0.8)}")

        else:
            a /= float(f"1.{int(100 / (a + b) * (a - b) * 0.8)}")
        return round(100 / (a + b) * a * coeff, 1), round(100 / (a + b) * b * coeff, 1)

    def __zip(self):
        self.data = list(self.__dict__.values())[1:]


if __name__ == "__main__":
    team_a = Team("Barcelona")
    team_a.set_form(0)
    team_a.set_head_to_head(0)
    team_a.set_absent_players(0)
    team_a.set_home_away(0)
    team_a.set_standings(0)
    team_a.set_rest(0)
    team_a.set_motivation(0)
    team_a.set_mood(0)

    team_b = Team("Lazio")
    team_b.set_form(1)
    team_b.set_head_to_head(1)
    team_b.set_absent_players(1)
    team_b.set_home_away(1)
    team_b.set_standings(1)
    team_b.set_rest(1)
    team_b.set_motivation(1)
    team_b.set_mood(1)

    print(team_a.predict(team_b))
