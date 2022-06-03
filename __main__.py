#!/usr/bin/env python3

import pygame
import logging

from game import Game
from window import Window
from assets import Assets

def main():
    pygame.init()
    logging.basicConfig(
        filename='debug.log',
        format='%(levelname)s: %(asctime)s: %(message)s',
        datefmt='%H:%M:%S',
        level=logging.INFO
    )
    logging.info("")
    logging.info("===> New Game <===")
    logging.info("")
    game = Game()
    game.mainMenu()
    pygame.quit()

if __name__ == '__main__':
    main()
