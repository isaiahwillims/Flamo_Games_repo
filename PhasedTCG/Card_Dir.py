import pygame, random

#Main Card Types

class Card(pygame.sprite.Sprite):
    pass
    
class Character(Card):
    global owner, controller, name, cost, elemtent, type, subtype, atk, res, hp, ThumbImage, CardImage, status
    
    def update(self):
        if self.hp < 1:
            status = "dead"
    
    def Dead(status):
        if status == "dead":
            self.kill()
    
    pass

class Relic(Card):
    pass
    
class Ability(Card):
    pass

# Core cards
    
class CelestialPhoenix(Character):

    owner = []
    controller = []
    name = "Celestial Phoenix"
    cost = 3
    element = ["LIGHT"]
    type = ["Character"]
    subtype = ["Phoenix"]
    atk = 85
    res = 7
    hp = 75
    status = "alive"
    
    ThumbImage = pygame.image.load("Data/Cards/Core_set/CelestialPhoenix_thumb.jpg")
    CardImage = pygame.image.load("Data/Cards/Core_set/CelestialPhoenix.jpg")
    
class ShadowrightDarkDragon(Character):

    owner = []
    controller = []
    name = "Shadowright, Dark Dragon"
    cost = 3
    element = "DARK"
    type = ["Epic", "Character"]
    subtype = ["Dragon"]
    atk = 90
    res = 15
    hp = 110
    status = "alive"
    
    ThumbImage = pygame.image.load("Data/Cards/Core_set/ShadowrightDarkDragon_thumb.jpg")
    CardImage = pygame.image.load("Data/Cards/Core_set/ShadowrightDarkDragon.jpg")
    
class BlazorPhoenixOfLegend(Character):

    owner = []
    controller = []
    name = "Blazor, Phoenix of Legend"
    cost = 3
    element = ["FIRE"]
    type = ["Epic" ,"Character"]
    subtype = ["Phoenix"]
    atk = 100
    res = 5
    hp = 70
    status = "alive"
    
    ThumbImage = pygame.image.load("Data/Cards/Core_set/BlazorPhoenixOfLegend(thumb).jpg")
    CardImage = pygame.image.load("Data/Cards/Core_set/BlazorPhoenixOfLegend.jpg")