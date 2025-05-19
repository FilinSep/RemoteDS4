# RemoteDS4
**RemoteDS4** is a tool for remote playing in local co-op games. Made for DualShock4 gamepads.

ONLY SUPPORTS 1 CLIENT!!!!!

# As second player
Go to releases and download client file

# As first player
To host your own server:
## Install Python
https://www.python.org/
## Setup project
Open cmd in project folder and write command

```pip install -r requirements.txt```
## Host server
Use Radmin or Hamachi. 

Change ip and port in server.py script
```py
HOST = "localhost" # Change to your ip
PORT = 5565 # Change to your port
```

Open cmd in project folder and write command

```py server.py```

# Custom keymap
You should change **keymap.py**

It has special structure
```py
import vgamepad


d = vgamepad.DS4_BUTTONS


keymaps = [
    d.DS4_BUTTON_CROSS,
    d.DS4_BUTTON_CIRCLE,
    d.DS4_BUTTON_SQUARE,
    d.DS4_BUTTON_TRIANGLE,
    d.DS4_BUTTON_SHARE,
    vgamepad.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_PS,
    d.DS4_BUTTON_OPTIONS,
    d.DS4_BUTTON_THUMB_LEFT,
    d.DS4_BUTTON_THUMB_RIGHT,
    d.DS4_BUTTON_SHOULDER_LEFT,
    d.DS4_BUTTON_SHOULDER_RIGHT,
    vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH,
    vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTH,
    vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_WEST,
    vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST,
    vgamepad.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_TOUCHPAD,
]
```

Every button is numerated by python list's indexes. It means DS4 cross button has 0 index, it's first button.
So, if you want to change **CROSS** button to another, you should change the first element in list. **CIRCLE** is second, **SQUARE** is third and etc.
