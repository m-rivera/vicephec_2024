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

class Background(ThreeDSlide):
    def construct(self):

        sub_font_size = 40
        #Tex.set_default(font="Nimbus Sans")

        def bulleted_list(str_list,buff=0.5):
            text_vgroup = VGroup()
            for i,item in enumerate(str_list):
                text_mobject = Tex(r"· "+item,font_size=sub_font_size).shift(DOWN*i)
                text_vgroup.add(text_mobject)
            text_vgroup.arrange_in_grid(cols=1,col_alignments="l",buff=buff)

            return text_vgroup

        top_left = UP*3 + LEFT*7
        bot_left = DOWN*3 + LEFT*7
        # set default font to sans
        #Tex.set_default(font="CMU Sans Serif",color=BLACK)
        #Tex.set_default(color=BLACK)

        #self.camera.background_color = ManimColor(bg_col)

        # title slide

        self.next_slide()
        title = Tex("Precise Animations for the STEM Classroom",font_size=60)
        self.play(Write(title))

        subtitle = Tex("ViCEPHEC 2024, University of Surrey, Miguel Rivera",font_size=sub_font_size).next_to(title,DOWN)
        self.play(Write(subtitle))

        # TOC
        self.next_slide()

        section_back = Tex("1. Background",font_size=60)
        self.wipe(Group(title,subtitle),section_back)

        self.next_slide()
        # visualisation
        vis_text = Tex("Visualisation skills").move_to(top_left,aligned_edge=LEFT)

        self.wipe(section_back,vis_text)

        self.next_slide()

        fig_height = 1

        text_inte = Tex("Interpretation",font_size=sub_font_size)
        eye = SVGMobject("img/eye.svg",stroke_width=5,height=0.7)
        for obj in eye:
            obj.joint_type=LineJointType.ROUND

        text_intr = Tex("Introspection",font_size=sub_font_size)
        brain = SVGMobject("img/brain.svg",stroke_width=5,height=fig_height)

        text_crea = Tex("Creation",font_size=sub_font_size)
        pencil = SVGMobject("img/pencil.svg",stroke_width=5,height=fig_height)

        skills = VGroup(eye, text_inte, pencil, text_crea, brain, text_intr)

        skills.arrange_in_grid(
                rows=3,
                buff=(0.2,0.5),
                col_alignments="cl",
                row_heights = [1,1,1])
        skills.move_to(LEFT*3)

        self.next_slide()
        self.play(Create(eye))
        self.play(Write(text_inte))
        self.next_slide()
        self.play(Create(pencil))
        self.play(Write(text_crea))
        self.next_slide()
        self.play(Create(brain))
        self.play(Write(text_intr))
        self.next_slide()

        ref_book_vis = Tex(r"J. Gilbert, M. Reiner and M. B. Nakhleh, Eds., \textit{Visualization: theory and practice in science education}, Springer, New York, 2008.",font_size=20).move_to(bot_left,aligned_edge=LEFT)
        self.play(Write(ref_book_vis))
        self.next_slide()

        # pendulum
        time = ValueTracker(0)
        init_angle = 50/180*PI
        anchor_pos = np.array([3,3,0])
        length = 4
        g = 15
        ang_freq = np.sqrt(g/length)
        period = 2*PI/ang_freq

        def get_angle(time):
            return init_angle*np.cos(ang_freq*time)



        def get_ball(pos):
            ball = Dot([pos[0],pos[1],0],fill_color=pink,radius = 0.15,z_index=1)
            return ball

        ball = always_redraw(lambda: get_ball(anchor_pos + np.array([length*np.sin(get_angle(time.get_value())),-length*np.cos(get_angle(time.get_value())),0])))

        anchor = Dot(anchor_pos,fill_color=pink,radius=0.15,z_index=1)

        #rope = always_redraw(lambda: Line(anchor_pos,ball))
        ref_line = DashedLine(start=anchor.get_center(),end=anchor.get_center()+np.array([0,-length,0]))
        rope = Line(anchor.get_center(),ball.get_center(),z_index=0).add_updater(lambda l:l.put_start_and_end_on(anchor.get_center(),ball.get_center()))

        def get_arc(angle):
            '''
            The arc makes the animation bug out on high res
            Not sure why!
            '''
            arc = VectorizedPoint().move_to(10*RIGHT)
            #if angle == 0:
            #    arc = VectorizedPoint().move_to(10*RIGHT)
            if angle>0:
                arc = Angle(rope,ref_line,quadrant=(1,1), other_angle=True)
            elif angle<0:
                arc = Angle(rope,ref_line,quadrant=(1,1), other_angle=False)

            return arc

        #arc = always_redraw(lambda: get_arc(get_angle(time.get_value())))


        self.play(Create(anchor))
        self.play(Create(ball))
        self.play(Create(rope))
        self.play(Create(ref_line))
        #self.play(Create(arc))

        self.next_slide(loop=True)
        self.play(time.animate.set_value(period),rate_func=linear,run_time=2)
        self.next_slide()
        #self.play(angle.animate.set_value(3*PI),rate_func=linear,run_time=3*period)
        triangle_text = Tex("Johnstone's triangle",font_size=sub_font_size+5).move_to(top_left,aligned_edge=LEFT)

        self.wipe(Group(vis_text,eye,text_inte,brain,text_intr,pencil,text_crea,ref_book_vis,anchor,ball,rope,ref_line),triangle_text)

        triangle = Triangle(color=WHITE).scale(1)
        self.play(Create(triangle))
        ref_john = Tex(r"A. H. Johnstone, \textit{J. Chem. Educ.}, 1993, \textbf{70}, 701.",font_size=20).move_to(bot_left,aligned_edge=LEFT)
        self.play(Write(ref_john))


        self.next_slide()

        formula_nacl = Tex("NaCl",font_size=sub_font_size)
        text_symbolic = Tex(r"\textbf{Symbolic}",font_size=sub_font_size).next_to(formula_nacl,UP)

        group_sym = VGroup(formula_nacl,text_symbolic).next_to(triangle,UP)
        self.play(Write(text_symbolic))
        self.play(Write(formula_nacl))

        self.next_slide()

        nacl_structure = SVGMobject("img/rock_salt.svg",stroke_width=3,height=1)
        text_sub = Tex(r"\textbf{Submicroscopic}",font_size=sub_font_size).next_to(nacl_structure,UP)

        group_sub = VGroup(text_sub,nacl_structure).next_to(triangle,DOWN+RIGHT)
        self.play(Write(text_sub))
        self.play(Create(nacl_structure))

        self.next_slide()

        shaker = SVGMobject("img/salt_shaker.svg",stroke_width=3,stroke_color=WHITE,height=1.2)
        text_macro = Tex(r"\textbf{Macroscopic}",font_size=sub_font_size).next_to(shaker,UP)

        group_macro = VGroup(text_macro,shaker).next_to(triangle,DOWN+LEFT)
        self.play(Write(text_macro))
        self.play(Create(shaker))

        self.next_slide()
        self.play(Wiggle(group_sym),Wiggle(group_sub))

        self.next_slide()










        anim_text = Tex("Dynamic visualisation platforms").move_to(top_left,aligned_edge=LEFT)

        self.wipe(Group(triangle,group_sub,group_macro,group_sym,triangle_text,ref_john),anim_text)

        self.next_slide()

        # manim presentation
        alternatives = bulleted_list(["Blender: Great for 3D", "Geogebra: Interactive", "Matplotlib: Programmable","Powerpoint: Widely used", "Using your hands: Cross-platform and renders quickly"], buff=0.5).move_to(top_left,aligned_edge=LEFT+UP).shift(DOWN+RIGHT)
        for alt in alternatives:
            self.play(Write(alt))
            self.next_slide()
        self.wipe(Group(anim_text,alternatives))

        banner = ManimBanner()
        self.play(banner.create())
        self.play(banner.expand())
        self.next_slide()
        self.play(banner.animate.scale(0.3).move_to(top_left,aligned_edge=LEFT))
        self.next_slide()

        man_features = bulleted_list(["Python-driven mathematical animations","Free, open-source", "Created by Grant Sanderson (3Blue1Brown)","Maintained by Manim Community"],buff=0.5).move_to(top_left,aligned_edge=LEFT+UP).shift(DOWN+RIGHT)
        for fea in man_features:
            self.play(Write(fea))
            self.next_slide()

        # fade out all
        self.play(*[FadeOut(mob) for mob in self.mobjects])








