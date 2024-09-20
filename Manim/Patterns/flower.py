from manim import *
from manim.utils.color.XKCD import PALEBLUE
import numpy as np

config.pixel_height = 1080
config.pixel_width = 1920
config.frame_height = 9
config.frame_width = 16


class RosePattern(VMobject):
    def __init__(self, radius=2, k=10, theta_range=TAU, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.k = k
        step_size = 0.05
        theta = np.arange(0, theta_range + step_size, step_size)

        # Calculate points based on the parametric rose curve formula
        points = [
            [
                radius * np.cos(k * t) * np.cos(t),
                radius * np.cos(k * t) * np.sin(t),
                0,  # Z-coordinate, since this is a 2D curve
            ]
            for t in theta
        ]

        # Set points smoothly for smooth curve drawing
        self.set_points_smoothly(points)


class RosePatternScene(Scene):
    def construct(self):
        text = (
            MathTex(
                "RosePattern",
            )
            .set_opacity(0.7)
            .set_color(PALEBLUE)
            .move_to(UL * 3)
        )
        rose = RosePattern(radius=3, k=15, theta_range=TAU * 2, color=BLUE).set_opacity(
            0.7
        )
        plane = NumberPlane().set_color(BLUE_A).set_opacity(0.2)
        ax = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1]).set_opacity(0.5)
        self.play(DrawBorderThenFill(VGroup(plane, ax)), run_time=2)
        self.play(Create(rose), run_time=7)
        self.play(Write(text), run_time=3)
        self.wait(3)
