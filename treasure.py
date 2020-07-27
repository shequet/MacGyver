#! /usr/bin/env python3
# coding: utf-8
""" Treasure """
import random


class Treasure:
    """ Treasure to find """
    def __init__(self, grid):
        self.grid = grid
        self.__generate()

    def __generate(self, quantity=3):
        empty_tile = []
        x = 0
        for line in self.grid:
            y = 0
            for tile_name in line:
                if tile_name == ".":
                    empty_tile.append([x, y])
                y += 1
            x += 1

        treasure_name = random.sample(["N", "E", "S", "T"], quantity)

        i = 0
        for item in random.sample(empty_tile, quantity):
            self.grid[item[0]][item[1]] = treasure_name[i]
            i += 1


