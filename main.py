"""Bot to predict the winner of the upcoming soccer match."""


from numpy import maximum


class Team:
    """Information about the soccer team."""

    coeffs = {
        "form": 0.25,
        "head_to_head": 0.2,
        "absent_players": 0.15,
        "home_away": 0.15,
        "place": 0.10,
        "rest": 0.05,
        "motivation": 0.05,
        "mood": 0.05,
    }
    maximums = {
        "form": 5,
        "head_to_head": 10,
        "home_away": None,
        "rest": 3,
        "motivation": 1,
        "mood": 3,
    }
    minimums = {
        "absent_players": 5,
        "place": None,
    }
    score = 0

    def __init__(self, name: str) -> None:
        """Name of the team."""
        self.name = name

    def set_form(self, form: int) -> None:
        """The number of victories in the last five matches of the league."""
        self.form = Team.__input_check(form, self.maximums["form"])

    def __compare_form(self, a_form: int, b_form: int) -> tuple:
        """Compares forms of teams."""
        return Team.__evaluate_with_maximum(a_form, b_form, self.maximums["form"])

    def set_head_to_head(self, head_to_head: int) -> None:
        """The number of victories in the last ten head-to-head matches."""
        self.head_to_head = Team.__input_check(
            head_to_head, self.maximums["head_to_head"]
        )

    def __compare_head_to_head(self, a_head_to_head: int, b_head_to_head: int) -> tuple:
        """Compares results of head-to-head matches."""
        return Team.__evaluate_with_maximum(
            a_head_to_head, b_head_to_head, self.maximums["head_to_head"]
        )

    def set_absent_players(self, absent_players: int) -> None:
        """The number of absent players."""
        self.absent_players = Team.__input_check(
            absent_players, self.minimums["absent_players"]
        )

    def set_standings(self, standings: int) -> None:
        """The size of standings."""
        self.standings = standings
        self.maximums["home_away"] = standings - 1
        self.minimums["place"] = standings

    def set_home_away(self, home_away: int) -> None:
        """The number of victories in all home/away matches of the league."""
        self.home_away = Team.__input_check(home_away, self.maximums["home_away"])

    def set_place(self, place: int) -> None:
        """Place in the standings."""
        self.place = Team.__input_check(place, self.minimums["place"])

    def set_rest(self, rest: int) -> None:
        """The number of days passed from the last match."""
        self.rest = Team.__input_check(rest, self.maximums["rest"])

    def set_motivation(self) -> None:
        """The team is motivated to win if it is in first or last 35% of the table."""

    def set_mood(self, mood: int) -> None:
        """Result of last match."""
        self.mood = mood

    def change_coeffs(self, new_coeffs: list) -> None:
        """Changes coefficients."""
        self.coeffs = new_coeffs

    def predict(self, opponent: "Team") -> str:
        """Predicts the possible winner of the upcoming match."""
        print(self.form, opponent.form)
        print(
            self.__compare_form(
                self.form,
                opponent.form,
            )
        )
        print(self.head_to_head, opponent.head_to_head)
        print(self.__compare_head_to_head(self.head_to_head, opponent.head_to_head))

    def __evaluate_with_maximum(a, b, maximum):
        """Evaluates the percentage."""
        if a == b:
            return 50, 50
        gap = max([a, b]) - min([a, b])
        k = 100 / (a + b) / (maximum / gap) * gap / 2
        if a < b:
            a = round((50 - k), 1)
            b = 100 - a
        else:
            b = round((50 - k), 1)
            a = 100 - b
        return a, b

    def __input_check(var, scale):
        """Checks whether number is less than one."""
        if var >= scale:
            return scale
        return var


if __name__ == "__main__":
    team_a = Team("Barcelona")
    team_a.set_form(6)
    team_a.set_head_to_head(1)
    team_a.set_absent_players(2)
    team_a.set_standings(20)
    team_a.set_place(3)
    team_a.set_home_away(5)
    team_a.set_rest(6)
    team_a.set_motivation()
    team_a.set_mood(2)

    team_b = Team("Lazio")
    team_b.set_form(7)
    team_b.set_head_to_head(2)
    team_b.set_absent_players(3)
    team_b.set_standings(20)
    team_b.set_place(10)
    team_b.set_home_away(10)
    team_b.set_rest(9)
    team_b.set_motivation()
    team_b.set_mood(6)

    print(team_a.predict(team_b))

    # for _ in range(6):
    #     for i in range(6):
    #         print((_, i), "=", team_a.predict(_, i))
