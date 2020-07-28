#! /usr/bin/env python3
# coding: utf-8
""" Map"""
import os

import pygame

from constant import TILE_WIDTH, TILE_HEIGHT


class Labyrinth:
    """ Mac Gyver game class to manage Labyrinth """

    def __init__(self, window):
        """ Init"""
        self.grid = []
        self.window = window
        self.images = self.__load_images()
        self.player_position = [0, 0]

    @staticmethod
    def __load_images():
        """ Load images resource from file """

        return {
            "P": {
                "name": "MacGyver Player",
                "image": pygame.transform.scale(
                    pygame.image.load(os.path.join('images', 'player.png')),
                    (TILE_HEIGHT, TILE_WIDTH)
                )
            },
            "W": {
                "name": "Wall",
                "image": pygame.transform.scale(
                    pygame.image.load(os.path.join('images', 'wall.png')),
                    (TILE_HEIGHT, TILE_WIDTH)
                )
            },
            "G": {
                "name": "Guardian",
                "image": pygame.transform.scale(
                    pygame.image.load(os.path.join('images', 'guardian.png')),
                    (TILE_HEIGHT, TILE_WIDTH)
                )
            },
            ".": {
                "name": "Green Path",
                "image": pygame.transform.scale(
                    pygame.image.load(os.path.join('images', 'path.png')),
                    (TILE_HEIGHT, TILE_WIDTH)
                )
            },
            "N": {
                "name": "Needle",
                "image": pygame.transform.scale(
                    pygame.image.load(os.path.join('images', 'needle.png')),
                    (TILE_HEIGHT, TILE_WIDTH)
                )
            },
            "E": {
                "name": "Ether",
                "image": pygame.transform.scale(
                    pygame.image.load(os.path.join('images', 'ether.png')),
                    (TILE_HEIGHT, TILE_WIDTH)
                )
            },
            "S": {
                "name": "Syringe",
                "image": pygame.transform.scale(
                    pygame.image.load(os.path.join('images', 'syringe.png')),
                    (TILE_HEIGHT, TILE_WIDTH)
                )
            },
            "T": {
                "name": "Pipe",
                "image": pygame.transform.scale(
                    pygame.image.load(os.path.join('images', 'pipe.png')),
                    (TILE_HEIGHT, TILE_WIDTH)
                )
            },
        }

    def load_level_from_file(self, filename):
        """ load level from file """
        self.grid = []
        if os.path.exists(filename):  # Check if the file exists
            with open(filename, "r") as file:
                for line in file:
                    # Remove line breaks and convert the string to an array
                    self.grid.append(list(line.strip()))
        else:
            raise FileExistsError(filename)

        return self.grid

    def draw(self):
        """ Draw the images on the grid"""

        tile_x = 0
        for line in self.grid:
            tile_y = 0
            for tile_name in line:
                if tile_name == "P":
                    self.player_position = [tile_x, tile_y]
                # For the player and the goalkeeper add the green background
                if tile_name in ("P", "G"):
                    self.__tile_draw(".", tile_x, tile_y)

                self.__tile_draw(tile_name, tile_x, tile_y)

                tile_y += 1
            tile_x += 1
        # Refresh windows
        pygame.display.flip()

    def __tile_draw(self, tile_name, tile_x, tile_y):
        """ Draw a tile in active window """

        if self.images.get(tile_name) is not None:  # if the tile is not available
            self.window.blit(
                self.images.get(tile_name)["image"],
                [
                    tile_y * TILE_HEIGHT,
                    tile_x * TILE_WIDTH
                ]
            )
        else:
            raise Exception('TileNotImplemented', tile_name)
