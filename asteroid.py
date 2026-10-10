import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        random_angle = random.uniform(20, 50)
        split_one = self.velocity.rotate(random_angle)
        split_one_radius = self.radius - ASTEROID_MIN_RADIUS

        split_two = self.velocity.rotate(-random_angle)
        split_two_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, split_one_radius)
        asteroid_one.velocity = split_one * 1.2
        asteroid_two = Asteroid(self.position.x, self.position.y, split_two_radius)
        asteroid_two.velocity = split_two * 1.2
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
