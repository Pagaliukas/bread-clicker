import pygame
import tkinter as tk
from tkinter import colorchooser
import sys
import importlib
from types import ModuleType
from typing import Any

root = tk.Tk()
root.withdraw()

# -----------------
# Settings functions
# -----------------

def _get_game() -> Any:
    game = sys.modules.get("__main__")
    if game is None or not hasattr(game, "settings_open"):
        game = importlib.import_module("breadclicker")
    return game


def open_settings():
    game = _get_game()
    game.achievements_opened = False
    game.settings_open = True


def close_settings():
    game = _get_game()
    game.settings_open = False


def update_fps(*args):
    game = _get_game()
    game.fps = int(game.fps_slider.getValue())


def update_music_volume(*args):
    game = _get_game()
    game.music_volume = game.music_volume_slider.getValue()
    pygame.mixer.music.set_volume(game.music_volume)
    if game.click_sound:
        game.click_sound.set_volume(game.sound_volume)


def update_sound_volume(*args):
    game = _get_game()
    game.sound_volume = game.sound_volume_slider.getValue()
    if game.click_sound:
        game.click_sound.set_volume(game.sound_volume)


def choose_bg_color():
    game = _get_game()
    rgb = colorchooser.askcolor(title="Choose a color")
    if rgb and rgb[0]:
        game.bg = tuple(int(v) for v in rgb[0])


def change_song():
    game = _get_game()
    game.current_song_index = (game.current_song_index + 1) % len(game.songs)
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    pygame.mixer.music.load(game.songs[game.current_song_index])
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(game.music_volume)
