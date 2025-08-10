import pygame, sys, random
import pygame_menu
from models.pypod_menu import *
from models.server import *
from services.discovery import *

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((320,240))



    # Try to find JellyFin servers (move this into settings)
    # server_list = discover_jellyfin_servers(3,2,True)
    
    # print("Hello from pypodpro!")
    

    # Initialize the menus
    # music_menu = pygame_menu.Menu('Music',320, 240,
    #                     theme=pygame_menu.themes.THEME_BLUE)
    
    # Try to use a custom class to make a menu
    music_menu = pypod_menu(elements={
        'Artists': pygame_menu.events.EXIT,
        'Albums': pygame_menu.events.EXIT,
        'Tracks': pygame_menu.events.EXIT
    })
    
    main_menu = pypod_menu(elements={
        'Music': music_menu,
        'Videos': music_menu,
        'Photos': music_menu,
        'Settings': music_menu,
        'Shuffle Songs': music_menu,
        'Quit': pygame_menu.events.EXIT
    })

    # main_menu = pygame_menu.Menu('pyPodPro', 320, 240,
    #                     theme=pygame_menu.themes.THEME_BLUE)
    
    
    # music_menu.add.button('Artists', start_the_game)
    # music_menu.add.button('Albums', start_the_game)
    # music_menu.add.button('Tracks', start_the_game)
    # music_menu.add.button('Artists', start_the_game)

    # main_menu.add.button('Music', music_menu)
    # main_menu.add.button('Videos', music_menu)
    # main_menu.add.button('Photos', music_menu)
    # main_menu.add.button('Settings', music_menu)
    # main_menu.add.button('Shuffle Songs', music_menu)
    # main_menu.add.button('Quit', pygame_menu.events.EXIT)
    main_menu.mainloop(screen)
    
    

    while True:
        for event in pygame.event.get():
            pass

def start_game():
    print("Game Started!")
    
if __name__ == "__main__":
    main()
