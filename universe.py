# -*- coding:utf-8 -*-
# universe.py in Universe-2D
# zhengyinloong
# 2023/07/25 12:48

from imports import *


class Universe:
    def __init__(self, name):
        pg.init()
        self.name = name
        self.law = PhysicalLaws(self)
        self.settings = Settings(self)

        # spawn bodys
        # self.add_system()

        # Special systems
        self.solar_system(asteroid_number=6)
        # self.double_star_system()
        # self.earth_system()

    def add_system(self):

        self.Solar = Star(self, 'Solar', radius=self.law.R_s,
                          position=vctr(0, 0), velcity=vctr(0, 0))

        self.Earth = Planet(self, 'Earth', radius=self.law.R_e,
                            position=vctr(0, 0), velcity=vctr(0, 0))
        self.Moon = Satellite(self, 'Moon', radius=self.law.R_m,
                              position=vctr(0, 0), velcity=vctr(0, 0))

        self.Solar.mass = self.law.Mass_Solar
        self.Earth.mass = self.law.Mass_Earth
        self.Moon.mass = self.law.Mass_Moon * 10

        self.Earth.pos.update(self.law.R_e2s, 0)
        self.Moon.pos.update(self.law.R_e2s + self.law.R_m2e * 10, 0)

        vgms, vgsm = self.law.circle_velocity_of_2_bodies(self.Moon, self.Solar)
        vges, vgse = self.law.circle_velocity_of_2_bodies(self.Earth, self.Solar)
        vgme, vgem = self.law.circle_velocity_of_2_bodies(self.Moon, self.Earth)
        # self.Solar.velocity.update(vgse + vgsm)
        self.Earth.velocity.update(vges + vgem)
        self.Moon.velocity.update(vgms + vgme)
        print(vgms, vges)

        self.add_body(self.Solar)
        self.add_body(self.Earth)
        self.add_body(self.Moon)

        self.time_unit = 'day'
        self.law.time_scale = 1 * 3600
        self.law.pos_scale = 1e-10

    def solar_system(self, asteroid_number=10):
        """
        solar system (no moons)
        :return:
        """
        self.Solar = Star(self, 'Solar', mass=self.law.Mass_Solar, radius=self.law.R_s,
                          position=vctr(0, 0),
                          velcity=vctr(0, 0))
        self.add_body(self.Solar)

        self.Earth = Planet(self, 'Earth', mass=self.law.Mass_Earth, radius=self.law.R_e,
                            position=vctr(0, self.law.R_e2s),
                            velcity=vctr(self.law.V_e, 0))
        V, V2 = self.law.circle_velocity_of_2_bodies(self.Earth, self.Solar)
        self.Earth.velocity.update(V)
        self.add_body(self.Earth)

        self.Mercury = Planet(self, 'Mercury', mass=3.285e23, radius=self.law.R_e,
                              position=vctr(0, 57.91e9),
                              velcity=vctr(0, 0),
                              color=(169, 169, 169))
        V, V2 = self.law.circle_velocity_of_2_bodies(self.Mercury, self.Solar)
        self.Mercury.velocity.update(V)
        self.add_body(self.Mercury)

        self.Venus = Planet(self, 'Venus', mass=4.867e24, radius=self.law.R_e,
                            position=vctr(0, 108.2e9),
                            velcity=vctr(0, 0),
                            color='purple')
        V, V2 = self.law.circle_velocity_of_2_bodies(self.Venus, self.Solar)
        self.Venus.velocity.update(V)
        self.add_body(self.Venus)

        self.Mars = Planet(self, 'Mars', mass=6.39e23, radius=self.law.R_e,
                           position=vctr(0, 227.9e9),
                           velcity=vctr(0, 0),
                           color=(255, 69, 0))
        V, V2 = self.law.circle_velocity_of_2_bodies(self.Mars, self.Solar)
        self.Mars.velocity.update(V)
        self.add_body(self.Mars)

        self.Jupiter = Planet(self, 'Jupiter', mass=1.898e27, radius=self.law.R_e,
                              position=vctr(0, 778.6e9),
                              velcity=vctr(0, 0),
                              color=(255, 140, 0))
        V = self.law.circle_velocity_of_2_bodies(self.Jupiter, self.Solar)[0]
        self.Jupiter.velocity.update(V)
        self.add_body(self.Jupiter)

        self.Saturn = Planet(self, 'Saturn', mass=5.683e26, radius=self.law.R_e,
                             position=vctr(0, 1427e9),
                             velcity=vctr(0, 0),
                             color=(210, 180, 140))
        V = self.law.circle_velocity_of_2_bodies(self.Saturn, self.Solar)[0]
        self.Saturn.velocity.update(V)
        self.add_body(self.Saturn)

        self.Uranus = Planet(self, 'Uranus', mass=8.681e25, radius=self.law.R_e,
                             position=vctr(0, 2871e9),
                             velcity=vctr(0, 0),
                             color=(0, 255, 255))
        V = self.law.circle_velocity_of_2_bodies(self.Uranus, self.Solar)[0]
        self.Uranus.velocity.update(V)
        self.add_body(self.Uranus)

        self.Neptune = Planet(self, 'Neptune', mass=1.024e26, radius=self.law.R_e,
                              position=vctr(0, 4498e9),
                              velcity=vctr(0, 0),
                              color=(65, 255, 128))
        V = self.law.circle_velocity_of_2_bodies(self.Neptune, self.Solar)[0]
        self.Neptune.velocity.update(V)
        self.add_body(self.Neptune)

        angle = 0
        for n in range(asteroid_number):
            pos = vctr(0, rdm0_1() * (4.2e11 - 2.2e11) + 2.2e11 + self.law.R_e2s)
            self.asteroid = Asteroid(self, f'asteroid_{n}', mass=1,
                                     position=pos,
                                     velcity=vctr(0, 0))
            pos = vctr(self.asteroid.pos.rotate(angle))
            self.asteroid.pos.update(pos)
            V = vctr(self.law.circle_velocity_of_2_bodies(self.asteroid, self.Solar)[0])
            self.asteroid.velocity.update(V)
            self.add_body(self.asteroid)
            angle += 360 / asteroid_number * rdm0_1()

        self.Comet = Satellite(self, f'Comet', mass=1, radius=1,
                               position=self.Jupiter.pos.rotate(90),
                               velcity=vctr(0, 0))
        V = vctr(self.law.circle_velocity_of_2_bodies(self.Comet, self.Solar)[0]).rotate(60)
        self.Comet.velocity.update(V)
        self.add_body(self.Comet)
        self.Moon = Satellite(self, 'Moon', mass=self.law.Mass_Moon, radius=self.law.R_m,
                              position=self.Earth.pos + vctr(self.law.R_m2e, 0),
                              velcity=vctr(0, 0))
        self.Moon.velocity.update(self.Earth.velocity + self.law.circle_velocity_of_2_bodies(self.Moon, self.Earth)[0])
        # self.add_body(self.Moon)

        self.law.time_scale = 3600 * 24 * 365
        self.time_unit = 'year'
        self.font_size = 10

    def earth_system(self):

        self.Earth = Planet(self, 'Earth', mass=self.law.Mass_Earth, radius=self.law.R_e,
                            position=vctr(0, 0),
                            velcity=vctr(0, 0))
        self.Moon = Satellite(self, 'Moon', mass=self.law.Mass_Moon, radius=self.law.R_m,
                              position=vctr(0, self.law.R_m2e),
                              velcity=vctr(0, 0))

        V1, V2 = self.law.circle_velocity_of_2_bodies(self.Earth, self.Moon)
        self.Earth.velocity.update(V1)
        self.Moon.velocity.update(V2)
        self.add_body(self.Earth)
        self.add_body(self.Moon)

    def double_star_system(self):
        self.star1 = Star(self, 'star1', mass=self.law.Mass_Solar, radius=self.law.R_s,
                          position=vctr(-self.law.R_e2s / 2, 0),
                          velcity=vctr(0, 0))
        # self.Earth = Planet(self, 'Earth', mass=self.law.Mass_Earth, radius=self.law.R_e,
        #                     position=vctr(0, self.law.R_e2s),
        #                     velcity=vctr(self.law.V_e, 0))
        self.star2 = Star(self, 'star2', mass=self.law.Mass_Solar, radius=self.law.R_s,
                          position=vctr(self.law.R_e2s / 2, 0),
                          velcity=vctr(0, 0))
        V1, V2 = self.law.circle_velocity_of_2_bodies(self.star1, self.star2)
        self.star1.velocity.update(V1)
        self.star2.velocity.update(V2)
        self.add_body(self.star1)
        self.add_body(self.star2)
        self.earth_system()

    def add_body(self, body: Body):
        self.body_list.append(body)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

    def update(self):
        pg.display.flip()
        self.clock.tick(1000 / self.dt)

        [cele.celect_next_pos_and_v() for cele in self.body_list]
        [cele.update_pos_and_v() for cele in self.body_list]
        pg.display.set_caption(f'{self.name}')
        self.time += self.dt * self.law.time_scale

    def draw(self):
        self.screen.fill('black')
        [body.draw(is_draw_track=True, track_num=200) for body in self.body_list]
        self.draw_time(self.time_unit)
        self.draw_center()
        self.draw_relative_scaling()
        self.draw_infos()

        self.next_info_pos.update(vctr(0, 0))

    def draw_infos(self):

        for i, body in enumerate(self.body_list):
            if type(body) != Asteroid:
                body.draw_infos()

    def draw_relative_scaling(self):
        self.draw_text(f'{"distence scale":15s}: {self.scale_by_mouse_ball * 100:4.1f} %', self.next_info_pos)

    def draw_time(self, d='second'):
        text = f'({d})'
        if d == 'second':
            text += str(f'{self.time / 1000 :.3f}')
        elif d == 'minute':
            text += str(f'{self.time / (1000 * 60):.3f}')
        elif d == 'hour':
            text += str(f'{self.time / (1000 * 60 * 60):.3f}')
        elif d == 'day':
            text += str(f'{self.time / (1000 * 60 * 60 * 24):.3f}')
        elif d == 'month':
            text += str(f'{self.time / (1000 * 60 * 60 * 24 * 30):.3f}')
        elif d == 'year':
            text += str(f'{self.time / (1000 * 60 * 60 * 24 * 365):.3f}')
        else:
            text = '(second)'
            text += str(f'{self.time / (1000):.3f}')
        text = 'time' + text
        self.draw_text(text, self.next_info_pos)

    def draw_text(self, text, text_pos, text_color='white'):
        # pygame.freetype.Font
        font = pg.font.SysFont(self.text_font, self.font_size)
        _text = font.render(text, True, text_color)
        text_rect = _text.get_rect()
        text_rect.x, text_rect.y = text_pos
        self.screen.blit(_text, text_rect)

        if text_pos == self.next_info_pos:
            self.next_info_pos += vctr(0, self.font_size)

    def draw_center(self):
        ux = (self.center - self.screen_center)[0]
        uy = -(self.center - self.screen_center)[1]
        self.universe_center.update(ux, uy)
        self.draw_text(f'univers  center: {self.universe_center}', self.next_info_pos)
        pass

    def check_events(self):
        # pg.mouse.get_rel()
        for _event in pg.event.get():
            if _event.type == pg.QUIT or (_event.type == pg.KEYDOWN and _event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            self.check_mouse_events(_event)

    def check_mouse_events(self, _event):
        a = 1
        if _event.type == pg.MOUSEBUTTONDOWN:
            if _event.button == 1:
                self.is_mouse_left_button_down = True
            # back to center
            elif _event.button == 3:
                self.center.update(self.screen_center)
            # pos scale by mouse
            elif _event.button == 4:
                a += self.mouse_sensitivity
                self.scale_by_mouse_ball += self.mouse_sensitivity
                self.law.pos_scale = self.law.pos_scale * a
            elif _event.button == 5:
                a -= self.mouse_sensitivity
                self.scale_by_mouse_ball -= self.mouse_sensitivity
                self.law.pos_scale = self.law.pos_scale * a
            else:
                pass
        elif _event.type == pg.MOUSEBUTTONUP:
            if _event.button == 1:
                self.is_mouse_left_button_down = False
        elif _event.type == pg.MOUSEMOTION:
            self.mouse_rel.update(pg.mouse.get_rel())
            if self.is_mouse_left_button_down:
                self.center += self.mouse_rel


if __name__ == '__main__':
    unvs = Universe('Solar System')
    unvs.run()
