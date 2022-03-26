"""Bot to predict the winner of the upcoming soccer match."""


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

    def __compare_absent_players(
        self, a_absent_players: int, b_absent_players: int
    ) -> tuple:
        """Compares the number of absent players in the match."""
        return Team.__evaluate_with_minimum(
            a_absent_players, b_absent_players, self.minimums["absent_players"]
        )

    def set_standings(self, standings: int) -> None:
        """The size of standings."""
        self.standings = standings
        self.maximums["home_away"] = standings - 1
        self.minimums["place"] = standings

    def set_home_away(self, home_away: int) -> None:
        """The number of victories in all home/away matches of the league."""
        self.home_away = Team.__input_check(home_away, self.maximums["home_away"])

    def __compare_home_away(self, a_home_away: int, b_home_away: int) -> tuple:
        """Compares results of home/away matches of the league."""
        return Team.__evaluate_with_maximum(
            a_home_away, b_home_away, self.maximums["home_away"]
        )

    def set_place(self, place: int) -> None:
        """Place in the standings."""
        self.place = Team.__input_check(place, self.minimums["place"])

    def __compare_place(self, a_place: int, b_place: int) -> tuple:
        """Compares places in the standings."""
        return Team.__evaluate_with_minimum(a_place, b_place, self.minimums["place"])

    def set_rest(self, rest: int) -> None:
        """The number of days passed from the last match."""
        self.rest = Team.__input_check(rest, self.maximums["rest"])

    def __compare_rest(self, a_rest: int, b_rest: int) -> tuple:
        """Compares time for rest."""
        return Team.__evaluate_with_maximum(a_rest, b_rest, self.maximums["rest"])

    def set_motivation(self) -> None:
        """The team is motivated to win if it is in first or last 35% of the table."""
        if self.place in (
            list(range(1, int(self.standings * 0.35) + 1))
            + list(range(int(self.standings * 0.65), self.standings + 1))
        ):
            self.motivation = 1
        else:
            self.motivation = 0

    def __compare_motivation(self, a_motivation: int, b_motivation: int) -> tuple:
        """Compares motivation."""
        return Team.__evaluate_with_maximum(
            a_motivation, b_motivation, self.maximums["motivation"]
        )

    def set_mood(self, mood: int) -> None:
        """Result of last match."""
        self.mood = Team.__input_check(mood, self.maximums["mood"])

    def __compare_mood(self, a_mood: int, b_mood: int) -> tuple:
        """Compares moods."""
        return Team.__evaluate_with_maximum(a_mood, b_mood, self.maximums["mood"])

    def change_coeffs(self, new_coeffs: list) -> None:
        """Changes coefficients."""
        self.coeffs = new_coeffs

    def predict(self, opponent: "Team") -> str:
        """Predicts the possible winner of the upcoming match."""
        comparison = []
        comparison.append(
            Team.__update_with_coeff(
                self.__compare_form(self.form, opponent.form),
                self.coeffs["form"],
            )
        )
        comparison.append(
            Team.__update_with_coeff(
                self.__compare_head_to_head(self.head_to_head, opponent.head_to_head),
                self.coeffs["head_to_head"],
            )
        )
        comparison.append(
            Team.__update_with_coeff(
                self.__compare_absent_players(
                    self.absent_players, opponent.absent_players
                ),
                self.coeffs["absent_players"],
            )
        )
        comparison.append(
            Team.__update_with_coeff(
                self.__compare_home_away(self.home_away, opponent.home_away),
                self.coeffs["home_away"],
            )
        )
        comparison.append(
            Team.__update_with_coeff(
                self.__compare_place(self.place, opponent.place),
                self.coeffs["place"],
            )
        )
        comparison.append(
            Team.__update_with_coeff(
                self.__compare_rest(self.rest, opponent.rest),
                self.coeffs["rest"],
            )
        )
        comparison.append(
            Team.__update_with_coeff(
                self.__compare_motivation(self.motivation, opponent.motivation),
                self.coeffs["motivation"],
            )
        )
        comparison.append(
            Team.__update_with_coeff(
                self.__compare_mood(self.mood, opponent.mood),
                self.coeffs["mood"],
            )
        )
        for _ in comparison:
            self.score += _[0]
        opponent.score = 100 - self.score
        print(f"Form: ({self.form}, {opponent.form})")
        print(self.__compare_form(self.form, opponent.form))
        print(f"Head-to-head: ({self.head_to_head}, {opponent.head_to_head})")
        print(self.__compare_head_to_head(self.head_to_head, opponent.head_to_head))
        print(f"Absent players: ({self.absent_players}, {opponent.absent_players})")
        print(
            self.__compare_absent_players(self.absent_players, opponent.absent_players)
        )
        print(f"Home/away: ({self.home_away}, {opponent.home_away})")
        print(self.__compare_home_away(self.home_away, opponent.home_away))
        print(f"Place: ({self.place}, {opponent.place})")
        print(self.__compare_place(self.place, opponent.place))
        print(f"Rest: ({self.rest}, {opponent.rest})")
        print(self.__compare_rest(self.rest, opponent.rest))
        print(f"Motivation: ({self.motivation}, {opponent.motivation})")
        print(self.__compare_motivation(self.motivation, opponent.motivation))
        print(f"Mood: ({self.mood}, {opponent.mood})")
        print(self.__compare_mood(self.mood, opponent.mood))
        print("\nRESULT WITH COEFFS")
        return f"<{self.name} {self.score}%> VS <{opponent.score}% {opponent.name}>"

    def __evaluate_with_maximum(a, b, max_num):
        """Evaluates the percentage."""
        if a == b:
            return 50, 50
        k = (50 * (max([a, b]) - min([a, b])) ** 2) / ((a + b) * max_num)

        if a < b:
            a = round(50 - k, 1)
            b = round(100 - a, 1)
        else:
            b = round(50 - k, 1)
            a = round(100 - b, 1)
        return a, b

    def __evaluate_with_minimum(a, b, min_num):
        """Evaluates the percentage."""
        if a == b:
            return 50, 50
        k = (50 * (max([a, b]) - min([a, b])) ** 2) / ((a + b) * min_num)
        if a < b:
            a = round(50 + k, 1)
            b = round(100 - a, 1)
        else:
            b = round(50 + k, 1)
            a = round(100 - b, 1)
        return a, b

    def __update_with_coeff(pair: tuple, coeff: float) -> tuple:
        """Updates percentage with coefficient."""
        return round(pair[0] * coeff, 1), round(pair[1] * coeff, 1)

    def __input_check(var, scale):
        """Checks whether number is less than one."""
        if var >= scale:
            return scale
        return var


def main():
    """The main fucntion."""
    data = receive_input()
    team_a = Team(data["name"])
    team_a.set_form(data["form"])
    team_a.set_head_to_head(data["head_to_head"])
    team_a.set_absent_players(data["absent_players"])
    team_a.set_standings(data["standings"])
    team_a.set_place(data["place"])
    team_a.set_home_away(data["home_away"])
    team_a.set_rest(data["home_away"])
    team_a.set_motivation()
    team_a.set_mood(data["mood"])

    data = receive_input()
    team_b = Team(data["name"])
    team_b.set_form(data["form"])
    team_b.set_head_to_head(data["head_to_head"])
    team_b.set_absent_players(data["absent_players"])
    team_b.set_standings(data["standings"])
    team_b.set_place(data["place"])
    team_b.set_home_away(data["home_away"])
    team_b.set_rest(data["home_away"])
    team_b.set_motivation()
    team_b.set_mood(data["mood"])

    print(team_a.predict(team_b))


def receive_input():
    """Receives user's input."""
    data = {}
    print("Team name:")
    data["name"] = input(">>> ")
    print("Form:")
    data["form"] = check_int()
    print("Head-to-head:")
    data["head_to_head"] = check_int()
    print("Number of absent players:")
    data["absent_players"] = check_int()
    print("Standings size:")
    data["standings"] = check_int()
    print("Place in the standings:")
    data["place"] = check_int()
    print("Home/away:")
    data["home_away"] = check_int()
    print("Rest:")
    data["rest"] = check_int()
    print("Mood:")
    data["mood"] = check_int()

    print("\nSuccess!\n")
    return data


def check_int():
    """Checks whether input is an integer number."""
    try:
        return int(input(">>> "))
    except ValueError:
        print("Error. Try again.")
        return check_int()


if __name__ == "__main__":
    main()
