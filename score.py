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
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Score : {score}/{total}".format(score=score, total=self.total), True, (255, 255, 255))
        textRect = text.get_rect()

        self.window.blit(text, textRect)
