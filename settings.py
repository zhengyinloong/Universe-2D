# -*- coding:utf-8 -*-
# settings.py in Universe-2D
# zhengyinloong
# 2023/07/28 10:53
from body import *
from universe import Universe
import pygame as pg


class Settings:
    def __init__(self, universe: Universe):
        self.universe = universe

        # basic settings
        self.universe.size = vctr(600, 600)
        self.universe.universe_center = vctr(0, 0)
        self.universe.screen = pg.display.set_mode(self.universe.size)
        self.universe.screen_center = vctr(self.universe.size / 2)
        self.universe.center = vctr(self.universe.size / 2)

        # time
        self.universe.clock = pg.time.Clock()
        self.universe.dt = 16
        self.universe.time = 0

        self.universe.body_list = []

        # mouse settings
        self.universe.mouse_rel = vctr(0, 0)  # for mouse drag
        self.universe.is_mouse_left_button_down = False

        self.universe.law.time_scale = 1e0 * 3600 * 24 * 365 * 3  # e-m system
        self.universe.law.pos_scale = 1e-9

        self.universe.body_types = [Star, Planet, Satellite, Asteroid]
        self.universe.weights = (0, 2, 1, 1)
        self.universe.body_number = 2

        self.universe.text_font = 'Courier std'
        # self.text_font = 'Courier New'
        self.universe.font_size = 15
        self.universe.next_info_pos = vctr(0, 0)
        self.universe.time_unit = 'year'

        self.universe.scale_by_mouse_ball = 1.0
        self.universe.mouse_sensitivity = 0.1
