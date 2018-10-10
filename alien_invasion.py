import game_functions as gf
import pygame

from button import Button
from game_stats import GameStats
from pygame.sprite import Group
from settings import Settings
from scoreboard import Scoreboard
from ship import Ship

def run_game():
    # initialize game and create a screen object
    pygame.init()
    ai_settings = Settings() # Settings instance
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # make the play button
    play_button = Button(ai_settings, screen, 'Play')
    # create an instance to store game statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)            
    # make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:   
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, 
            ship, aliens, bullets, play_button)

run_game()