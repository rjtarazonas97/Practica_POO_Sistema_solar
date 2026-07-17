import pygame 

class Planet:
    
    def __init__(self, image_path, distance, orbit_speed,mass, nucleo_status):
        self.image_path = image_path 
        self.distance = distance
        self.orbit_speed = orbit_speed
        self.mass = mass
        self.nucleo_status = nucleo_status
        
        
        3