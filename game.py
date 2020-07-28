#! /usr/bin/env python3
# coding: utf-8
""" MacGyver project"""
import pygame

from constant import DISPLAY_MODE, DISPLAY_GAME_TITLE, BACKGROUND_COLOR, TREASURE_TOTAL
from labyrinth import Labyrinth
from player import Player
from treasure import Treasure
from score import Score


def main():
    """ Main function """

    pygame.init()  # Initialize pygame

    window = pygame.display.set_mode(DISPLAY_MODE)  # Set the window size of the screen

    pygame.display.set_caption(DISPLAY_GAME_TITLE)  # Set title of screen

    window.fill(BACKGROUND_COLOR)  # Set the background color

    labyrinth = Labyrinth(window)
    labyrinth.load_level_from_file("level/level1.map")  # Load level one

    Treasure(labyrinth.grid, TREASURE_TOTAL)
    labyrinth.draw()

    score = Score(window, TREASURE_TOTAL)
    score.draw()

    player = Player(labyrinth.grid, labyrinth.player_position, TREASURE_TOTAL)

    # Loop until the user clicks the close button.
    done = False
    while not done:
        pygame.time.Clock().tick(60)  # Update the clock

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:  # If user press key
                player.move(event.key)  # Move player
                labyrinth.draw()  # Update labyrinth
                score.draw(player.score)  # Update score

        pygame.display.update()
    print("Exit Game")


if __name__ == "__main__":
    main()
