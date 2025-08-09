import pygame, sys, random
from models.ui import *
from models.server import *
from services.discovery import *

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((320,240))



    # Try to find JellyFin servers
    server_list = discover_jellyfin_servers(3,2,True)
    
    
    print("Hello from pypodpro!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            screen.fill(color="#000000")

if __name__ == "__main__":
    main()
