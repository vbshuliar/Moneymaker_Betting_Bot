"""Bot to predict the winner of the upcoming soccer match."""


class Team:
    """Information about the soccer team."""

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

    def __init__(self, name: str) -> None:
        """Name of the team."""
        self.name = name

    def set_form(self, form: int) -> None:
        """The number of victories in the last five matches of the league."""
        self.form = form

    def set_head_to_head(self, head_to_head: int) -> None:
        """The number of victories in the last ten head-to-head matches."""
        self.head_to_head = head_to_head

    def set_absent_players(self, absent_players: int) -> None:
        """The number of absent players."""
        self.absent_players = absent_players

    def set_home_away(self, home_away: int) -> None:
        """The number of victories in all home/away matches of the league."""
        self.home_away = home_away

    def set_standings(self, place: int, standings: int) -> None:
        """Place in the standings."""
        self.place = place
        self.standings = standings

    def set_rest(self, rest: int) -> None:
        """The number of days passed from the last match."""
        self.rest = rest

    def set_motivation(self) -> None:
        """The team is motivated to win if it is in first or last 35% of the table."""
        pass

    def set_mood(self, mood: int) -> None:
        """Result of last match."""
        self.mood = mood

    def change_coeffs(self, new_coeffs: list) -> None:
        """Changes coefficients."""
        self.coeffs = new_coeffs

    def predict(self, opponent) -> str:
        """Predicts the possible winner of the upcoming match."""
        self.__zip()
        opponent.__zip()

    def __compress(self):
        """Compresses all the information about the team."""
        self.data = list(self.__dict__.values())[1:]


if __name__ == "__main__":
    team_a = Team("Barcelona")
    team_a.set_form(0)
    team_a.set_head_to_head(1)
    team_a.set_absent_players(2)
    team_a.set_home_away(5)
    team_a.set_standings(3)
    team_a.set_rest(6)
    team_a.set_motivation(45)
    team_a.set_mood(2)

    team_b = Team("Lazio")
    team_b.set_form(1)
    team_b.set_head_to_head(2)
    team_b.set_absent_players(3)
    team_b.set_home_away(10)
    team_b.set_standings(7)
    team_b.set_rest(9)
    team_b.set_motivation(55)
    team_b.set_mood(6)
    print(type(team_a))
    print(type([]))

    print(team_a.predict(team_b))
