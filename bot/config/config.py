import os
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str
    admin_ids: set[int]
    language: str


@dataclass
class Miscellaneous:
    path_to_db: str
    telegraph_token: str


@dataclass
class Config:
    tg_bot: TgBot
    misc: Miscellaneous


def load_config():
    return Config(
        tg_bot=TgBot(
            admin_ids=set(map(int, os.getenv('ADMIN_IDS').split(';'))),
            language=os.getenv('LANGUAGE'),
            token=os.getenv('BOT_TOKEN')
        ),
        misc=Miscellaneous(
            path_to_db=os.getenv('PATH_TO_DB'),
            telegraph_token=os.getenv('TELEGRAPH_TOKEN')
        )
    )
