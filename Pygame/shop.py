import importlib
import sys
from typing import Any


def _get_game() -> Any:
    game = sys.modules.get("__main__")
    if game is None or not hasattr(game, "money"):
        game = importlib.import_module("breadclicker")
    return game


SHOP_X = 240
SHOP_Y = 0
SHOP_WIDTH = 205
SHOP_HEIGHT = 600
SHOP_HEADER_HEIGHT = 60
SHOP_ITEM_HEIGHT = 90
SHOP_ITEM_PADDING = 10

def get_discounted_price(price: int) -> int:
    game = _get_game()
    return max(1, int(round(price * game.price_discount)))


def check_shop_locked() -> bool:
    game = _get_game()
    return game.shop_locked


def buy_grandma():
    game = _get_game()
    actual_price = get_discounted_price(game.price_grandma)
    if game.money >= actual_price:
        game.money -= actual_price
        game.grandmas_owned += 1
        game.money_per_second += 1
        game.price_grandma = int(round(100 * (1.15 ** game.grandmas_owned)))


def buy_bread_farm():
    game = _get_game()
    actual_price = get_discounted_price(game.price_farm)
    if game.money >= actual_price:
        game.money -= actual_price
        game.farms_owned += 1
        game.money_per_second += 15
        game.price_farm = int(round(1000 * (1.15 ** game.farms_owned)))


def buy_bread_mine():
    game = _get_game()
    actual_price = get_discounted_price(game.price_mine)
    if game.money >= actual_price:
        game.money -= actual_price
        game.mines_owned += 1
        game.money_per_second += 100
        game.price_mine = int(round(10000 * (1.15 ** game.mines_owned)))


def buy_worker_from_azia():
    game = _get_game()
    actual_price = get_discounted_price(game.price_worker_from_azia)
    if game.money >= actual_price:
        game.money -= actual_price
        game.workers_from_azia_owned += 1
        game.money_per_second += 500
        game.price_worker_from_azia = int(round(50000 * (1.15 ** game.workers_from_azia_owned)))


def buy_low_paid_person():
    game = _get_game()
    actual_price = get_discounted_price(game.price_low_paid_people)
    if game.money >= actual_price:
        game.money -= actual_price
        game.low_paid_people_owned += 1
        game.money_per_second += 2500
        game.price_low_paid_people = int(round(250000 * (1.15 ** game.low_paid_people_owned)))


def buy_robber():
    game = _get_game()
    actual_price = get_discounted_price(game.price_robber)
    if game.money >= actual_price:
        game.money -= actual_price
        game.robbers_owned += 1
        game.money_per_second += 10000
        game.price_robber = int(round(1000000 * (1.15 ** game.robbers_owned)))


def buy_badger():
    game = _get_game()
    if game.money >= game.price_badger:
        game.money -= game.price_badger
        game.badger_owned += 1
        game.price_badger = int(round(2500000 * (1.15 ** game.badger_owned)))

def buy_event_display():
    game = _get_game()
    actual_price = get_discounted_price(game.price_event_display)
    if game.money >= actual_price and game.event_display_owned < 1:
        game.money -= actual_price
        game.event_display_owned += 1
        game.price_event_display = int(round(10000000 * (1.15 ** game.event_display_owned)))
        for item in shop_items:
            if item.get("name") == "Event display":
                item["hidden"] = True
                item["button_rect"] = None
                break
    else:
        for idx, item in enumerate(shop_items):
            if item.get("name") == "Event display":
                item["button_warning"] = 1.0
                break

def buy_chinese_woman():
    game = _get_game()
    actual_price = get_discounted_price(game.price_chinese_woman)
    if game.money >= actual_price:
        game.money -= actual_price
        game.chinese_woman_owned += 1
        game.price_chinese_woman = int(round(10000000 * (1.15 ** game.chinese_woman_owned)))


shop_items = [
    {
        "name": "Grandma",
        "description": "+1 money per second",
        "price": lambda: get_discounted_price(_get_game().price_grandma),
        "action": buy_grandma,
        "button_rect": None,
        "button_colour": (150, 150, 150),
        "button_warning": 0.0,
    },
    {
        "name": "Bread Farm",
        "description": "Generates 15 money per second",
        "price": lambda: get_discounted_price(_get_game().price_farm),
        "action": buy_bread_farm,
        "button_rect": None,
        "button_colour": (150, 150, 150),
        "button_warning": 0.0,
    },
    {
        "name": "Bread Mine",
        "description": "Generates 100 money per second",
        "price": lambda: get_discounted_price(_get_game().price_mine),
        "action": buy_bread_mine,
        "button_rect": None,
        "button_colour": (150, 150, 150),
        "button_warning": 0.0,
    },
    {
        "name": "Worker from Asia",
        "description": "Generates 500 money per second",
        "price": lambda: get_discounted_price(_get_game().price_worker_from_azia),
        "action": buy_worker_from_azia,
        "button_rect": None,
        "button_colour": (150, 150, 150),
        "button_warning": 0.0,
    },
    {
        "name": "Low Paid Person",
        "description": "Generates 2500 money per second",
        "price": lambda: get_discounted_price(_get_game().price_low_paid_people),
        "action": buy_low_paid_person,
        "button_rect": None,
        "button_colour": (150, 150, 150),
        "button_warning": 0.0,
    },
    {
        "name": "Robber",
        "description": "Generates 10000 money per second",
        "price": lambda: get_discounted_price(_get_game().price_robber),
        "action": buy_robber,
        "button_rect": None,
        "button_colour": (150, 150, 150),
        "button_warning": 0.0,
    },
    {
        "name": "Badger",
        "description": "Is afk, generates +1k/hour from the last time game was closed",
        "price": lambda: get_discounted_price(_get_game().price_badger),
        "action": buy_badger,
        "button_rect": None,
        "button_colour": (150, 150, 150),
        "button_warning": 0.0,
    },
    {
        "name": "Event display",
        "description": "Shows the time left till the event",
        "price": lambda: get_discounted_price(_get_game().price_event_display),
        "action": buy_event_display,
        "button_rect": None,
        "button_colour": (150, 150, 150),
        "button_warning": 0.0,
        "hidden": False,
    },
    {
        "name": "Chinese woman",
        "description": "Generates 1 azian person every 30 seconds",
        "price": lambda: get_discounted_price(_get_game().price_chinese_woman),
        "action": buy_chinese_woman,
        "button_rect": None,
        "button_colour": (150, 150, 150),
        "button_warning": 0.0,
    }
]
