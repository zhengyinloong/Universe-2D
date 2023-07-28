# -*- coding:utf-8 -*-
# cle.py in Universe-2D
# zhengyinloong
# 2023/07/26 00:59
import math

from body import *


# ai = v^2/Ri
# ai = G*Mj/L^2
# L = Ri+Rj
# Ms = Mi+Mj
# ==> v = √(G/L*Ms)

def v_by_2_bodys(body1: Body, body2: Body, G=6.67430e-11):
    re_pos = vctr(body2.pos - body1.pos)
    m1, m2 = body1.mass, body2.mass
    M = m1 + m2
    L = re_pos.length()
    v1 = math.sqrt(G / (L * M)) * m2
    v2 = math.sqrt(G / (L * M)) * m1
    V1 = re_pos.normalize().rotate(90) * v1
    V2 = re_pos.normalize().rotate(-90) * v2

    # R1, R2 = vctr(body2.mass, body1.mass) * L / M

    return V1, V2
