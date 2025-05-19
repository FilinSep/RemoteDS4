import colorama
colorama.init()
from colorama import Fore

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
pygame.init()

import socket
import json
import time


def join():
    print(Fore.LIGHTGREEN_EX + 'RemoteDS4')
    print(Fore.RESET + 'GitHub: https://github.com/FilinSep/RemoteDS4')
    print()
    print(Fore.YELLOW + '*' + Fore.RESET + ' Allows you to play local co-op games on the DualShock4 joystick as a multiplayer using python sockets. Also you can use RadminVPN.')
    print()

    IP = input('ip > ' + Fore.YELLOW)
    print(Fore.RESET, end='')
    PORT = input('port > ' + Fore.YELLOW)
    print(Fore.RESET, end='')
    os.system('cls')
    
    sock = socket.socket()

    try:
        print('Connecting...')
        sock.connect((IP, int(PORT)))
    except:
        print('Wrong address')
        exit()

    os.system(f'title Party on {IP}:{PORT}')

    while True:
        try:
            j = pygame.joystick.Joystick(0)
            j.init()

            os.system('cls')

            while True:
                time.sleep(0.005)
                events = pygame.event.get()
                
                axis = {
                    't': 'axis',
                    'l3_x': j.get_axis(0),
                    'l3_y': j.get_axis(1),
                    'r3_x': j.get_axis(2),
                    'r3_y': j.get_axis(3),
                    'l2_a': j.get_axis(4),
                    'r2_a': j.get_axis(5)
                }

                sock.send(json.dumps(axis).encode())

                for event in events:
                    if event.type == pygame.JOYBUTTONDOWN:
                        print(f'INPUT DOWN {event.button}')
                        sock.send(json.dumps({'t': 'down', 'key': event.button}).encode())
                    elif event.type == pygame.JOYBUTTONUP:
                        print(f'INPUT UP {event.button}')
                        sock.send(json.dumps({'t': 'up', 'key': event.button}).encode())
                    elif event.type == pygame.JOYAXISMOTION and event.axis == 4:
                        print(f'INPUT L2 [{event.value}]')
                    elif event.type == pygame.JOYAXISMOTION and event.axis == 5:
                        print(f'INPUT R2 [{event.value}]')
        except socket.error:
            print('Party ended :(')
            input()
            exit()
        except:
            print('Waiting for DualShock4...', end='\r')
 

if __name__ == "__main__":
    join()