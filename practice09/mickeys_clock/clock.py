import pygame
import datetime
import os

class MickeyClock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (300, 300)

       
        base_path = os.path.dirname(__file__)
        img_path = os.path.join(base_path, "images")

        
        self.clock_img = pygame.image.load(os.path.join(img_path, "clock.png")).convert_alpha()
        self.left_hand = pygame.image.load(os.path.join(img_path, "left.png")).convert_alpha()
        self.right_hand = pygame.image.load(os.path.join(img_path, "right.png")).convert_alpha()

    
        self.clock_img = pygame.transform.scale(self.clock_img, (600, 600))
        self.left_hand = pygame.transform.scale(self.left_hand, (120, 300))
        self.right_hand = pygame.transform.scale(self.right_hand, (120, 300))

    def get_angles(self):
        now = datetime.datetime.now()

        minutes = now.minute
        seconds = now.second

        minute_angle = -(minutes / 60) * 360
        second_angle = -(seconds / 60) * 360

        return minute_angle, second_angle

    def rotate(self, image, angle):
        rotated = pygame.transform.rotate(image, angle)
        rect = rotated.get_rect(center=self.center)
        return rotated, rect

    def update(self):
        self.min_angle, self.sec_angle = self.get_angles()

    def draw(self):
        
        self.screen.blit(self.clock_img, (0, 0))

        
        right_rot, right_rect = self.rotate(self.right_hand, self.min_angle)

        
        left_rot, left_rect = self.rotate(self.left_hand, self.sec_angle)


        self.screen.blit(right_rot, right_rect)
        self.screen.blit(left_rot, left_rect)

        
        pygame.draw.circle(self.screen, (0, 0, 0), self.center, 5)