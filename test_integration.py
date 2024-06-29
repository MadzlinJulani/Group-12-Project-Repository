import unittest
from main import Car

class TestCar(unittest.TestCase):
    
    def setUp(self):
        self.car = Car()
    
    def test_initial_position(self):
        self.assertEqual(self.car.rect.center, (490, 820))
    
    def test_initial_velocity(self):
        self.assertEqual(self.car.vel_vector, pygame.math.Vector2(0.8, 0))
    
    def test_drive(self):
        initial_position = self.car.rect.center
        self.car.drive()
        self.assertNotEqual(self.car.rect.center, initial_position)
    
    def test_collision_detection(self):
        self.car.rect.center = (0, 0)  # Place the car at a position where it collides
        self.car.collision()
        self.assertFalse(self.car.alive)
    
    def test_radar(self):
        self.car.radar(0)
        self.assertEqual(len(self.car.radars), 1)
        self.assertIsInstance(self.car.radars[0], list)
    
    def test_data(self):
        self.car.radar(0)
        data = self.car.data()
        self.assertEqual(len(data), 5)
        self.assertTrue(all(isinstance(d, int) for d in data))

if __name__ == '__main__':
    unittest.main()
