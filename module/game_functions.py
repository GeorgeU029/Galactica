import sys
import pygame
from module.bullet import Bullet


def check_events(ai_settings,screen,ship,bullets):
    """This will respond to keyboard and mouse presses"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
             
               
def update_screen(ai_settings,screen,ship,bullets): 
    """This will update the images on the screen """
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #update the frames of the gane
    pygame.display.flip()

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """"will respond and move the ship depending on key press"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()    

def check_keyup_events(event,ship):
    """"will respond and move the ship depending on key press_up"""
    if event.key == pygame.K_RIGHT:    
        ship.moving_right = False
    if event.key == pygame.K_LEFT:    
        ship.moving_left = False 
def fire_bullets(ai_settings,screen,ship,bullets):
    """Used to fire the bullets when pressing space """  
    if len(bullets) < ai_settings.bullets_allowed:
        #Create a new bullet and add it to the bullets group
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet) 

def update_bullets(bullets):
    """update the pos of the bullets and remove old bullets"""
    bullets.update()
    #remove the bullets that are off the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)       