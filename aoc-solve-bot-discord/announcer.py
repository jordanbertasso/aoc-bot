from __future__ import annotations
import requests
import json
import config
import time
import logging
import datetime
from discord import Embed
from json.decoder import JSONDecodeError


class Announcer:
    webhook_data: dict
    solve_string: str
    first_blood_string: str
    rate_limit_remaining: int
    rate_limit_sleep_time: int

    def __init__(self):
        self.webhook_url = config.webhook_url
        self.webhook_data = json.loads(
            requests.get(self.webhook_url).content.decode())
        self.rate_limit_remaining = 1
        self.rate_limit_sleep_time = 0

    def format_time_delta(self, td: datetime.timedelta):
        s = td.total_seconds()

        hours = int(s // 3600)

        s = s - (hours * 3600)

        minutes = int(s // 60)

        seconds = int(s - (minutes * 60))

        if hours:
            return f'{hours}h {minutes}m {seconds}s'
        elif minutes:
            return f'{minutes}m {seconds}s'
        else:
            return f'{seconds}s'

    def sort_challenge(self, item):
        challenge = item[1]

        if not challenge.part2_solve_time:
            p2 = datetime.datetime.max
        else:
            p2 = challenge.part2_solve_time

        return (p2, challenge.part1_solve_time)

    def announce(self, day: int, solves: {name, [Challenge]}):
        self.check_rate_limits()

        e = Embed()
        e.title = f'Day {day} Summary'
        e.set_thumbnail(url='https://adventofcode.com/favicon.png')
        e.url = 'https://adventofcode.com/2020/leaderboard/private/view/373020'
        e.colour = 0xFFFF74

        solves = dict(sorted(solves.items(), key=self.sort_challenge))

        for name, challenge in solves.items():
            d = datetime.datetime.now()
            time_taken1 = self.format_time_delta(
                challenge.part1_solve_time -
                datetime.datetime(d.year, d.month, d.day, 16))
                # datetime.datetime(d.year, d.month, 10, 16))

            try:
                time_taken2 = self.format_time_delta(
                    challenge.part2_solve_time -
                    datetime.datetime(d.year, d.month, d.day, 16))
            except Exception as ex:
                time_taken2 = None
                print(ex)

            if time_taken2:
                e.add_field(
                    name=name,
                    value=f"Part 1: {time_taken1}\nPart 2: {time_taken2}")
            else:
                e.add_field(name=name, value=f"Part 1: {time_taken1}")

        self.webhook_data["embeds"] = [e.to_dict()]
        print(self.webhook_data)

        res = requests.post(self.webhook_url, json=self.webhook_data)

        # Unavoidable and unpredictable webhook specific rate-limit from Discord
        # Retry if limited
        # https://github.com/discord/discord-api-docs/issues/1454
        self.check_429(res)

        self.update_rate_limits(res)

    def update_rate_limits(self, res):
        try:
            self.rate_limit_remaining = min(
                int(res.headers["X-RateLimit-Remaining"]),
                int(res.headers["X-RateLimit-Global"]))
        except KeyError:
            self.rate_limit_remaining = int(
                res.headers["X-RateLimit-Remaining"])

        self.rate_limit_sleep_time = int(
            res.headers["X-RateLimit-Reset-After"])

        logging.debug(f"Bucket {res.headers['X-RateLimit-Bucket']}")
        logging.debug(res.status_code)
        logging.debug(f"{self.rate_limit_remaining=}")
        logging.debug(f"{self.rate_limit_sleep_time=}")

    def check_rate_limits(self):
        if self.rate_limit_remaining == 0:
            secs = self.rate_limit_sleep_time
            logging.info(f"Sleeping for {secs}s - Rate Limits\n")
            time.sleep(secs)

    def check_429(self, res):
        if res.status_code == 429:

            try:
                json = logging.debug(res.json())
                self.rate_limit_sleep_time = json["retry_after"] / 1000
            except (ValueError, JSONDecodeError, KeyError) as e:
                print(e)
                self.rate_limit_sleep_time = 60

            logging.info(
                f"429 Received - Sleeping for {self.rate_limit_sleep_time}s")
            time.sleep(self.rate_limit_sleep_time)
            res = requests.post(self.webhook_url, json=self.webhook_data)
