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
    # R_m = 1.7375e6

    R_s = 20
    R_e = 10
    R_m = 1

    R_e2s = 1.496e11
    R_m2e = 3.844e8

    V_e = 2.978e4
    V_m = 1.02e3
    # scales
    pos_scale = 1e-9
    time_scale = 1e7
    Light_second = c * 1
    Light_year = c * 3600 * 24 * 365

    def __init__(self, universe):
        self.universe = universe

    def circle_velocity_of_2_bodies(self, body1: Body, body2: Body):
        """
        anticlockwise
        """
        re_pos = vctr(body2.pos - body1.pos)
        m1, m2 = body1.mass, body2.mass
        M = m1 + m2
        L = re_pos.length()
        v1 = math.sqrt(self.G / (L * M)) * m2
        v2 = math.sqrt(self.G / (L * M)) * m1
        V1 = re_pos.normalize().rotate(90) * v1
        V2 = re_pos.normalize().rotate(-90) * v2

        # R1, R2 = vctr(body2.mass, body1.mass) * L / M

        return V1, V2

    def gravity_by_otherbody(self, body1: Body, body2: Body):
        # F, R = self.law.calculate_gravity_2(self, otherbody)
        m1, m2 = body1.mass, body2.mass
        p1, p2 = body1.pos, body2.pos
        re_pos = p2 - p1
        R = re_pos.length()
        body1.dists_to[body2] = R
        F_mod = self.G * m1 * m2 / (R ** 2)
        F = re_pos.normalize() * F_mod
        return F
