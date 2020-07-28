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
        """ Move the player with the keyboard """

        tile_x = 0
        tile_y = 0

        if key == pygame.K_UP:
            self.__move_in_grid(-1, tile_y)
        elif key == pygame.K_DOWN:
            self.__move_in_grid(1, tile_y)
        elif key == pygame.K_LEFT:
            self.__move_in_grid(tile_x, -1)
        elif key == pygame.K_RIGHT:
            self.__move_in_grid(tile_x, 1)

    def __move_in_grid(self, tile_x, tile_y):
        """ Move player in the grid"""

        if self.__possible_to_be_moved(tile_x, tile_y):

            self.__collect_object(tile_x, tile_y)

            self.__is_finish(tile_x, tile_y)

            # Restore last tile
            self.__set_current_tile(self.last_tile)

            # Set last tile for the restore
            self.last_tile = self.__get_new_tile(tile_x, tile_y)

            # Move Player in the Grid
            self.__set_new_tile(tile_x, tile_y, "P")

            # Save player position
            self.player_position = [
                self.player_position[0] + tile_x,
                self.player_position[1] + tile_y
            ]

    def __collect_object(self, tile_x, tile_y):
        """ Collect the object and increment a point """

        if self.__get_new_tile(tile_x, tile_y) in ("N", "E", "S", "T"):
            self.__set_new_tile(tile_x, tile_y, ".")
            self.score += 1

    def __is_finish(self, tile_x, tile_y):
        """ Check if the game is over """
        if self.__get_new_tile(tile_x, tile_y) == "G":
            if self.score == self.total_score:
                self.__set_new_tile(tile_x, tile_y, ".")
                self.is_finish = True
                return True
            else:
                print("Il manque des éléments")
                return False
        return False

    def __possible_to_be_moved(self, tile_x, tile_y):
        """ Check is possible to be move """

        if self.__get_new_tile(tile_x, tile_y) == "W":
            return False
        return True

    def __get_current_tile(self):
        """ Get current tile """
        return self.grid[self.player_position[0]][self.player_position[1]]

    def __set_current_tile(self, tile):
        """ Set current tile """
        self.grid[self.player_position[0]][self.player_position[1]] = tile

    def __get_new_tile(self, tile_x, tile_y):
        """ get new tile """
        return self.grid[self.player_position[0] + tile_x][self.player_position[1] + tile_y]

    def __set_new_tile(self, tile_x, tile_y, tile):
        """ set new tile """
        self.grid[self.player_position[0] + tile_x][self.player_position[1] + tile_y] = tile
