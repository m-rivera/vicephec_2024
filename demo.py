from manim import *

from manim_slides import Slide
from manim_slides import ThreeDSlide
import numpy as np

# colors
teal = "#3E969A"
pink = "#F24680"
yellow = "#FFA34F"
green = "#3C9D00"
brown = "#87402f"
bg_col = "#FFF8E7"
grey = "#8e8e8e"

class Demo(ThreeDSlide):
    def construct(self):

        section_demo = Tex("3. Demonstration",font_size=60)

        code_listing = Code(
                "demo_code.py",
                tab_width=4,
                style=Code.styles_list[13],
                background="window",
                language="Python",
                font="Monospace")

        self.wipe(section_demo,code_listing)

        self.next_slide()

        self.wipe(code_listing,)

        # create a circle
        circle = Circle(color=RED).move_to(UP)
        self.play(Create(circle))
        self.wait()

        # replace it with a square
        square = Square(color=WHITE).move_to(UP)
        self.play(ReplacementTransform(circle,square))
        self.wait()

        # move down and rotate
        self.play(square.animate.move_to(DOWN))
        self.play(Rotate(square, angle=PI))
        self.wait()
        self.play(FadeOut(square))
