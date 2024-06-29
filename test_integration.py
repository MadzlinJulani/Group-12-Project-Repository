
import unittest
import os
import neat
from main import Car, eval_genomes

class TestIntegration(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Get the path to config.txt in the parent directory
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.txt')
        cls.config = neat.config.Config(
            neat.DefaultGenome,
            neat.DefaultReproduction,
            neat.DefaultSpeciesSet,
            neat.DefaultStagnation,
            config_path
        )

    def test_neat_initialization(self):
        pop = neat.Population(self.config)
        self.assertIsInstance(pop, neat.Population)
        
    def test_car_initialization(self):
        car = Car()
        self.assertIsInstance(car, Car)
        self.assertTrue(car.alive)
        self.assertEqual(car.angle, 0)
        self.assertEqual(len(car.radars), 0)
        
    def test_eval_genomes(self):
        # Create a fake genome for testing
        genomes = [(1, neat.DefaultGenome(1))]
        eval_genomes(genomes, self.config)
        # Check if the genome fitness has been set
        self.assertGreaterEqual(genomes[0][1].fitness, 0)

if __name__ == '__main__':
    unittest.main()
