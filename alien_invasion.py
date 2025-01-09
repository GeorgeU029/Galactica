import pygame
from module.settings import Settings
from module.ship import Ship
import module.game_functions as gf

def run_game():
    #Initialize the game and create the screeen object
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #creating the ship
    ship = Ship(ai_settings,screen)
    #Starts the main loop of the game
    while True:
        gf.check_events(ship)
        ship.update()
        #set the baclground color of the screen 
        gf.update_screen(ai_settings,screen,ship)
run_game()                