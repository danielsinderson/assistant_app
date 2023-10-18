"""

"""

default_criteria: list[tuple[str, float]] = [
    ("pro-social goodness", 1.0),
    ("intrinsic goodness", 1.0),
    ("money money money", 1.0)
]


def ask_for_criteria() -> list[tuple[str, float]]:
    criteria = input("Please input your criteria in the following format \
                     criteria2:weight2,criteria2:weight2,etc. \
                     or press [enter] to use the default criteria:\n")
    if criteria == "":
        return default_criteria
    
    criteria_list = [(elem.split(':')[0], float(elem.split(':')[1])) for elem in criteria.split(',')]
    print(criteria_list)
    return criteria_list


def ask_for_options(criteria: list) -> list[tuple[str, float]]:
    results: dict[str, float] = {}
    while True:
        option_name = input("Type out your next option, or press [enter] to move on: ")
        
        if option_name == "":
            return results
        
        total_score = 0
        for criterion in criteria:
            criterion_score = float(input(f"Please assign a score for {criterion[0]}: "))
            total_score += criterion_score * criterion[1]
        
        results[option_name] = total_score


def main():
    criteria: list[tuple[str, float]] = ask_for_criteria()
    options: dict[str, float] = ask_for_options(criteria)
    for option, value in options.items():
        print(f"{option} has a score of {value}.")



if __name__ == "__main__":
    main()