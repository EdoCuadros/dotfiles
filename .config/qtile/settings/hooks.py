from libqtile import hook
import os
import subprocess

@hook.subscribe.startup_once
def set_wallpaper():
    subprocess.Popen([
        "feh",
        "--bg-fill",
        "/home/ed/cloned_repos/upgraded-memory/Wallpapers/wallhaven-856dlk_1920x1080.png"
    ])
