from datetime import datetime


class Challenge:
    day: int
    part1_solve_time: int
    part2_solve_time: int

    def __init__(self, challenge_day: str, day_info: dict):
        self.day = int(challenge_day)

        try:
            self.part1_solve_time = datetime.fromtimestamp(
                int(day_info['1']['get_star_ts']))
        except KeyError:
            self.part1_solve_time = None

        try:
            self.part2_solve_time = datetime.fromtimestamp(
                int(day_info['2']['get_star_ts']))
        except KeyError:
            self.part2_solve_time = None

    def __repr__(self):
        return f'Day: {self.day}'
