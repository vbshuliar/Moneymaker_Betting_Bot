def main():
    a_name = input("First team name: ")
    b_name = input("Second team name: ")
    form = score_formula(input("Form: "), 0.25, a_name, b_name)
    head_to_head = score_formula(input("Head-to-head: "), 0.2, a_name, b_name)
    absent_players = score_formula(input("Absent players: "), 0.15, a_name, b_name)
    home_away = score_formula(input("Home-away: "), 0.15, a_name, b_name)
    standings = score_formula(standings_evaluation(input("Standings: ")), 0.1, a_name, b_name)
    time_for_rest = score_formula(time_for_rest_evaluation(input("Time for rest: ")), 0.05, a_name, b_name)
    motivation = motivation_evaluation(standings, a_name, b_name)
    mood = score_formula(mood_evaluation(input("Mood: ")), 0.05, a_name, b_name)

    a = form[0] + head_to_head[0] + absent_players[1] + home_away[0] +\
        standings[0] + time_for_rest[0] + motivation[0] + mood[0]

    return f"""
Winning chance of {a_name} is {a}%
Winnings chance of {b_name} is {100-a}%
"""


def standings_evaluation(var):
    c, a, b = list(map(int, var.split()))

    return f"{round(100/c*a)} {round(100/c*b)}"


def time_for_rest_evaluation(var):
    a, b = list(map(int, var.split()))
    if a >= 4:
        a = 4
    if b >= 4:
        b = 4

    return f"{a} {b}"


def motivation_evaluation(var, a_name, b_name):
    a, b = 5 if var[0] in [1, 2, 3, 8, 9, 10] else 0, \
        5 if var[1] in [1, 2, 3, 8, 9, 10] else 0

    print(f"""
{a_name} gets {a} points!
{b_name} gets {b} points!
""")

    return [a, b]


def mood_evaluation(var):
    var = var.split()
    a, b = 1 if var[0] == "W" else 0, 1 if var[1] == "W" else 0

    return f"{a} {b}"


def score_formula(var, cf, a_name, b_name):
    a, b = list(map(lambda x: int(x), var.split()))
    a, b = round(100/(a+b)*a*cf), round(100/(a+b)*b*cf)

    print(f"""
{a_name} gets {a} points!
{b_name} gets {b} points!
""")

    return a, b


print(main())
