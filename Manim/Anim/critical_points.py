import random as rd
from manim import *
from manim.utils.color.BS381 import RED_OXIDE
from manim.utils.color.X11 import GRAY60, PALETURQUOISE4
from manim.utils.color.XKCD import (
    BLUEPURPLE,
    BROWNGREEN,
    GREYBROWN,
    MOSSGREEN,
    NEONGREEN,
    ORANGEYYELLOW,
    PALEBLUE,
    PINEGREEN,
)
from manim.utils.unit import Percent


class Crit(Scene):
    def construct(self):
        c = Circle(color=GREYBROWN, fill_opacity=0.5)
        self.play(FadeIn(c))
        cross_color = [RED, GREEN, BLUE, YELLOW]
        for d in [(0, 0, 0), UP, RIGHT, UR, DR, DOWN, DL, LEFT, UL]:
            size = len(cross_color)
            index = rd.randint(0, size - 1)
            self.play(
                Create(
                    (
                        Cross(scale_factor=0.2).move_to(c.get_critical_point(d))
                    ).set_color(cross_color[index])
                )
            )
        color = [
            RED_OXIDE,
            ORANGEYYELLOW,
            PINEGREEN,
            MOSSGREEN,
            BLUEPURPLE,
            GRAY60,
            NEONGREEN,
            PALEBLUE,
            MAROON_E,
            BROWNGREEN,
        ]
        for perc in range(15, 51, 5):
            size = len(color)
            index = rd.randint(0, size - 1)
            self.play(
                Create(Circle(radius=perc * Percent(X_AXIS)).set_color(color[index]))
            )
