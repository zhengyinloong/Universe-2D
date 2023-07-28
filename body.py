# -*- coding:utf-8 -*-
# body.py in Universe-2D
# zhengyinloong
# 2023/07/25 12:52

import pygame as pg
import math

vctr = pg.Vector2


class Body:
    def __init__(self, universe, name='body', mass=1, radius=4,
                 position=vctr(10, 10), velcity=vctr(0, 0),
                 color='white'):
        self.universe = universe
        self.name = name
        self.law = self.universe.law
        self.mass = mass
        self.radius = radius
        self.a = vctr(0, 0)
        self.R = 0
        self.center = vctr(0, 0)
        self.density = self.colect_body_density(self)
        self.velocity = velcity
        self.pos = position
        self.next_vel = self.velocity
        self.next_pos = self.pos
        self.dists_to = {}
        self.color = color

    def draw(self, is_track):
        self.draw_pos = self.pos * self.law.pos_scale + self.universe.center
        pg.draw.circle(self.universe.screen, self.color,
                       self.draw_pos, self.radius)
        if is_track:
            pg.draw.circle(self.universe.screen, self.color, self.center * self.law.pos_scale + self.universe.center,
                           radius=self.R * self.law.pos_scale, width=1)

        pass

    def draw_infos(self):
        self.universe.draw_text(f'{self.name:6s} position: {self.pos}', self.universe.next_info_pos,
                                text_color=self.color)
        self.universe.draw_text(f'{"":6s} velocity: {self.velocity}', self.universe.next_info_pos,
                                text_color=self.color)
        self.universe.draw_text(self.name, self.draw_pos + (self.radius, 0),
                                text_color=self.color)
    @staticmethod
    def colect_body_density(body):
        volume = 4 * math.pi * body.radius ** 3 / 3
        body.density = body.mass / volume

        return body.density

    def celect_next_pos_and_v(self):
        F = vctr(0, 0)
        self.cs = {}
        is_c = False
        for otherbody in self.universe.body_list:
            if otherbody != self:
                f = self.calculate_gravity_2(otherbody)
                F += f
        """
                if self.dists_to[otherbody] < self.radius + otherbody.radius:
                    is_c = True
                    self.cs[otherbody] = True
        if is_c:
            for ob, is_p in self.cs.items():
                # ob.next_pos=ob.pos
                if ob.mass < self.mass:
                    self.universe.body_list.remove(ob)
                    self.mass += ob.mass
                    ob.velocity.update(0, 0)
                else:
                    ob.velocity.update(ob.velocity.rotate(180))
        """
        a = F / self.mass
        self.a.update(a)
        self.R = self.velocity.dot(self.velocity) / self.a.length()
        self.center.update(self.a.normalize() * self.R + self.pos)
        vx, vy = self.velocity + a * (self.universe.dt / 1000) * self.law.time_scale
        self.next_vel.update(vx, vy)
        x, y = self.next_pos + self.velocity * (self.universe.dt / 1000) * self.law.time_scale

        self.next_pos.update(x, y)

    def update_pos_and_v(self):
        self.velocity.update(self.next_vel)
        self.pos.update(self.next_pos)

    def calculate_gravity_2(self, otherbody):
        # F, R = self.law.calculate_gravity_2(self, otherbody)
        m1, m2 = self.mass, otherbody.mass
        p1, p2 = self.pos, otherbody.pos
        re_pos = p2 - p1
        R = re_pos.length()
        self.dists_to[otherbody] = R
        F_mod = self.law.G * m1 * m2 / (R ** 2)
        F = re_pos.normalize() * F_mod
        return F


class Star(Body):
    id = 'Star'

    def __init__(self, universe, name='star', mass=100, radius=20,
                 position=vctr(0, 0), velcity=vctr(0, 0), color='yellow'):
        super().__init__(universe=universe, mass=mass, radius=radius,
                         position=position, velcity=velcity)
        self.name = name
        self.color = color


class Planet(Body):
    id = 'Planet'

    def __init__(self, universe, name='planet', mass=10, radius=10,
                 position=vctr(0, 0), velcity=vctr(0, 0), color=(135, 206, 250)):
        super().__init__(universe=universe, mass=mass, radius=radius,
                         position=position, velcity=velcity)
        self.name = name
        self.color = color


class Satellite(Body):
    id = 'Satellite'

    def __init__(self, universe, name='satellite', mass=1, radius=5,
                 position=vctr(0, 0), velcity=vctr(0, 0), color='white'):
        super().__init__(universe=universe, mass=mass, radius=radius,
                         position=position, velcity=velcity)
        self.name = name
        self.color = color


class Asteroid(Body):
    id = 'Asteroid'

    def __init__(self, universe, name='asteroid', mass=1, radius=2,
                 position=vctr(0, 0), velcity=vctr(0, 0), color='white'):
        super().__init__(universe=universe, mass=mass, radius=radius,
                         position=position, velcity=velcity, color=color)
        self.name = name
