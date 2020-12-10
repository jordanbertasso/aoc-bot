import schedule
import logging

from solve_handler import Solve_Handler


def main():
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)

    handler = logging.FileHandler("./data/aoc-solve-bot-discord.log")
    handler.setLevel(logging.INFO)
    logging.getLogger().addHandler(handler)

    solve_handler = Solve_Handler()

    schedule.every().day.at("20:00").do(solve_handler.get_solves)

    # schedule.every(5).seconds.do(solve_handler.get_solves)

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    main()
