#!/bin/sh

# Start composer
picom &

# Start wifi GUI
nm-applet &
blueman-applet &
#Keys latam
setxkbmap latam
