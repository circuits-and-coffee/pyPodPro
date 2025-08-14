import pygame
import pygame_menu
from time import strftime
from models.pypod_menu import *
from models.server import *
from services.discovery import *
from models.menu_struct import MENU_STRUCTURE
import datetime

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

def build_menu(title, structure):
    # Create the menu itself
    menu = pypod_menu(elements={})  # start empty so we can add buttons manually

    for label, value in structure.items():
        if isinstance(value, dict):
            submenu = build_menu(label, value)
            menu.add.button(label, submenu)
        elif isinstance(value, pygame_menu.Menu):
            menu.add.button(label, value)
        elif callable(value) or value == pygame_menu.events.EXIT:
            menu.add.button(label, value)
        else:
            # placeholder -> create dummy menu for now
            placeholder = pypod_menu(elements={})
            menu.add.button(label, placeholder)

    return menu

def main():
    pygame.init()
    # game_clock = pygame.time.Clock()
    # dt = 0
    screen = pygame.display.set_mode((320,240))

    # Try to find JellyFin servers (move this into settings)
    # server_list = discover_jellyfin_servers(3,2,True)
    
    # Initialize the menus
    
    # Make a menu based on our Menu Structure data structure
    main_menu = build_menu('Main', MENU_STRUCTURE)

    main_menu.mainloop(screen)

    while True:
        for event in pygame.event.get():
            pass

def start_game():
    print("Game Started!")
    
if __name__ == "__main__":
    main()
