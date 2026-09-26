import importlib
import sys
from typing import Any


def _get_game() -> Any:
    game = sys.modules.get("__main__")
    if game is None or not hasattr(game, "money"):
        game = importlib.import_module("breadclicker")
    return game


achievements = {
    "First Click": {
        "description": "Click the bread for the first time.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().money >= 1,
        "icon": "👆"
    },
    "Bread Hoarder": {
        "description": "Accumulate 1000 money.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().money >= 1000,
        "icon": "💰"
    },
    "Grandma's Helper": {
        "description": "Own your first Grandma.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().grandmas_owned >= 1,
        "icon": "👵"
    },
    "Farm Owner": {
        "description": "Own your first Bread Farm.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().farms_owned >= 1,
        "icon": "🌾"
    },
    "Mine Operator": {
        "description": "Own your first Bread Mine.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().mines_owned >= 1,
        "icon": "⛏️"
    },
    "Azia's Worker Employer": {
        "description": "Own your first Worker from Azia.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().workers_from_azia_owned >= 1,
        "icon": "👷"
    },
    "Low Paid Person Employer": {
        "description": "Own your first Low Paid Person.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().low_paid_people_owned >= 1,
        "icon": "🧑‍💼"
    },
    "Robber Employer": {
        "description": "Own your first Robber.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().robbers_owned >= 1,
        "icon": "🕵️"
    },
    "Money Millionaire": {
        "description": "Accumulate 1,000,000 money.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().money >= 1000000,
        "icon": "🤑"
    },
    "Clicking Addict": {
        "description": "Click the bread 10,000 times.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().times_clicked >= 10000,
        "icon": "🖱️"
    },
    "Grandma Collector": {
        "description": "Own 100 Grandmas.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().grandmas_owned >= 100,
        "icon": "👵"
    },
    "Farm Collector": {
        "description": "Own 100 Bread Farms.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().farms_owned >= 100,
        "icon": "🚜"
    },
    "Mine Collector": {
        "description": "Own 100 Bread Mines.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().mines_owned >= 100,
        "icon": "⛏️"
    },
    "Azia's Worker Collector": {
        "description": "Own 100 Workers from Azia.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().workers_from_azia_owned >= 100,
        "icon": "🏗️"
    },
    "Low Paid Person Collector": {
        "description": "Own 100 Low Paid People.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().low_paid_people_owned >= 100,
        "icon": "👨‍💼"
    },
    "Robber Collector": {
        "description": "Own 100 Robbers.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().robbers_owned >= 100,
        "icon": "💣"
    },
    "Badger Owner": {
        "description": "Own your first Badger.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().badger_owned >= 1,
        "icon": "🦡"
    },
    "Badger Collector": {
        "description": "Own 100 Badgers.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().badger_owned >= 100,
        "icon": "🐾"
    },
    "Music Lover": {
        "description": "Change the background music.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().current_song_index != 0,
        "icon": "🎵"
    },
    "Color Customizer": {
        "description": "Change the background color.",
        "unlocked": False,
        "unlock_condition": lambda: _get_game().bg != (139, 204, 55),
        "icon": "🎨"
    },
}


def check_achievements():
    game = _get_game()
    for name, info in achievements.items():
        if not info["unlocked"] and info["unlock_condition"]():
            info["unlocked"] = True


def open_achievements():
    game = _get_game()
    game.settings_open = False
    check_achievements()
    game.achievements_opened = True


def close_achievements():
    game = _get_game()
    game.achievements_opened = False


def toggle_achievements():
    game = _get_game()
    if game.achievements_opened:
        close_achievements()
    else:
        open_achievements()
