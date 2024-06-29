import pytest
import pygame
from main import run
import os

def test_simulation_run():
    # Initialize Pygame
    pygame.init()
    
    # Create a temporary configuration file path
    config_path = os.path.join(os.path.dirname(__file__), 'config.txt')
    
    # Run the simulation 
    run(config_path)
    
    # Check if the population object is created and not None
    assert pop is not None
    assert pop.best_genome is not None
    
    # Quit Pygame
    pygame.quit()

if __name__ == '__main__':
    pytest.main()
