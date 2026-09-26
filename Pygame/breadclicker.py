import pygame
import pygame_widgets
import os
    
import random
import tkinter as tk
from tkinter import colorchooser
import time
import json
import settings
import shop
import achievements as achievements_module

SKINS_DIR = os.path.join(os.path.dirname(__file__), "Skins")
skin_definitions = [
    {
        "id": "default",
        "display_name": "Default",
        "description": "Default skin",
        "achievement_key": None,
        "achievement_name": "Default",
        "icon": "🍞",
        "image_file": "bread.png",
    },
    {
        "id": "first_click",
        "display_name": "First Click Skin",
        "description": "Unlocked by the 'First Click' achievement.",
        "achievement_key": "First Click",
        "achievement_name": "First Click",
        "icon": "👆",
        "image_file": "first_click.png",
    },
    {
        "id": "bread_hoarder",
        "display_name": "Bread Hoarder Skin",
        "description": "Unlocked by the 'Bread Hoarder' achievement.",
        "achievement_key": "Bread Hoarder",
        "achievement_name": "Bread Hoarder",
        "icon": "💰",
        "image_file": "bread_horderer.webp",
    },
    {
        "id": "grandmas_helper",
        "display_name": "Grandma's Helper Skin",
        "description": "Unlocked by the 'Grandma's Helper' achievement.",
        "achievement_key": "Grandma's Helper",
        "achievement_name": "Grandma's Helper",
        "icon": "👵",
        "image_file": "grandmas_helper.png",
    },
    {
        "id": "farm_owner",
        "display_name": "Farm Owner Skin",
        "description": "Unlocked by the 'Farm Owner' achievement.",
        "achievement_key": "Farm Owner",
        "achievement_name": "Farm Owner",
        "icon": "🌾",
        "image_file": "farm_owner.jpg",
    },
    {
        "id": "mine_operator",
        "display_name": "Mine Operator Skin",
        "description": "Unlocked by the 'Mine Operator' achievement.",
        "achievement_key": "Mine Operator",
        "achievement_name": "Mine Operator",
        "icon": "⛏️",
        "image_file": "mine_operator.png",
    },
    {
        "id": "azia_worker_employer",
        "display_name": "Azia's Worker Employer Skin",
        "description": "Unlocked by the 'Azia's Worker Employer' achievement.",
        "achievement_key": "Azia's Worker Employer",
        "achievement_name": "Azia's Worker Employer",
        "icon": "👷",
        "image_file": "azian_worker_empolayer.png",
    },
    {
        "id": "low_paid_person_employer",
        "display_name": "Low Paid Person Employer Skin",
        "description": "Unlocked by the 'Low Paid Person Employer' achievement.",
        "achievement_key": "Low Paid Person Employer",
        "achievement_name": "Low Paid Person Employer",
        "icon": "🧑‍💼",
        "image_file": "low_paid_people_employer.jpg",
    },
    {
        "id": "robber_employer",
        "display_name": "Robber Employer Skin",
        "description": "Unlocked by the 'Robber Employer' achievement.",
        "achievement_key": "Robber Employer",
        "achievement_name": "Robber Employer",
        "icon": "🕵️",
        "image_file": "robber_empoyer.webp",
    },
    {
        "id": "money_millionaire",
        "display_name": "Money Millionaire Skin",
        "description": "Unlocked by the 'Money Millionaire' achievement.",
        "achievement_key": "Money Millionaire",
        "achievement_name": "Money Millionaire",
        "icon": "💵",
        "image_file": "money_millionare.jpg",
    },
    {
        "id": "clicking_addict",
        "display_name": "Clicking Addict Skin",
        "description": "Unlocked by the 'Clicking Addict' achievement.",
        "achievement_key": "Clicking Addict",
        "achievement_name": "Clicking Addict",
        "icon": "🖱️",
        "image_file": "clicking_addict.png",
    },
    {
        "id": "grandma_collector",
        "display_name": "Grandma Collector Skin",
        "description": "Unlocked by the 'Grandma Collector' achievement.",
        "achievement_key": "Grandma Collector",
        "achievement_name": "Grandma Collector",
        "icon": "👵",
        "image_file": None,
    },
    {
        "id": "farm_collector",
        "display_name": "Farm Collector Skin",
        "description": "Unlocked by the 'Farm Collector' achievement.",
        "achievement_key": "Farm Collector",
        "achievement_name": "Farm Collector",
        "icon": "🌾",
        "image_file": None,
    },
    {
        "id": "mine_collector",
        "display_name": "Mine Collector Skin",
        "description": "Unlocked by the 'Mine Collector' achievement.",
        "achievement_key": "Mine Collector",
        "achievement_name": "Mine Collector",
        "icon": "⛏️",
        "image_file": None,
    },
    {
        "id": "robber_collector",
        "display_name": "Robber Collector Skin",    
        "description": "Unlocked by the 'Robber Collector' achievement.",
        "achievement_key": "Robber Collector",
        "achievement_name": "Robber Collector",
        "icon": "🕵️",
        "image_file": None,
    },
    {
        "id": "badger_collector",
        "display_name": "Badger Collector Skin",
        "description": "Unlocked by the 'Badger Collector' achievement.",
        "achievement_key": "Badger Collector",
        "achievement_name": "Badger Collector",
        "icon": "🦡",
        "image_file": None,
    },
    {
        "id": "chinese_woman_collector",
        "display_name": "Chinese Woman Collector Skin",
        "description": "Unlocked by the 'Chinese Woman Collector' achievement.",
        "achievement_key": "Chinese Woman Collector",
        "achievement_name": "Chinese Woman Collector",
        "icon": "🧕",
        "image_file": None,
    }
]
for name, info in achievements_module.achievements.items():
    skin_definitions.append({
        "id": f"skin_{len(skin_definitions)}",
        "display_name": f"{name} Skin",
        "description": f"Unlocked by the '{name}' achievement.",
        "achievement_key": name,
        "achievement_name": name,
        "icon": info.get("icon", "🎨"),
        "image_file": None,
    })

skin_image_cache = {}


def load_skin_image(image_file):
    if image_file in skin_image_cache:
        return skin_image_cache[image_file]

    image_path = os.path.join(SKINS_DIR, image_file)
    if not os.path.exists(image_path):
        skin_image_cache[image_file] = None
        return None

    try:
        image = pygame.image.load(image_path).convert_alpha()
        skin_image_cache[image_file] = image
        return image
    except Exception as exc:
        print(f"Could not load skin image '{image_file}': {exc}")
        skin_image_cache[image_file] = None
        return None


def get_skin_preview_image(skin):
    image_file = skin.get("image_file")
    if not image_file:
        return None
    return load_skin_image(image_file)


def wrap_text(text, font, max_width):
    words = text.split()
    if not words:
        return []

    lines = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        if font.size(test)[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def is_skin_unlocked(skin):
    return skin["achievement_key"] is None or achievements_module.achievements.get(skin["achievement_key"], {}).get("unlocked", False)


def open_skins():
    global skins_opened, achievements_opened, settings_open
    settings_open = False
    achievements_opened = False
    skins_opened = True


def close_skins():
    global skins_opened
    skins_opened = False


def toggle_skins():
    global skins_opened, achievements_opened, settings_open
    if skins_opened:
        skins_opened = False
    else:
        skins_opened = True
        achievements_opened = False
        settings_open = False

from pygame_widgets.slider import Slider
from pygame_widgets.button import Button

pygame.init()

# -----------------
# Window setup
# -----------------
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bread Clicker")
pygame.display.set_icon(pygame.transform.smoothscale(pygame.image.load(os.path.join(os.path.dirname(__file__), "Skins", "bread.png")), (32, 32)))
pygame.display.set_allow_screensaver(False)


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 24)
emoji_font = pygame.font.SysFont("Segoe UI Emoji", 24)

fps = 60
money = 0
bg = (139, 204, 55)
VERSION = "BETA 1.0"
# -----------------
# sound setup
# -----------------

music_volume = 0.5
sound_volume = 0.5
pygame.mixer.init()

click_sound_path = os.path.join(os.path.dirname(__file__), "Sounds", "click_sound.wav")
try:
    click_sound = pygame.mixer.Sound(click_sound_path)
except Exception as e:
    print(f"Failed to load sound '{click_sound_path}':", e)
    click_sound = None

music_path = os.path.join(os.path.dirname(__file__), "Sounds", "background_music.mp3")
raining_tacos_path = os.path.join(os.path.dirname(__file__), "Sounds", "raining_tacos.mp3")
pancake_song_path = os.path.join(os.path.dirname(__file__), "Sounds", "pancake_song.mp3")

songs = [music_path, raining_tacos_path, pancake_song_path]
current_song_index = 0
pygame.mixer.music.load(songs[current_song_index])
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(music_volume)

if click_sound:
    click_sound.set_volume(sound_volume)

# -----------------
# Upgrade info
# ------------------
money_per_second = 0
#grandmas
grandmas_owned = 0
price_grandma = int(round(100 * (1.15 ** grandmas_owned)))
#bread farms
farms_owned = 0
price_farm = int(round(1000 * (1.15 ** farms_owned)))
#bread mines
mines_owned = 0
price_mine = int(round(10000 * (1.15 ** mines_owned)))
#workers from azia
workers_from_azia_owned = 0
price_worker_from_azia = int(round(50000 * (1.15 ** workers_from_azia_owned)))
#low paid people
low_paid_people_owned = 0
price_low_paid_people = int(round(250000 * (1.15 ** low_paid_people_owned)))
#robbers
robbers_owned = 0
price_robber = int(round(1000000 * (1.15 ** robbers_owned)))
#event display
event_display_owned = 0
price_event_display = int(round(10000000 * (1.15 ** event_display_owned)))
#badger
badger_owned = 0
price_badger = int(round(2500000 * (1.15 ** badger_owned)))
#chinese woman
chinese_woman_owned = 0
price_chinese_woman = int(round(10000000 * (1.15 ** chinese_woman_owned)))


money_earned_multiplier = 1.0
price_discount = 1.0
shop_locked = False
active_custom_events = []
event_message = ""
event_message_time = 0.0
last_opened_time = time.time()
auto_save_timer = 0.0
settings_open = False
skin_selector_open = False

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

# -----------------
# Helper functions
# -----------------

def get_earned_money(amount):
    return int(amount * money_earned_multiplier)


def format_money(value: int) -> str:
    try:
        n = int(value)
    except Exception:
        return str(value)

    abs_n = abs(n)
    if abs_n >= 1_000_000_000_000:
        v = n / 1_000_000_000_000
        suffix = "tril"
    elif abs_n >= 1_000_000_000:
        v = n / 1_000_000_000
        suffix = "bil"
    elif abs_n >= 1_000_000:
        v = n / 1_000_000
        suffix = "mil"
    elif abs_n >= 1_000:
        v = n / 1_000
        suffix = "k"
    else:
        return str(n)

    # Show integer if exact, otherwise one decimal place
    if float(v).is_integer():
        formatted = f"{int(v)}{suffix}"
    else:
        formatted = f"{round(v,1)}{suffix}"

    return formatted


def save_game_data():
    global last_opened_time
    last_opened_time = time.time()
    data = {
        "money": money,
        "grandmas_owned": grandmas_owned,
        "farms_owned": farms_owned,
        "mines_owned": mines_owned,
        "workers_from_azia_owned": workers_from_azia_owned,
        "low_paid_people_owned": low_paid_people_owned,
        "robbers_owned": robbers_owned,
        "badger_owned": badger_owned,
        "chinese_woman_owned": chinese_woman_owned,
        "event_display_owned": event_display_owned,
        "current_song_index": current_song_index,
        "last_opened_time": last_opened_time,
            "achievements_unlocked": {name: info["unlocked"] for name, info in achievements_module.achievements.items()},
        "selected_skin_id": selected_skin_id,
    }
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print("Failed to save game data:", e)


def load_game_data():
    global money, grandmas_owned, farms_owned, mines_owned, workers_from_azia_owned, chinese_woman_owned
    global low_paid_people_owned, robbers_owned, badger_owned, event_display_owned, current_song_index
    global price_grandma, price_farm, price_mine, price_worker_from_azia, price_chinese_woman
    global price_low_paid_people, price_robber, price_badger, price_event_display, money_per_second
    global last_opened_time, selected_skin_id

    if not os.path.exists(DATA_FILE):
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print("Failed to load game data:", e)
        return

    money = int(data.get("money", money))
    grandmas_owned = int(data.get("grandmas_owned", grandmas_owned))
    farms_owned = int(data.get("farms_owned", farms_owned))
    mines_owned = int(data.get("mines_owned", mines_owned))
    workers_from_azia_owned = int(data.get("workers_from_azia_owned", workers_from_azia_owned))
    low_paid_people_owned = int(data.get("low_paid_people_owned", low_paid_people_owned))
    robbers_owned = int(data.get("robbers_owned", robbers_owned))
    badger_owned = int(data.get("badger_owned", badger_owned))
    event_display_owned = int(data.get("event_display_owned", event_display_owned))
    chinese_woman_owned = int(data.get("chinese_woman_owned", chinese_woman_owned))
    selected_skin_id = data.get("selected_skin_id", selected_skin_id)
    if selected_skin_id not in {skin["id"] for skin in skin_definitions}:
        selected_skin_id = "default"
    current_song_index = int(data.get("current_song_index", current_song_index))

    price_grandma = int(round(100 * (1.15 ** grandmas_owned)))
    price_farm = int(round(1000 * (1.15 ** farms_owned)))
    price_mine = int(round(10000 * (1.15 ** mines_owned)))
    price_worker_from_azia = int(round(50000 * (1.15 ** workers_from_azia_owned)))
    price_low_paid_people = int(round(250000 * (1.15 ** low_paid_people_owned)))
    price_robber = int(round(1000000 * (1.15 ** robbers_owned)))
    price_badger = int(round(2500000 * (1.15 ** badger_owned)))
    price_event_display = int(round(10000000 * (1.15 ** event_display_owned)))
    price_chinese_woman = int(round(10000000 * (1.15 ** chinese_woman_owned)))

    achievements_state = data.get("achievements_unlocked", {})
    for name, value in achievements_state.items():
        if name in achievements_module.achievements:
            achievements_module.achievements[name]["unlocked"] = bool(value)

    money_per_second = (
        grandmas_owned * 10
        + farms_owned * 30
        + mines_owned * 250
        + workers_from_azia_owned * 1000
        + low_paid_people_owned * 4000
        + robbers_owned * 10000
    )

    last_opened_time = float(data.get("last_opened_time", last_opened_time))
    now = time.time()
    if badger_owned > 0 and last_opened_time < now:
        elapsed_seconds = now - last_opened_time
        offline_income = int(badger_owned * 1000 * (elapsed_seconds / 3600.0))
        if offline_income > 0:
            money += offline_income

    last_opened_time = now

    try:
        pygame.mixer.music.load(songs[current_song_index])
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(music_volume)
    except Exception:
        pass
    for item in shop.shop_items:
        if item.get("name") == "Event display":
            item["hidden"] = True
            item["button_rect"] = None
            break

# -----------------
# Achievements
# -----------------

times_clicked = 0
achievements_opened = False
skins_opened = False
skins_scroll_offset = 0.0
skins_max_scroll = 0.0
selected_skin_id = "default"

# Load persisted data if available
load_game_data()
for item in shop.shop_items:
    if item.get("name") == "Event display" and event_display_owned >= 1:
        item["hidden"] = True
        item["button_rect"] = None
        break

# -----------------
# Load bread image
# -----------------
bread_path = os.path.join(os.path.dirname(__file__), "Skins", "bread.png")

try:
    default_bread_image = pygame.image.load(bread_path).convert_alpha()
except Exception as e:
    print(f"Failed to load image '{bread_path}':", e)

    default_bread_image = pygame.Surface((100, 100), pygame.SRCALPHA)
    pygame.draw.rect(
        default_bread_image,
        (130, 104, 29),
        default_bread_image.get_rect(),
        border_radius=20
    )

IMG_SIZE = (140, 140)
def apply_selected_skin():
    global bread_img
    selected_skin = next((skin for skin in skin_definitions if skin["id"] == selected_skin_id), None)
    if selected_skin and is_skin_unlocked(selected_skin):
        preview_image = get_skin_preview_image(selected_skin)
        if preview_image is not None:
            bread_img = pygame.transform.smoothscale(preview_image, IMG_SIZE)
            return

    bread_img = pygame.transform.smoothscale(default_bread_image, IMG_SIZE)

bread_img = pygame.transform.smoothscale(default_bread_image, IMG_SIZE)
apply_selected_skin()

player_rect = pygame.Rect(
    25,
    250,
    IMG_SIZE[0],
    IMG_SIZE[1]
)

# -----------------
# Hover effect
# -----------------
HOVER_SCALE = 1.12

# -----------------
# Particles
# -----------------
PARTICLE_COUNT = 10
PARTICLE_SIZE = (28, 28)
GRAVITY = 800

particles = []

# -----------------
# Shop scrolling
SHOP_X = 240
SHOP_Y = 0
SHOP_WIDTH = 205
SHOP_HEIGHT = 600
SHOP_HEADER_HEIGHT = 60
SHOP_ITEM_HEIGHT = 90
SHOP_ITEM_PADDING = 10

ACHIEVEMENTS_START_X = 10
ACHIEVEMENTS_START_Y = 90
ACHIEVEMENTS_COLS = 3
ACHIEVEMENTS_CARD_WIDTH = 240
ACHIEVEMENTS_CARD_HEIGHT = 100
ACHIEVEMENTS_PADDING = 15
ACHIEVEMENTS_VISIBLE_HEIGHT = 420
ACHIEVEMENTS_AREA_WIDTH = ACHIEVEMENTS_COLS * (ACHIEVEMENTS_CARD_WIDTH + ACHIEVEMENTS_PADDING) - ACHIEVEMENTS_PADDING

# -----------------
# Buttons
# -----------------
settings_button = Button(
    screen,
    750,
    20,
    40,
    40,

    font=emoji_font,
    text="⚙️",
    fontSize=24,
    margin=10,
    radius=12,

    inactiveColour=(170, 170, 170),
    hoverColour=(200, 200, 200),
    pressedColour=(130, 130, 130),

    onClick=settings.open_settings
)

close_settings_button = Button(
    screen,
    750,
    20,
    40,
    40,

    font=emoji_font,
    text="❌",
    fontSize=20,
    margin=6,
    radius=10,

    inactiveColour=(170, 170, 170),
    hoverColour=(200, 200, 200),
    pressedColour=(130, 130, 130),

    onClick=settings.close_settings
)
open_achievements_button = Button(
    screen,
    750,
    70,
    40,
    40,
    
    font=emoji_font,
    text="🏆",
    fontSize=18,
    margin=6,
    inactiveColour=(170, 170, 170),
    hoverColour=(200, 200, 200),
    pressedColour=(130, 130, 130),
    radius=10,
    onClick=achievements_module.toggle_achievements
)

open_skins_button = Button(
    screen,
    750,
    120,
    40,
    40,
    
    font=emoji_font,
    text="👗",
    fontSize=18,
    margin=6,
    inactiveColour=(170, 170, 170),
    hoverColour=(200, 200, 200),
    pressedColour=(130, 130, 130),
    radius=10,
    onClick=toggle_skins
)

close_achievements_button = Button(
    screen,
    750,
    70,
    40,
    40,
    
    font=emoji_font,
    text="❌",
    fontSize=20,
    margin=6,
    radius=10,
    inactiveColour=(170, 170, 170),
    hoverColour=(200, 200, 200),
    pressedColour=(130, 130, 130),
    onClick=achievements_module.close_achievements
)
close_achievements_button.hide()

close_skins_button = Button(
    screen,
    750,
    120,
    40,
    40,
    
    font=emoji_font,
    text="❌",
    fontSize=20,
    margin=6,
    radius=10,
    inactiveColour=(170, 170, 170),
    hoverColour=(200, 200, 200),
    pressedColour=(130, 130, 130),
    onClick=close_skins
)
close_skins_button.hide()
close_skins_button.hide()

open_color_picker_button = Button(
    screen,
    50,
    50,
    200,
    40,

    text="Choose Background Color",
    fontSize=18,
    margin=6,

    inactiveColour=(170, 170, 170),
    hoverColour=(200, 200, 200),
    pressedColour=(130, 130, 130),

    onClick=settings.choose_bg_color
)
change_song_button = Button(
    screen,
    50,
    250,
    200,
    40,

    text="Change Song",
    fontSize=18,
    margin=6,

    inactiveColour=(170, 170, 170),
    hoverColour=(200, 200, 200),
    pressedColour=(130, 130, 130),

    onClick=settings.change_song
)   

# -----------------
# FPS Slider
# -----------------
fps_slider = Slider(
    screen,
    50,
    140,
    250,
    20,
    min=10,
    max=240,
    step=5,
    initial=fps,
    handleColour=(0, 0, 0),
    handleRadius=14,
    colour=(50, 100, 0),
    curved = True,
    onValueChange=settings.update_fps
)

# -----------------
# music_volume Slider
# -----------------
music_volume_slider = Slider(
    screen,
    50,
    200,
    250,
    20,
    min=0,
    max=1,
    step=0.1,
    text="Music Volume",
    initial=music_volume,
    handleColour=(0, 0, 0),
    handleRadius=14,
    colour=(50, 100, 0),
    curved = True,
    onValueChange=settings.update_music_volume
)
sound_volume_slider = Slider(
    screen,
    335,
    200,
    250,
    20,
    min=0,
    max=1,
    step=0.1,
    text="Sound Volume",
    initial=sound_volume,
    handleColour=(0, 0, 0),
    handleRadius=14,
    colour=(50, 100, 0),
    curved = True,
    onValueChange=settings.update_sound_volume
)

# Hide settings widgets at start
close_settings_button.hide()
fps_slider.hide()
music_volume_slider.hide()
sound_volume_slider.hide()
open_color_picker_button.hide()
change_song_button.hide()
money_timer = 0
azian_woman_timer = 0.0
shop_scroll_offset = 0.0
achievements_scroll_offset = 0.0
achievements_max_scroll = 0.0
# Custom events and their timers
# -----------------

custom_events = [
    {
        "name": "Norbertas",
        "description": "-99% potato sell earnings for 10 seconds",
        "duration": 10,
        "frequency": 900, # every 15 minutes
        "event_type": pygame.USEREVENT + 1,
        "type": "earnings"
    },
    {
        "name": "Lukashenko",
        "description": "Gives 40% of current money",
        "duration": 1,
        "frequency": 3600,
        "event_type": pygame.USEREVENT + 2,
        "type": "instant"
    },
    {
        "name": "Germans",
        "description": "Occupies the shop for 30 seconds, preventing purchases",
        "duration": 30,
        "frequency": 1830, # every 30.5 minutes
        "event_type": pygame.USEREVENT + 3,
        "type": "lock"
    },
    {
        "name": "Taxes",
        "description": "Takes 15% of your money",
        "duration": 1,
        "frequency": 1500, # every 25 minutes
        "event_type": pygame.USEREVENT + 4,
        "type": "instant"
    },
]

for event_def in custom_events:
    pygame.time.set_timer(event_def["event_type"], int(event_def["frequency"] * 1000))
    event_def["next_trigger"] = time.time() + event_def["frequency"]


def format_duration(seconds):
    seconds = max(0, int(round(seconds)))
    minutes, seconds = divmod(seconds, 60)
    if minutes:
        return f"{minutes}m {seconds}s"
    return f"{seconds}s"


def get_event_display_text():
    now = time.time()
    if active_custom_events:
        active = min(active_custom_events, key=lambda a: a["time_left"])
        duration_text = format_duration(active["time_left"])
        return f"{active['name']} {duration_text} left"

    next_event = min(custom_events, key=lambda e: e.get("next_trigger", now + e["frequency"]))
    time_left = max(0, next_event.get("next_trigger", now) - now)
    return f"{next_event['name']} in {format_duration(time_left)}"


def trigger_custom_event(event_def):
    global money, price_discount, shop_locked, event_message, event_message_time

    event_message = f"{event_def['name']}: {event_def['description']}"
    event_message_time = 3.0

    if event_def["name"] == "Norbertas":
        money_earned_multiplier = 0.01
        existing = next((a for a in active_custom_events if a["name"] == event_def["name"]), None)
        if existing:
            existing["time_left"] = event_def["duration"]
        else:
            active_custom_events.append({
                "name": event_def["name"],
                "type": "earnings",
                "time_left": event_def["duration"]
            })
    elif event_def["name"] == "Lukashenko":
        bonus = int(money * 0.4)
        money += bonus
    elif event_def["name"] == "Germans":
        shop_locked = True
        active_custom_events.append({
            "name": event_def["name"],
            "type": "lock",
            "time_left": event_def["duration"]
        })
    elif event_def["name"] == "Taxes":
        loss = int(money * 0.15)
        money -= loss

    event_def["next_trigger"] = time.time() + event_def["frequency"]

# -----------------
# Main loop
# -----------------
running = True

while running:
    
    dt = clock.tick(fps) / 1000

    events = pygame.event.get()
    
    # precompute scrolling limits so event handlers can use them
    visible_shop_items = [item for item in shop.shop_items if not item.get("hidden", False)]
    content_height = len(visible_shop_items) * (SHOP_ITEM_HEIGHT + SHOP_ITEM_PADDING) + SHOP_ITEM_PADDING
    max_scroll = max(0, content_height - (SHOP_HEIGHT - SHOP_HEADER_HEIGHT))

    fps = int(fps_slider.getValue())
    music_volume = music_volume_slider.getValue()
    sound_volume = sound_volume_slider.getValue()
    pygame.mixer.music.set_volume(music_volume)
    if click_sound:
        click_sound.set_volume(sound_volume)
    # -----------------
    # Money generation (every 1 second)
    # -----------------
    money_timer += dt
    if money_timer >= 1.0:
        money += get_earned_money(money_per_second)
        money_timer = 0
    
    azian_woman_timer += dt
    if azian_woman_timer >= 30.0:
        if chinese_woman_owned > 0:
            workers_from_azia_owned += chinese_woman_owned
            money_per_second += 500 * chinese_woman_owned
        azian_woman_timer = 0.0

    achievements_module.check_achievements()
    apply_selected_skin()

    auto_save_timer += dt
    if auto_save_timer >= 60.0:
        save_game_data()
        auto_save_timer = 0.0

    auto_save_timer += dt
    if auto_save_timer >= 60.0:
        save_game_data()
        auto_save_timer = 0.0

    for item in shop.shop_items:
        if item["button_warning"] > 0:
            item["button_warning"] -= dt
            if item["button_warning"] <= 0:
                item["button_warning"] = 0
                item["button_colour"] = (150, 150, 150)


    # -----------------
    # Events
    # -----------------
    for event in events:

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if achievements_opened:
                achievements_opened = False
            elif skins_opened:
                skins_opened = False
            elif settings_open:
                settings_open = False

        # -----------------
        # Custom events
        # -----------------
        if event.type >= pygame.USEREVENT:
            for event_def in custom_events:
                if event.type == event_def["event_type"]:
                    trigger_custom_event(event_def)
                    break

        # -----------------
        # Bread clicking
        # -----------------
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            if skins_opened:
                cols = ACHIEVEMENTS_COLS
                card_w = ACHIEVEMENTS_CARD_WIDTH
                card_h = ACHIEVEMENTS_CARD_HEIGHT
                padding = ACHIEVEMENTS_PADDING
                start_x = ACHIEVEMENTS_START_X
                start_y = ACHIEVEMENTS_START_Y

                for idx, skin in enumerate(skin_definitions):
                    row = idx // cols
                    col = idx % cols
                    x = start_x + col * (card_w + padding)
                    y = start_y + row * (card_h + padding) - skins_scroll_offset
                    rect = pygame.Rect(x, y, card_w, card_h)
                    if rect.collidepoint(mouse_pos) and is_skin_unlocked(skin):
                        selected_skin_id = skin["id"]
                        save_game_data()
                        break
            elif not settings_open and not achievements_opened:
                for item in visible_shop_items:
                    button_rect = item.get("button_rect")
                    if button_rect and button_rect.collidepoint(mouse_pos):
                        if shop_locked:
                            item["button_colour"] = (200, 0, 0)
                            item["button_warning"] = 0.75
                        else:
                            price = item["price"]()
                            if money >= price:
                                item["action"]()
                            else:
                                item["button_colour"] = (200, 0, 0)
                                item["button_warning"] = 0.75
                        break

                hovered = player_rect.collidepoint(mouse_pos)

                if hovered:
                    money += get_earned_money(1)
                    times_clicked += 1
                    if click_sound:
                        click_sound.play()

                    cx, cy = player_rect.center

                    for _ in range(PARTICLE_COUNT):
                        small = pygame.transform.smoothscale(
                            bread_img,
                            PARTICLE_SIZE
                        ).copy()

                        particles.append({
                            "x": cx + random.uniform(-10, 10),
                            "y": cy + random.uniform(-10, 10),
                            "vx": random.uniform(-120, 120),
                            "vy": random.uniform(-30, 80),
                            "img": small,
                            "alpha": 255,
                        })

        elif event.type == pygame.MOUSEWHEEL and not settings_open:
            mx, my = getattr(event, 'pos', pygame.mouse.get_pos())
            scroll_amount = 40
            if achievements_opened or skins_opened:
                if achievements_opened:
                    rows = (len(achievements_module.achievements) + ACHIEVEMENTS_COLS - 1) // ACHIEVEMENTS_COLS
                else:
                    rows = (len(skin_definitions) + ACHIEVEMENTS_COLS - 1) // ACHIEVEMENTS_COLS
                content_height = rows * (ACHIEVEMENTS_CARD_HEIGHT + ACHIEVEMENTS_PADDING) - ACHIEVEMENTS_PADDING
                max_scroll = max(0, content_height - ACHIEVEMENTS_VISIBLE_HEIGHT)
                if ACHIEVEMENTS_START_X <= mx <= ACHIEVEMENTS_START_X + ACHIEVEMENTS_AREA_WIDTH and ACHIEVEMENTS_START_Y <= my <= ACHIEVEMENTS_START_Y + ACHIEVEMENTS_VISIBLE_HEIGHT:
                    if achievements_opened:
                        achievements_scroll_offset = max(0, min(achievements_scroll_offset - event.y * scroll_amount, max_scroll))
                    else:
                        skins_scroll_offset = max(0, min(skins_scroll_offset - event.y * scroll_amount, max_scroll))
            else:
                if SHOP_X <= mx <= SHOP_X + SHOP_WIDTH and SHOP_Y <= my <= SHOP_Y + SHOP_HEIGHT:
                    delta = event.y
                    shop_scroll_offset = max(0, min(shop_scroll_offset - delta * scroll_amount, max_scroll))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button in (4, 5) and not settings_open:
            mx, my = getattr(event, 'pos', pygame.mouse.get_pos())
            scroll_amount = 40
            if achievements_opened or skins_opened:
                if achievements_opened:
                    rows = (len(achievements_module.achievements) + ACHIEVEMENTS_COLS - 1) // ACHIEVEMENTS_COLS
                else:
                    rows = (len(skin_definitions) + ACHIEVEMENTS_COLS - 1) // ACHIEVEMENTS_COLS
                content_height = rows * (ACHIEVEMENTS_CARD_HEIGHT + ACHIEVEMENTS_PADDING) - ACHIEVEMENTS_PADDING
                max_scroll = max(0, content_height - ACHIEVEMENTS_VISIBLE_HEIGHT)
                if ACHIEVEMENTS_START_X <= mx <= ACHIEVEMENTS_START_X + ACHIEVEMENTS_AREA_WIDTH and ACHIEVEMENTS_START_Y <= my <= ACHIEVEMENTS_START_Y + ACHIEVEMENTS_VISIBLE_HEIGHT:
                    delta = 1 if event.button == 4 else -1
                    if achievements_opened:
                        achievements_scroll_offset = max(0, min(achievements_scroll_offset - delta * scroll_amount, max_scroll))
                    else:
                        skins_scroll_offset = max(0, min(skins_scroll_offset - delta * scroll_amount, max_scroll))
            else:
                if SHOP_X <= mx <= SHOP_X + SHOP_WIDTH and SHOP_Y <= my <= SHOP_Y + SHOP_HEIGHT:
                    delta = 1 if event.button == 4 else -1
                    shop_scroll_offset = max(0, min(shop_scroll_offset - delta * scroll_amount, max_scroll))

    for active in active_custom_events[:]:
        active["time_left"] -= dt
        if active["time_left"] <= 0:
            active_custom_events.remove(active)
            if active["type"] == "discount" and not any(a["type"] == "discount" for a in active_custom_events):
                price_discount = 1.0
            elif active["type"] == "earnings" and not any(a["type"] == "earnings" for a in active_custom_events):
                money_earned_multiplier = 1.0
            elif active["type"] == "lock" and not any(a["type"] == "lock" for a in active_custom_events):
                shop_locked = False

    if event_message_time > 0:
        event_message_time -= dt

    # Draw
    # -----------------
    if settings_open:

        screen.fill((220, 220, 220))

        # Show settings widgets
        settings_button.hide()
        open_achievements_button.hide()
        open_skins_button.hide()
        close_achievements_button.hide()
        close_skins_button.hide()
        close_settings_button.show()
        fps_slider.show()
        open_color_picker_button.show()
        change_song_button.show()
        music_volume_slider.show()
        sound_volume_slider.show()

        fps_text = font.render(
            f"Max FPS: {int(fps)}",
            True,
            (0, 0, 0)
        )
        current_song_name = os.path.basename(songs[current_song_index]).capitalize().replace('_', ' ').replace('.mp3', '')
        current_song_text = small_font.render(
            f"Current Song: {current_song_name}",
            True,
            (0, 0, 0)
        )
        screen.blit(current_song_text, (270, 265))

        screen.blit(fps_text, (95, 110))
        
        music_volume_text = font.render(
            f"music volume: {round(music_volume, 1)}",
            True,
            (0, 0, 0)
        )
        screen.blit(music_volume_text, (95, 170))
        
        sound_volume_text = font.render(
            f"sound volume: {round(sound_volume, 1)}",
            True,
            (0, 0, 0)
        )
        screen.blit(sound_volume_text, (375, 170))
        
        screen.blit(
            small_font.render(
                f"Version: {VERSION}",
                True,
                (0, 0, 0),
            ),
            (5, 580)
        )

    else:
        try:
            screen.fill(bg)
        except Exception as e:
            screen.fill((139, 204, 55))

        # Show main widgets
        settings_button.show()
        close_settings_button.hide()
        fps_slider.hide()
        open_color_picker_button.hide()
        change_song_button.hide()
        music_volume_slider.hide()
        sound_volume_slider.hide()

        pygame.draw.rect(
            screen,
            (100, 100, 100),
            (SHOP_X, SHOP_Y, SHOP_WIDTH, SHOP_HEIGHT),
            border_radius=20
        )

        header_rect = pygame.Rect(SHOP_X + 6, SHOP_Y + 6, SHOP_WIDTH - 12, SHOP_HEADER_HEIGHT - 10)
        pygame.draw.rect(screen, (80, 80, 80), header_rect, border_radius=16)
        pygame.draw.rect(screen, (180, 180, 180), header_rect, 2, border_radius=16)
        screen.blit(
            font.render(
                "Shop",
                True,
                (255, 255, 255)
            ),
            (SHOP_X + 20, SHOP_Y + 16)
        )

        content_background = pygame.Rect(
            SHOP_X + 6,
            SHOP_Y + SHOP_HEADER_HEIGHT,
            SHOP_WIDTH - 12,
            SHOP_HEIGHT - SHOP_HEADER_HEIGHT - 6
        )
        pygame.draw.rect(screen, (235, 235, 235), content_background, border_radius=16)

        mouse_pos = pygame.mouse.get_pos()
        shop_content_top = SHOP_Y + SHOP_HEADER_HEIGHT
        visible_height = SHOP_HEIGHT - SHOP_HEADER_HEIGHT
        content_y = shop_content_top + SHOP_ITEM_PADDING - shop_scroll_offset
        shop_hover_description = None
        hovered_tooltip_rect = None

        previous_clip = screen.get_clip()
        screen.set_clip(content_background)

        for item in visible_shop_items:
            item_rect = pygame.Rect(
                SHOP_X + SHOP_ITEM_PADDING,
                content_y,
                SHOP_WIDTH - SHOP_ITEM_PADDING * 2,
                SHOP_ITEM_HEIGHT
            )

            if item_rect.bottom >= shop_content_top and item_rect.top <= shop_content_top + visible_height:
                pygame.draw.rect(screen, (245, 245, 245), item_rect, border_radius=10)
                pygame.draw.rect(screen, (160, 160, 160), item_rect, 2, border_radius=10)

                screen.blit(
                    small_font.render(item["name"], True, (0, 0, 0)),
                    (item_rect.x + 10, item_rect.y + 10)
                )
                screen.blit(
                    small_font.render(f"{format_money(item['price']())} money", True, (0, 0, 0)),
                    (item_rect.x + 10, item_rect.y + 58)
                )

                if item_rect.collidepoint(mouse_pos):
                    shop_hover_description = item["description"]
                    hovered_tooltip_rect = item_rect

                button_rect = pygame.Rect(item_rect.right - 64, item_rect.y + 24, 54, 36)
                pygame.draw.rect(screen, item["button_colour"], button_rect, border_radius=8)
                screen.blit(
                    small_font.render("Buy", True, (0, 0, 0)),
                    (button_rect.x + 8, button_rect.y + 8)
                )
                item["button_rect"] = button_rect
            else:
                item["button_rect"] = None

            content_y += SHOP_ITEM_HEIGHT + SHOP_ITEM_PADDING

        if shop_hover_description and hovered_tooltip_rect:
            tooltip_info = (shop_hover_description, hovered_tooltip_rect)
        else:
            tooltip_info = None

        screen.set_clip(previous_clip)

        scroll_area_height = visible_height
        content_height = len(visible_shop_items) * (SHOP_ITEM_HEIGHT + SHOP_ITEM_PADDING) + SHOP_ITEM_PADDING
        max_scroll = max(0, content_height - scroll_area_height)
        if max_scroll > 0:
            thumb_height = max(24, scroll_area_height * scroll_area_height / content_height)
            thumb_y = shop_content_top + (shop_scroll_offset / max_scroll) * (scroll_area_height - thumb_height)
            pygame.draw.rect(screen, (180, 180, 180), (SHOP_X + SHOP_WIDTH - 10, thumb_y, 6, thumb_height), border_radius=3)

        screen.blit(
            small_font.render(
                f"Version: {VERSION}",
                True,
                (0, 0, 0),
            ),
            (5, 580)
        )

        open_achievements_button.show()
        open_skins_button.show()
        close_achievements_button.hide()
        close_skins_button.hide()

        # -----------------
        # Bread hover effect
        # -----------------
        mouse_pos = pygame.mouse.get_pos()

        hovered = player_rect.collidepoint(mouse_pos)

        if hovered:

            scaled_size = (
                int(IMG_SIZE[0] * HOVER_SCALE),
                int(IMG_SIZE[1] * HOVER_SCALE)
            )

            draw_img = pygame.transform.smoothscale(
                bread_img,
                scaled_size
            )

            draw_rect = draw_img.get_rect(
                center=player_rect.center
            )

        else:

            draw_img = bread_img

            draw_rect = bread_img.get_rect(
                topleft=player_rect.topleft
            )

        screen.blit(draw_img, draw_rect.topleft)

        # -----------------
        # Particles
        # -----------------
        alive = []

        for p in particles:

            p["vy"] += GRAVITY * dt

            p["x"] += p["vx"] * dt
            p["y"] += p["vy"] * dt

            p["alpha"] -= 220 * dt

            if (
                p["alpha"] > 0
                and p["y"] < screen.get_height() + 50
            ):

                img = p["img"].copy()

                img.set_alpha(
                    max(0, int(p["alpha"]))
                )

                screen.blit(
                    img,
                    (
                        int(p["x"] - img.get_width() / 2),
                        int(p["y"] - img.get_height() / 2)
                    )
                )

                alive.append(p)

        particles = alive

        # -----------------
        # Money text
        # -----------------
        money_text = font.render(
            f"Money: {format_money(money)}",
            True,
            (0, 0, 0)
        )
        money_sec_text = small_font.render(
            f"+{format_money(money_per_second)} per second",
            True,
            (0, 0, 0)
        )

        screen.blit(money_text, (50, 20))
        screen.blit(money_sec_text, (50, 50))

        if event_display_owned > 0:
            event_display_text = get_event_display_text()
            event_surface = small_font.render(event_display_text, True, (255, 255, 255))
            event_rect = event_surface.get_rect(topright=(740, 28))
            pygame.draw.rect(screen, (0, 0, 0), event_rect.inflate(16, 12), border_radius=10)
            screen.blit(event_surface, event_rect)

        elif event_message_time > 0 and event_display_owned == 0:
            screen.blit(
                small_font.render(event_message, True, (255, 220, 0)),
                (50, 80)
            )

        if shop_locked:
            lock_text = small_font.render("Shop occupied by Germans! Purchases disabled.", True, (255, 100, 0))
            screen.blit(lock_text, (SHOP_X + 10, SHOP_Y + SHOP_HEADER_HEIGHT + 10))

        if tooltip_info:
            shop_hover_description, hovered_tooltip_rect = tooltip_info
            tooltip_w = 180
            padding_x = 12
            max_text_w = tooltip_w - padding_x * 2

            words = shop_hover_description.split()
            lines = []
            cur = ""
            for w in words:
                test = (cur + " " + w).strip()
                if small_font.size(test)[0] <= max_text_w:
                    cur = test
                else:
                    if cur:
                        lines.append(cur)
                    cur = w
            if cur:
                lines.append(cur)

            line_h = small_font.get_linesize()
            tooltip_h = max(32, len(lines) * line_h + padding_x)

            tooltip_x = hovered_tooltip_rect.x - tooltip_w - 10
            tooltip_y = hovered_tooltip_rect.y
            if tooltip_x < 6:
                tooltip_x = 6
            if tooltip_y + tooltip_h > screen.get_height() - 6:
                tooltip_y = max(6, screen.get_height() - tooltip_h - 6)

            tooltip_rect = pygame.Rect(tooltip_x, tooltip_y, tooltip_w, tooltip_h)
            pygame.draw.rect(screen, (245, 245, 245), tooltip_rect, border_radius=8)
            pygame.draw.rect(screen, (180, 180, 180), tooltip_rect, 2, border_radius=8)

            ty = tooltip_y + 8
            for ln in lines:
                screen.blit(small_font.render(ln, True, (0, 0, 0)), (tooltip_x + padding_x, ty))
                ty += line_h
    
    if achievements_opened:
        screen.fill((245, 245, 250))
        close_achievements_button.show()
        settings_button.show()
        open_achievements_button.show()
        open_skins_button.show()

        title_text = font.render("Achievements", True, (20, 20, 20))
        screen.blit(title_text, (20, 20))

        padding = ACHIEVEMENTS_PADDING
        cols = ACHIEVEMENTS_COLS
        card_w = ACHIEVEMENTS_CARD_WIDTH
        card_h = ACHIEVEMENTS_CARD_HEIGHT
        start_x = ACHIEVEMENTS_START_X
        start_y = ACHIEVEMENTS_START_Y
        visible_height = ACHIEVEMENTS_VISIBLE_HEIGHT
        mouse_pos = pygame.mouse.get_pos()
        hovered_info = None
        hovered_name = None

        achievement_items = list(achievements_module.achievements.items())
        rows = (len(achievement_items) + cols - 1) // cols
        content_height = rows * (card_h + padding) - padding
        achievements_max_scroll = max(0, content_height - visible_height)
        achievements_scroll_offset = min(max(0, achievements_scroll_offset), achievements_max_scroll)

        for idx, (name, info) in enumerate(achievement_items):
            row = idx // cols
            col = idx % cols
            x = start_x + col * (card_w + padding)
            y = start_y + row * (card_h + padding) - achievements_scroll_offset
            rect = pygame.Rect(x, y, card_w, card_h)

            if rect.bottom < start_y or rect.top > start_y + visible_height:
                continue

            unlocked = info["unlocked"]
            bg_color = (220, 255, 220) if unlocked else (255, 220, 220)
            border_color = (30, 150, 30) if unlocked else (180, 40, 40)
            pygame.draw.rect(screen, bg_color, rect, border_radius=14)
            pygame.draw.rect(screen, border_color, rect, 3, border_radius=14)

            icon = info.get("icon", "🏆")
            screen.blit(emoji_font.render(icon, True, border_color), (x + 14, y + 18))
            screen.blit(
                small_font.render(name, True, (20, 20, 20)),
                (x + 62, y + 18)
            )

            status_text = "Unlocked" if unlocked else "Locked"
            status_color = (0, 100, 0) if unlocked else (150, 0, 0)
            screen.blit(
                small_font.render(status_text, True, status_color),
                (x + 62, y + 50)
            )

            if rect.collidepoint(mouse_pos):
                hovered_name = name
                hovered_info = info
                pygame.draw.rect(screen, (255, 255, 255), rect, 3, border_radius=14)

        area_rect = pygame.Rect(start_x, start_y, ACHIEVEMENTS_AREA_WIDTH, visible_height)

        if achievements_max_scroll > 0:
            thumb_height = max(32, visible_height * visible_height / content_height)
            thumb_y = start_y + (achievements_scroll_offset / achievements_max_scroll) * (visible_height - thumb_height)
            pygame.draw.rect(screen, (180, 180, 180), (area_rect.right + 6, thumb_y, 8, thumb_height), border_radius=4)

        detail_y = start_y + visible_height + 20
        if hovered_info:
            label = font.render(hovered_name, True, (0, 0, 0))
            screen.blit(label, (20, detail_y))

            desc = hovered_info["description"]
            max_desc_width = 760
            words = desc.split()
            lines = []
            current = ""
            for word in words:
                test = (current + " " + word).strip()
                if small_font.size(test)[0] <= max_desc_width:
                    current = test
                else:
                    lines.append(current)
                    current = word
            if current:
                lines.append(current)

            desc_y = detail_y + 40
            for line in lines:
                screen.blit(small_font.render(line, True, (50, 50, 50)), (20, desc_y))
                desc_y += small_font.get_linesize()
        else:
            hint = small_font.render(
                "Hover an achievement card to see its description.",
                True,
                (80, 80, 80)
            )
            screen.blit(hint, (20, detail_y))
    
    if skins_opened:
        screen.fill((245, 245, 250))
        close_skins_button.show()
        close_achievements_button.hide()
        settings_button.show()
        open_achievements_button.show()
        open_skins_button.show()

        title_text = font.render("Skins", True, (20, 20, 20))
        screen.blit(title_text, (20, 20))

        padding = ACHIEVEMENTS_PADDING
        cols = ACHIEVEMENTS_COLS
        card_w = ACHIEVEMENTS_CARD_WIDTH
        card_h = ACHIEVEMENTS_CARD_HEIGHT
        start_x = ACHIEVEMENTS_START_X
        start_y = ACHIEVEMENTS_START_Y
        visible_height = ACHIEVEMENTS_VISIBLE_HEIGHT
        mouse_pos = pygame.mouse.get_pos()
        hovered_skin = None

        rows = (len(skin_definitions) + cols - 1) // cols
        content_height = rows * (card_h + padding) - padding
        skins_max_scroll = max(0, content_height - visible_height)
        skins_scroll_offset = min(max(0, skins_scroll_offset), skins_max_scroll)

        for idx, skin in enumerate(skin_definitions):
            row = idx // cols
            col = idx % cols
            x = start_x + col * (card_w + padding)
            y = start_y + row * (card_h + padding) - skins_scroll_offset
            rect = pygame.Rect(x, y, card_w, card_h)

            if rect.bottom < start_y or rect.top > start_y + visible_height:
                continue

            unlocked = is_skin_unlocked(skin)
            selected = selected_skin_id == skin["id"]
            bg_color = (220, 255, 220) if unlocked else (255, 220, 220)
            border_color = (30, 150, 30) if selected else ((30, 120, 200) if unlocked else (180, 40, 40))
            pygame.draw.rect(screen, bg_color, rect, border_radius=14)
            pygame.draw.rect(screen, border_color, rect, 3, border_radius=14)

            preview_rect = pygame.Rect(x + 12, y + 12, 90, 76)
            if unlocked:
                pygame.draw.rect(screen, (245, 245, 245), preview_rect, border_radius=10)
                pygame.draw.rect(screen, border_color, preview_rect, 2, border_radius=10)
                preview_image = get_skin_preview_image(skin)
                if preview_image is not None:
                    scaled_preview = pygame.transform.smoothscale(preview_image, (preview_rect.width, preview_rect.height))
                    screen.blit(scaled_preview, preview_rect.topleft)
                else:
                    screen.blit(small_font.render("Preview", True, (80, 80, 80)), (preview_rect.x + 18, preview_rect.y + 28))
            else:
                pygame.draw.rect(screen, (0, 0, 0), preview_rect, border_radius=10)
                pygame.draw.rect(screen, (60, 60, 60), preview_rect, 2, border_radius=10)
                screen.blit(small_font.render("Needs", True, (255, 255, 255)), (preview_rect.x + 18, preview_rect.y + 16))
                screen.blit(small_font.render(skin.get("achievement_name", "Unlock"), True, (255, 255, 255)), (preview_rect.x + 8, preview_rect.y + 40))

            text_area = pygame.Rect(x + 112, y + 12, rect.width - 122, rect.height - 20)
            name_lines = wrap_text(skin["display_name"], small_font, max(80, text_area.width - 8))
            if name_lines:
                for line_index, line in enumerate(name_lines[:2]):
                    line_y = text_area.y + line_index * small_font.get_linesize()
                    screen.blit(small_font.render(line, True, (20, 20, 20)), (text_area.x, line_y))

            status_text = "Selected" if selected else ("Unlocked" if unlocked else "Locked")
            status_color = (0, 100, 0) if selected else ((0, 100, 0) if unlocked else (150, 0, 0))
            status_y = text_area.y + min(len(name_lines), 2) * small_font.get_linesize() + 4
            if status_y < y + rect.height - 18:
                screen.blit(
                    small_font.render(status_text, True, status_color),
                    (text_area.x, status_y)
                )

            if rect.collidepoint(mouse_pos):
                hovered_skin = skin
                pygame.draw.rect(screen, (255, 255, 255), rect, 3, border_radius=14)

        area_rect = pygame.Rect(start_x, start_y, ACHIEVEMENTS_AREA_WIDTH, visible_height)
        if skins_max_scroll > 0:
            thumb_height = max(32, visible_height * visible_height / content_height)
            thumb_y = start_y + (skins_scroll_offset / skins_max_scroll) * (visible_height - thumb_height)
            pygame.draw.rect(screen, (180, 180, 180), (area_rect.right + 6, thumb_y, 8, thumb_height), border_radius=4)

        detail_y = start_y + visible_height + 20
        if hovered_skin:
            label = font.render(hovered_skin["display_name"], True, (0, 0, 0))
            screen.blit(label, (20, detail_y))

            desc = hovered_skin["description"]
            max_desc_width = 760
            words = desc.split()
            lines = []
            current = ""
            for word in words:
                test = (current + " " + word).strip()
                if small_font.size(test)[0] <= max_desc_width:
                    current = test
                else:
                    lines.append(current)
                    current = word
            if current:
                lines.append(current)

            desc_y = detail_y + 40
            for line in lines:
                screen.blit(small_font.render(line, True, (50, 50, 50)), (20, desc_y))
                desc_y += small_font.get_linesize()
        else:
            hint = small_font.render(
                "Hover a skin card to see its description and click to select.",
                True,
                (80, 80, 80)
            )
            screen.blit(hint, (20, detail_y))

    # -----------------
    # Update ALL widgets
    # -----------------
    pygame_widgets.update(events)

    pygame.display.flip()

save_game_data()
pygame.quit()
