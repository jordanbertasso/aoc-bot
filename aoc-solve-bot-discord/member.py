from __future__ import annotations
from challenge import Challenge


class Member:
    id: int
    name: str
    challenges: [Challenge]

    def __init__(self, member_info: dict):
        self.id = member_info['id']
        self.name = member_info['name']
        self.challenges = [
            Challenge(challenge_day, day_info) for challenge_day, day_info in
            member_info['completion_day_level'].items()
        ]

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, levels: {self.challenges}"

    def get_challenge(self, day: int):
        for challenge in self.challenges:
            if challenge.day == day:
                return challenge
