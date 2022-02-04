def main():
    form = score_formula(input(), 0.25)
    head_to_head = score_formula(input())
    absent_players = 
    home_away =
    standings =
    time_for_rest = 
    motivation
    mood
    return a, b


def form(var):
    pass


def head_to_head(var):
    pass


def absent_players(var):
    pass


def home_away(var):
    pass


def standings(var):
    pass


def time_for_rest(var):
    pass


def motivation(var):
    pass


def mood(var):
    pass


def score_formula(var, cf):
    a, b = list(map(lambda x: int(x), var.split()))
    a, b = round(100/(a+b)*a*cf), round(100/(a+b)*b*cf)
    return a, b


if __name__ == "__main__":
    print(main())
