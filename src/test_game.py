import pytest
import pygame
import time
from Jogo import Game  # Import the Game class from your module

# Create a fixture to initialize a Game instance for testing
@pytest.fixture
def game_instance():
    # pygame.init()
    game = Game()
    return game

# Test the initialization of the Game class
def test_game_initialization(game_instance):
    assert game_instance.vida == 3
    assert game_instance.moedinha == 0
    pygame.quit()

# Test the load_data method
def test_load_data(game_instance):
    game_instance.load_data()
    # Add assertions to check that data is loaded correctly
    assert game_instance.spritesheet != None
    assert game_instance.nuvem_images != None
    assert game_instance.som_dir != None
    assert game_instance.jump_sound != None
    assert game_instance.boost_sound != None
    pygame.quit()