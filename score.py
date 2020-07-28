#! /usr/bin/env python3
# coding: utf-8
""" Score """
import pygame


class Score:
    """ Score"""

    def __init__(self, window, total):
        self.window = window
        self.total = total

    def draw(self, score=0):
        """ Draw the score in the grid """

        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(
            "Score : {score}/{total}".format(score=score, total=self.total),
            True,
            (255, 255, 255)
        )
        text_rect = text.get_rect(x=350, y=5)

        self.window.blit(text, text_rect)
