#! /usr/bin/env python3
# coding: utf-8
""" MacGyver project"""
import pygame

from constant import DISPLAY_MODE, DISPLAY_GAME_TITLE, ITEM_TOTAL
from labyrinth import Labyrinth
from player import Player
from item import Item
from score import Score


def main():
    """ Main function """

    pygame.init()  # Initialize pygame

    window = pygame.display.set_mode(DISPLAY_MODE)  # Set the window size of the screen

    pygame.display.set_caption(DISPLAY_GAME_TITLE)  # Set title of screen

    labyrinth = Labyrinth(window)
    labyrinth.load_level_from_file("level/level1.map")  # Load level one

    Item(labyrinth.grid, ITEM_TOTAL)
    labyrinth.draw()

    score = Score(window, ITEM_TOTAL)
    score.draw()

    player = Player(
        window,
        labyrinth.grid,
        labyrinth.player_position,
        ITEM_TOTAL
    )

    # Loop until the user clicks the close button.
    done = False
    while not done:
        pygame.time.Clock().tick(1000)  # Update the clock

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN and player.is_finish is None:
                player.move(event.key)  # Move player
                labyrinth.draw()  # Update labyrinth
                score.draw(player.score)  # Update score
                player.game_over()  # Show Game Over

        pygame.display.update()


if __name__ == "__main__":
    main()
