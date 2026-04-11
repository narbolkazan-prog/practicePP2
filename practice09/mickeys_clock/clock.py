import pygame
from datetime import datetime

class MickeyClock:
    def __init__(self, screen, hand_image_path):
        self.screen = screen
        
        # Load image
        self.hand_img = pygame.image.load(hand_image_path).convert_alpha()
        self.hand_img = pygame.transform.scale(self.hand_img, (300, 300))

        self.center = self.screen.get_rect().center

    def get_time_angles(self):
        now = datetime.now()
        minutes = now.minute
        seconds = now.second

        minute_angle = minutes * 6
        second_angle = seconds * 6

        return minute_angle, second_angle

    def draw_hand(self, angle):
        rotated = pygame.transform.rotate(self.hand_img, -angle)
        rect = rotated.get_rect(center=self.center)
        self.screen.blit(rotated, rect)

    def draw(self):
        minute_angle, second_angle = self.get_time_angles()

        # Right hand (minutes)
        self.draw_hand(minute_angle)

        # Left hand (seconds)
        self.draw_hand(second_angle)