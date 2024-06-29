import unittest
import pygame
import os
import math
from main import Car, SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT

class TestCar(unittest.TestCase):
    def setUp(self):
        # Initialize Pygame and create a car instance
        pygame.init()
        self.car = Car()
        self.car.rect.center = (490, 820)

    def test_drive(self):
        # Initial position
        initial_position = self.car.rect.center
        # Simulate driving
        self.car.drive()
        # New position
        new_position = self.car.rect.center
        # Check if the car has moved
        self.assertNotEqual(initial_position, new_position)

    def test_rotate(self):
        # Initial angle
        initial_angle = self.car.angle
        # Simulate rotation
        self.car.direction = 1
        self.car.rotate()
        # New angle
        new_angle = self.car.angle
        # Check if the car has rotated
        self.assertNotEqual(initial_angle, new_angle)

    def test_radar(self):
        # Simulate radar detection
        self.car.radar(0)
        # Check if radars are detected
        self.assertGreater(len(self.car.radars), 0)

    def test_collision(self):
        # Move car to a known collision point
        self.car.rect.center = (490, 820)
        self.car.collision()
        # Check if the car is marked as not alive due to collision
        self.assertFalse(self.car.alive)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
