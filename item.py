#! /usr/bin/env python3
# coding: utf-8
""" Item class """
import random


class Item:
    """ Item to find """

    def __init__(self, grid, quantity):
        self.grid = grid
        self.quantity = quantity
        self.__generate()

    def __generate(self):
        """ Generate random position item """

        empty_tile = []
        tile_x = 0
        for line in self.grid:
            tile_y = 0
            for tile_name in line:
                if tile_name == ".":
                    empty_tile.append([tile_x, tile_y])
                tile_y += 1
            tile_x += 1

        item_name = random.sample(["N", "E", "S", "T"], self.quantity)

        i = 0
        for item in random.sample(empty_tile, self.quantity):
            self.grid[item[0]][item[1]] = item_name[i]
            i += 1
