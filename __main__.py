#!/usr/bin/env python3

import pygame
import logging

from game import Game
from window import Window
from assets import Assets

def main():
    pygame.init()
    logging.basicConfig(filename = 'debug.log', level = logging.INFO)
    logging.info("\n===> New Game <===\n")
    game = Game()
    game.mainMenu()
    pygame.quit()

if __name__ == '__main__':
    main()
