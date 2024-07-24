from manim import *

class Demonstration(Scene):
    def construct(self):
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
