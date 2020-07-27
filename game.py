#! /usr/bin/env python3
# coding: utf-8
""" MacGyver project"""

import os
import pygame

from constant import*
from labyrinth import Labyrinth
from player import Player
from treasure import Treasure


def main():
    """ Main function """

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    window = pygame.display.set_mode(DISPLAY_MODE)

    # Set title of screen
    pygame.display.set_caption(DISPLAY_GAME_TITLE)

    # Set the background color
    window.fill(BACKGROUND_COLOR)

    labyrinth = Labyrinth(window)
    labyrinth.load_level_from_file("level/level1.map")
    Treasure(labyrinth.grid)

    labyrinth.draw()


    player = Player(labyrinth.grid, labyrinth.player_position)

    # Loop until the user clicks the close button.
    done = False
    while not done:
        pygame.time.Clock().tick(60)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                player.move(event.key)
                labyrinth.draw()

        pygame.display.update()
    print("Exit Game")


if __name__ == "__main__":
    main()
