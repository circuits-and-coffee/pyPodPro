import pygame, sys, random 

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((320,240))

    print("Hello from pypodpro!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            screen.fill(color="#000000")

if __name__ == "__main__":
    main()
