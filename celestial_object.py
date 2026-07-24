import pygame
import math
from abc import ABC, abstractmethod

class CelestialObject(ABC):
    
    def __init__(self,image_path, mass, distance=0, orbit_speed=0):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.angle = 0
        self.distance = distance
        self._orbit_speed = 0
        self.mass = mass
        
        self.orbit_speed = orbit_speed
        
    @property
    def orbit_speed(self):
        return self._orbit_speed
    
    @orbit_speed.setter
    def orbit_speed(self, value):
        if value >=0 and value <=10:
            self._orbit_speed = value
        else:
            raise ValueError("Error en la orbita")

    def update(self):
        self.angle += self.orbit_speed
        
    def draw(self, screen):
        x = (screen.get_width() // 2) + (self.distance * math.cos(math.radians(self.angle)))
        y = (screen.get_height() // 2) + (self.distance * math.sin(math.radians(self.angle)))
        self.rect.centerx = x
        self.rect.centery = y
        screen.blit(self.image, self.rect)
        
    @abstractmethod
    def generate_magnetic_field(self, screen):
        pass
        
        