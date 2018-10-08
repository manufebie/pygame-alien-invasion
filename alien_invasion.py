import game_functions as gf
import pygame

from alien import Alien
from pygame.sprite import Group
from settings import Settings
from ship import Ship

def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings() # Settings instance
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # make a ship
    ship = Ship(ai_settings, screen)
    # make a group to store bullets in.
    bullets = Group()
    # make an alien
    alien = Alien(ai_settings, screen)

    # set the background color
    # bg_color = (230, 230, 230)

    # start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

run_game()