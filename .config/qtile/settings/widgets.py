import subprocess
from libqtile import widget
from .theme import colors

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)

def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline_triangle(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",
        fontsize=37,
        padding=-2
    )
def powerline_circle(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",
        fontsize=31,
        padding=0
    )
def media_marquee_widget():
    text_state = {"song": "", "scroll": ""}

    def scroll():
        # Obtener info de playerctl
        song = subprocess.getoutput(
            "playerctl metadata -p spotify --format '{{artist}} - {{title}}' 2>/dev/null"
        ).strip()

        status = subprocess.getoutput("playerctl -p spotify status 2>/dev/null").strip()

        if not song:
            return " "

        # Reiniciar scroll si cambia la canción
        if song != text_state["song"]:
            text_state["song"] = song
            text_state["scroll"] = song + "       "

        s = text_state["scroll"]

        # Siempre rotar (scroll continuo)
        text_state["scroll"] = s[1:] + s[0]

        # Icono depende del estado
        if status == "Paused":
            icon = "  "
        elif status == "Playing":
            icon = "  "
        else:
            icon = ""

        return f"{icon}{s[:30]}"

    return widget.GenPollText(
        func=scroll,
        update_interval=0.20,
        foreground=colors["color2"][0],
        background=colors["dark"][0],
        padding=10,
    )




def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]

primary_widgets_temp = [

    widget.GroupBox(
        font="UbuntuMono Nerd Font",
        fontsize=22,
        borderwidth=3,
        highlight_method='block',
        active=colors["color2"][0],
        block_highlight_text_color=colors["grey"][0],
        highlight_color='#353446',
        inactive=colors["inactive"][0],
        foreground=colors["color1"],
        background=colors["grey"][0],
        this_current_screen_border=colors['light'][0],
        this_screen_border='#353446',
        other_current_screen_border='#353446',
        other_screen_border='#353446',
        urgent_border=colors["urgent"][0],
        rounded=True,
        disable_drag=True,
    ),

    widget.Spacer(
        length=8,
        background=colors["grey"][0],
    ),
    powerline_triangle('grey','text'),

    widget.Spacer(
        length=8,
        background=colors["text"][0],
    ),

    widget.CurrentLayout(
        stom_icon_paths=["~/.config/qtile/Assets/layout"],
        background=colors["text"][0],
        foreground=colors["color2"][0],
        scale=0.50,
    ),
    widget.Spacer(
        length=8,
        background=colors["text"][0],
    ),

    powerline_triangle('text','dark'),

    widget.Spacer(
        length=8,
        background=colors['dark'][0],
    ),
    widget.WindowName(
        background=colors["dark"][0],
        font="UbuntuMono Nerd Font Bold",
        fontsize=15,
        empty_group_string="Desktop",
        max_chars=130,
        foreground=colors["color2"][0],
    ),

    widget.Spacer(
        length=8,
        background=colors["dark"][0],
    ),
    
    #spotify_widget(),
    media_marquee_widget(),

    powerline_triangle('dark','text'),
    widget.Spacer(
        length=8,
        background=colors['text'][0],
    ),

    widget.Net(**base('color2','text'), interface='wlan0'),
    
    widget.Systray(
        background=colors["text"][0],
        icon_size=20,
    ),
    powerline_triangle('text','grey'),

    widget.Spacer(
        length=15,
        background=colors["grey"][0],
    ),

    widget.TextBox(
        text=" ",
        font="Font Awesome 6 Free Solid",
        fontsize=16,
        background=colors["grey"][0],
        foreground=colors['color2'][0],
    ),

    widget.Battery(
        font="UbuntuMono Nerd Font Bold",
        fontsize=16,
        background=colors["grey"][0],
        foreground='#CAA9E0',
        format='{percent:2.0%}',
    ),
    widget.Spacer(
        length=8,
        background=colors["grey"][0],
    ),

    powerline_triangle('grey','dark'),
    
    widget.Spacer(
        length=8,
        background=colors["dark"][0],
    ),

    widget.Clock(
        format='%d/%m/%Y - %I:%M' ,
        background=colors["dark"][0],
        foreground=colors['color2'][0],
        font="UbuntuMono Nerd Font Bold",
        fontsize=15,
    ),

    widget.Spacer(
        length=18,
        background=colors["dark"][0],
    ),
]

primary_widgets = [
    *workspaces(),

    separator(),

    powerline_triangle('color4', 'dark'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline_triangle('color3', 'color4'),

    icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    
    widget.Net(**base(bg='color3'), interface='wlp2s0'),

    powerline_triangle('color2', 'color3'),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline_triangle('color1', 'color2'),

    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline_triangle('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline_triangle('color1', 'dark'),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline_triangle('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline_triangle('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()