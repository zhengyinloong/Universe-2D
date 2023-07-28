# -*- coding:utf-8 -*-
# physical_laws.py in Universe-2D
# zhengyinloong
# 2023/07/25 13:50

from body import *


class PhysicalLaws:
    # physical constants
    c = 2.99792458e8  # velocity of light
    G = 6.67430e-11  # gravitational constant

    Mass_Solar = 1.989e30  # The mass of the sun, in kilograms
    Mass_Earth = 5.972e24  # The mass of the Earth, in kilograms
    Mass_Moon = 7.348e22  # The mass of the Moon, in kilograms

    # R_s = 6.957e7
    # R_e = 6.371e6
    # R_m = 1737500

    R_s = 20
    R_e = 10
    R_m = 5

    R_e2s = 1.496e11
    R_m2e = 3.844e8

    V_e = 2.978e4
    V_m = 1.02e3
    # scales
    pos_scale = 1e-10
    time_scale = 1e7
    Light_second = c*1
    Light_year = c*3600*24*365
    def __init__(self, universe):
        self.universe = universe


