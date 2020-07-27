#! /usr/bin/env python3
# coding: utf-8
""" Player"""
import pygame


class Player:
    """ Play in the Game (MacGyver) """
    def __init__(self, grid, player_position):
        self.last_tile = "."
        self.grid = grid
        self.player_position = player_position

    def move(self, key):
        """ Move player """

        x = 0
        y = 0

        if key == pygame.K_UP:
            self.__move_in_grid(-1, y)
        elif key == pygame.K_DOWN:
            self.__move_in_grid(1, y)
        elif key == pygame.K_LEFT:
            self.__move_in_grid(x, -1)
        elif key == pygame.K_RIGHT:
            self.__move_in_grid(x, 1)

    def __move_in_grid(self, x, y):
        """ Move player in grid"""

        if self.__possible_to_be_moved(x, y):

            # Restore last tile
            self.grid[self.player_position[0]][self.player_position[1]] = self.last_tile

            # Set last tile for the restore
            self.last_tile = self.grid[self.player_position[0] + x][self.player_position[1] + y]

            # Move Player in the Grid
            self.grid[self.player_position[0] + x][self.player_position[1] + y] = "P"

            self.player_position = [self.player_position[0] + x, self.player_position[1] + y]

    def __possible_to_be_moved(self, x, y):
        if self.grid[self.player_position[0] + x][self.player_position[1] + y] == "W":
            return False
        return True
