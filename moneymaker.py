def main():
    a_name = input("\nFirst team name: ")
    b_name = input("\nSecond team name: ")
    form = score_formula(input("\nForm: "), 0.25, a_name, b_name)
    head_to_head = score_formula(input("Head-to-head: "), 0.2, a_name, b_name)
    absent_players = score_formula(input("Absent players: "), 0.15, a_name, b_name)
    print("(Score displayed reversed)")
    home_away = score_formula(input("\nHome-away: "), 0.15, a_name, b_name)
    table = input("Standings: ")
    standings = score_formula(standings_evaluation(table), 0.1, a_name, b_name)
    time_for_rest = score_formula(time_for_rest_evaluation(input("Time for rest: ")), 0.05, a_name, b_name)
    motivation = motivation_evaluation(table, a_name, b_name)
    mood = score_formula(mood_evaluation(input("Mood: ")), 0.05, a_name, b_name)

    a, b = form[0] + head_to_head[0] + absent_players[1] + home_away[0] +\
        standings[0] + time_for_rest[0] + motivation[0] + mood[0],\
        form[1] + head_to_head[1] + absent_players[0] + home_away[1] +\
        standings[1] + time_for_rest[1] + motivation[1] + mood[1]

    return f"""
Winning chance of {a_name} is {a}%
Winnings chance of {b_name} is {b}%
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
    c, a, b = list(map(int, var.split()))
    a, b = round(10/c*a), round(10/c*b)
    a, b = 5 if a in range(0, 4) or a in range(8, 10) else 0, \
        5 if b in range(0, 4) or b in range(8, 10) else 0
    if a == b:
        a, b = 2.5, 2.5

    print(f"""Motivation:

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
    try:
        a, b = round(100/(a+b)*a*cf, 1), round(100/(a+b)*b*cf, 1)
    except ZeroDivisionError:
        if a == 0 and b == 0:
            a, b = round(100*cf/2, 1), round(100*cf/2, 1)
        elif b == 0:
            a, b = 100*cf, 0
        else:
            a, b = 0, 100*cf

    print(f"""
{a_name} gets {a} points
{b_name} gets {b} points
""")

    return a, b


if __name__ == "__main__":
    print(main())
