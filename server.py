import colorama
colorama.init()
from colorama import Fore

import json
import socket
import os
import re

import vgamepad
from keymaps import keymaps


ds4 = vgamepad.VDS4Gamepad()


def make():
    os.system('cls')

    HOST = "26.122.140.201"
    PORT = 5565
    
    print('Created virtual DS4 gamepad. Number:' + Fore.YELLOW, ds4.get_index() + 1, Fore.RESET)
    print('Hosting server on ' + Fore.YELLOW + f'{HOST}:{PORT}' + Fore.RESET)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by ' + Fore.YELLOW + f'{addr[0]}' + Fore.RESET)
            while True:
                try: 
                    r_data = conn.recv(1024)
                    redata = r_data.decode().replace('}', '}<>')
                    
                    groups = redata.split('<>')

                    for data in groups:
                        if not data:
                            continue

                        if not data.endswith('}'):
                            data += '}'
                        
                        try: data = json.loads(data)
                        except: continue

                        if 't' not in data:
                            continue

                        if data['t'] == 'down':
                            if 'key' not in data:
                                continue

                            if keymaps[data['key']].__class__ == vgamepad.DS4_SPECIAL_BUTTONS:
                                ds4.press_special_button(keymaps[data['key']])
                            elif keymaps[data['key']].__class__ == vgamepad.DS4_DPAD_DIRECTIONS:
                                ds4.directional_pad(keymaps[data['key']])
                            else:
                                ds4.press_button(keymaps[data['key']])

                            ds4.update()
                            
                        elif data['t'] == 'up':
                            if 'key' not in data:
                                continue

                            if keymaps[data['key']].__class__ == vgamepad.DS4_SPECIAL_BUTTONS:
                                ds4.release_special_button(keymaps[data['key']])
                            elif keymaps[data['key']].__class__ == vgamepad.DS4_DPAD_DIRECTIONS:
                                ds4.directional_pad(vgamepad.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE)
                            else:
                                ds4.release_button(keymaps[data['key']])

                            ds4.update()

                            print('OUTPUT ' + Fore.YELLOW + f'{keymaps[data['key']].name}', Fore.RESET)

                        elif data['t'] == 'axis':
                            if 'l2_a' in data:
                                ds4.left_trigger_float(data['l2_a'])
                                ds4.update()
                            if 'r2_a' in data:
                                ds4.right_trigger_float(data['r2_a'])
                                ds4.update()

                            if 'l3_x' in data and 'l3_y' in data:
                                ds4.left_joystick_float(data['l3_x'], data['l3_y'])
                                ds4.update()
                            if 'r3_x' in data and 'r3_y' in data:
                                ds4.right_joystick_float(data['r3_x'], data['r3_y'])
                                ds4.update()
                    
                except Exception as e: 
                    print('Party ended with error: ', e)
                    input()
                    break

                if not r_data:
                    pass


if __name__ == "__main__":
    make()