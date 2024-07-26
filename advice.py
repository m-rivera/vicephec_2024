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

class Advice(ThreeDSlide):
    def construct(self):

        sub_font_size = 40
        #Tex.set_default(font="Nimbus Sans")

        top_left = UP*3 + LEFT*7
        bot_left = DOWN*3 + LEFT*7

        def bulleted_list(str_list,buff=0.5):
            text_vgroup = VGroup()
            for i,item in enumerate(str_list):
                text_mobject = Tex(r"· "+item,font_size=sub_font_size).shift(DOWN*i)
                text_vgroup.add(text_mobject)
            text_vgroup.arrange_in_grid(cols=1,col_alignments="l",buff=buff)

            return text_vgroup.move_to(top_left,aligned_edge=LEFT+UP).shift(DOWN+RIGHT)
       # set default font to sans
        #Tex.set_default(font="CMU Sans Serif",color=BLACK)
        #Tex.set_default(color=BLACK)

        #self.camera.background_color = ManimColor(bg_col)

        # title slide

        #demo_text = Tex("3. Demo",font_size=60)
        advice_text = Tex("4. Advice",font_size=60)
        self.next_slide()
        self.play(Write(advice_text))
        self.next_slide()

        stren_text = Tex("Strengths").move_to(top_left,aligned_edge=LEFT)

        self.wipe(advice_text,stren_text)

        self.next_slide()

        strengths = bulleted_list(["Precisely controllable",
            "Well documented",
            "Interoperable with Python code",
            "Attractive-looking defaults"])

        for stren in strengths:
            self.play(Write(stren))
            self.next_slide()

        self.next_slide()
        weak_text = Tex("Weaknesses").move_to(top_left,aligned_edge=LEFT)
        self.wipe(Group(stren_text,strengths),weak_text)

        weaknesses = bulleted_list([
            "Needs Python expertise",
            "Long development time",
            "Involves additional editing",
            "Passive learning experience"])

        for wea in weaknesses:
            self.play(Write(wea))
            self.next_slide()

        self.next_slide()
        rec_text = Tex("Recommendations").move_to(top_left,aligned_edge=LEFT)
        self.wipe(Group(weak_text,weaknesses),rec_text)

        recs = bulleted_list([
            "Re-use as much as possible",
            "Collaborate",
            "Publish your source code",
            "Use in flipped classrooms"])

        for rec in recs:
            self.play(Write(rec))
            self.next_slide()


        self.next_slide()
        quote_text = Tex("Student quotes").move_to(top_left,aligned_edge=LEFT)
        self.wipe(Group(rec_text,recs),quote_text)

        # quotes arising from general questions about the practical
        # (not prompted to mention lecture material)
        quotes= bulleted_list([
            "...videos for this topic were incredibly detailed and well put together...",
            "Visual materials in the videos were exceptionally good.",
            "introductory lectures were very well done",
            "The mini-lectures (youtube videos)...were helpful."
            ])
        self.play(Create(quotes))

        self.wait(0.5)
        self.next_slide()
        ack_text = Tex("Acknowledgments").move_to(top_left,aligned_edge=LEFT)
        self.wipe(Group(quote_text,quotes),ack_text)

        acks = bulleted_list([
            "Manim Community",
            "Michael Ingham",
            "Michael O'Neill"])
        self.play(Create(acks))

        self.wait(0.5)
        self.next_slide()
        shout_out = Tex(r"Python in Chemistry: pythoninchemistry.org",font_size=sub_font_size).move_to(top_left,aligned_edge=LEFT).shift(DOWN*4)
        source = Tex(r"Presentation source code: github.com/m-rivera/vicephec\_2024",font_size=sub_font_size).move_to(top_left,aligned_edge=LEFT).shift(DOWN*5)
        self.play(Write(shout_out),Write(source))

        self.wait(3)
        self.next_slide()
        #self.play(*[FadeOut(mob) for mob in self.mobjects])
