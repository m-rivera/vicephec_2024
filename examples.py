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

class Examples(ThreeDSlide):
    def construct(self):

        sub_font_size = 40
        #Tex.set_default(font="Nimbus Sans")

        def bulleted_list(str_list,buff=1):
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

        example_text = Tex("2. Examples",font_size=60)
        self.play(Write(example_text))

        self.next_slide()
        vib_text = Tex("Motion").move_to(top_left,aligned_edge=LEFT)
        self.wipe(example_text,vib_text)

        self.next_slide()

        time = ValueTracker(0)
        morse_disp_data = np.loadtxt("morse_disp.dat")

        def morse_disp(time):
            """Morse potential displacement with time in [0,1["""
            len_dat = len(morse_disp_data)
            ind = int(time*len_dat) # round to floor integer to get an index
            return morse_disp_data[ind]

        def displacement(time,pot="harm"):
            """The displacement of the bond under a Harmonic or Morse potential"""
            omega = 1 # angular frequency
            amplitude = 1
            if pot=="harm":
                return amplitude*np.sin(omega*time)
            elif pot=="morse":
                return amplitude*morse_disp((time%(2*PI))/(2*PI))
            else:
                raise("Wrong potential type!")

        def draw_atom(pos):
            return Dot(color=pink,radius=0.3).move_to(pos)

        bond_eq = 2

        pot_type = "harm"

        atom_1 = always_redraw(lambda: draw_atom([-bond_eq/2 - displacement(time.get_value(),pot=pot_type)/2,2,0]))
        atom_2 = always_redraw(lambda: draw_atom([bond_eq/2 + displacement(time.get_value(),pot=pot_type)/2,2,0]))
        bond = always_redraw(lambda: Line(atom_1.get_center(),atom_2.get_center(),stroke_width=20))

        diatomic = VGroup(bond, atom_1, atom_2)

        self.play(Create(diatomic))
        self.next_slide()

        # plot Harmonic
        def harm(x):
            return (x-bond_eq)**2/5

        def morse(x):
            decay_param = 1
            return (1-np.exp(-decay_param*(x-bond_eq)))**2

        def generic_pot(x,pot="harm"):
            if pot=="harm":
                return harm(x)
            elif pot=="morse":
                return morse(x)
            else:
                raise("Wrong potential type!")

        ax = Axes(x_range=[0,2*bond_eq], y_range=[0,1], x_length=bond_eq*2, y_length=3, axis_config={"include_tip": False}).shift(DOWN)
        labels = ax.get_axis_labels(x_label="r",y_label="V(r)")



        harm_plot = ax.plot(harm,x_range=[bond_eq/2-1,3*bond_eq/2+1])

        dot_track = always_redraw(lambda: Dot(color=pink).move_to(ax.c2p(bond_eq + displacement(time.get_value(),pot=pot_type),generic_pot(bond_eq+displacement(time.get_value(),pot=pot_type),pot_type))))

        self.play(Create(ax),Create(labels))
        self.play(Create(harm_plot),Create(dot_track))

        self.next_slide(loop=True)

        self.play(time.animate.set_value(2*PI),rate_func=linear,runt_time=2)

        self.next_slide()

        # plot Morse

        morse_plot = ax.plot(morse,x_range=[bond_eq-0.7,3*bond_eq/2+1])
        self.play(Transform(harm_plot,morse_plot))

        self.next_slide(loop=True)

        pot_type = "morse"
        dot_track = always_redraw(lambda: Dot(color=pink).move_to(ax.c2p(bond_eq + displacement(time.get_value(),pot=pot_type),morse(bond_eq+displacement(time.get_value(),pot=pot_type)))))

        self.play(time.animate.set_value(0),rate_func=linear,runt_time=0)
        self.play(time.animate.set_value(2*PI),rate_func=linear,runt_time=2)

        self.next_slide()

        algo_text = Tex("Algorithms").move_to(top_left,aligned_edge=LEFT)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.play(Write(algo_text))
        self.next_slide()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
