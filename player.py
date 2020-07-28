#! /usr/bin/env python3
# coding: utf-8
""" Player"""
import pygame


class Player:
    """ Play in the Game (MacGyver) """
    def __init__(self, grid, player_position, total_score):
        self.last_tile = "."
        self.grid = grid
        self.player_position = player_position
        self.score = 0
        self.total_score = total_score
        self.is_finish = False

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

            self.__collect_object(x, y)

            self.__is_finish(x, y)

            # Restore last tile
            self.__set_current_tile(self.last_tile)

            # Set last tile for the restore
            self.last_tile = self.__get_new_tile(x, y)

            # Move Player in the Grid
            self.__set_new_tile(x, y, "P")

            # Save player position
            self.player_position = [self.player_position[0] + x, self.player_position[1] + y]

    def __collect_object(self, x, y):
        """ Collect object and add score"""
        if self.__get_new_tile(x, y) in ("N", "E", "S", "T"):
            self.__set_new_tile(x, y, ".")
            self.score += 1

    def __is_finish(self, x, y):
        """ Check is finish the game """
        if self.__get_new_tile(x, y) == "G":
            if self.score == self.total_score:
                self.__set_new_tile(x, y, ".")
                self.is_finish = True
                return True
            else:
                print("Il manque des éléments")
        return False

    def __possible_to_be_moved(self, x, y):
        """ Check is possible to be move """
        if self.__get_new_tile(x, y) == "W":
            return False
        return True

    def __get_current_tile(self):
        """ Get current tile """
        return self.grid[self.player_position[0]][self.player_position[1]]

    def __set_current_tile(self, tile):
        """ Set current tile """
        self.grid[self.player_position[0]][self.player_position[1]] = tile

    def __get_new_tile(self, x, y):
        """ get new tile """
        return self.grid[self.player_position[0] + x][self.player_position[1] + y]

    def __set_new_tile(self, x, y, tile):
        """ set new tile """
        self.grid[self.player_position[0] + x][self.player_position[1] + y] = tile

