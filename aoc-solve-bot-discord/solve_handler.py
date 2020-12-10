from __future__ import annotations
import config
import logging
import datetime
from announcer import Announcer
from api_session import session as s
from member import Member
from json.decoder import JSONDecodeError


class Solve_Handler:
    host: str

    def __init__(self):
        super().__init__()
        self.announcer = Announcer()

    def get_solves(self):
        logging.debug("GETTING SOLVES")

        try:
            res = s.get()
            data = res
        except Exception as e:
            print(e)
            return

        try:
            data = res.json()
        except (ValueError, JSONDecodeError, KeyError) as e:
            print(e)
            data = []

        members: [Member] = []
        for member_id, member_info in data['members'].items():
            member = Member(member_info)
            members.append(member)

        day: int = datetime.datetime.now().day
        print(f'{day=}')
        # day: int = 10
        solves = {}
        for member in members:
            challenge_stats = member.get_challenge(day)
            if challenge_stats:
                solves[member.name] = challenge_stats

        self.announcer.announce(day, solves)
