from manim import *

from manim_slides import Slide
from manim_slides import ThreeDSlide
import numpy as np


# colors
teal = ManimColor("#3E969A")
l_teal = ManimColor("#64e8ef")
pink = ManimColor("#F24680")
yellow = ManimColor("#FFA34F")
l_yellow = ManimColor("#fcbc80")
green = ManimColor("#3C9D00")
brown = ManimColor("#87402f")
black = ManimColor("#000000")
bg_col = black
grey = ManimColor("#8e8e8e")


class PES(ThreeDSlide):
    def construct(self):
        self.next_slide()
        resolution_fa = 32
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES,zoom = 0.3)

        shift = 0.3
        range_func = np.array([0.748,1.4]) + shift
        sigma = 0.75 + shift
        epsilon = 3.02
        r_min = np.power(2,1/6)*sigma

        def lj_pot_2d(x,y):
            """Lennard-Jones potential with two coordinates"""
            power_6_1 = np.power(sigma/x,6)
            power_6_2 = np.power(sigma/y,6)
            z = 4 * epsilon * (power_6_1 * (power_6_1 - 1) + power_6_2 * (power_6_2 - 1))+2*epsilon
            return z

        max_point = lj_pot_2d(range_func[1],range_func[1])
        min_point = lj_pot_2d(r_min,r_min)
        mid_point = -(max_point-min_point)/2

        axes = ThreeDAxes(
                x_range = range_func,
                y_range = range_func,
                z_range = [min_point, lj_pot_2d(range_func[0],range_func[0])]
        )
        label_scale = 1
        lab_x = axes.get_x_axis_label(Tex("$r_{12}$"),buff=0.2).scale(label_scale)
        lab_y = axes.get_y_axis_label(Tex("$r_{23}$"),buff=0.2).scale(label_scale)
        lab_z = Tex("$E$").move_to(axes.c2p(range_func[0],range_func[0],max_point+3)).scale(label_scale)

        self.add_fixed_orientation_mobjects(lab_x,lab_y,lab_z)

        #self.begin_ambient_camera_rotation(rate=0.12)

        self.play(Create(lab_x),Create(lab_y),Create(lab_z))

        lj_plane = Surface(
            lambda u, v: axes.c2p(u, v, lj_pot_2d(u,v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=np.array(range_func),
            u_range=range_func,
        )

        lj_plane.set_style(fill_opacity=.8)
        #lj_plane.set_fill_by_value(axes = axes, colors = [(pink, lj_pot_2d(r_min,r_min)),(teal, lj_pot_2d(range_func[0]-0.3,range_func[0]-0.3))])

        lj_plane.set_fill_by_value(axes = axes, colors = [(pink, min_point),(yellow,max_point)])

        self.play(FadeIn(lj_plane),Create(axes))
        self.next_slide()

        self.move_camera(phi=45 * DEGREES, theta=90 * DEGREES,zoom = 0.3)
        self.next_slide()

        self.next_slide()

        def cool_sphere(x,y):
            return Sphere(center=axes.c2p(x,y,lj_pot_2d(x,y)),radius=0.5,resolution=(20,20)).set_color(teal)
            #return Sphere(center=axes.c2p(x,y,lj_pot_2d(x,y)),radius=0.5).set_color(teal)

        def normalise(x):
            """Return the value scaled within the range of the function definition"""
            return  range_func[0] + x*(range_func[1]-range_func[0])

        def un_normalise(x):
            """Return the value scaled within the range of 0 and 1"""
            return  (x-range_func[0])/(range_func[1]-range_func[0])


        x_vt = ValueTracker(normalise(0.6))
        y_vt = ValueTracker(normalise(0.8))
        ball = always_redraw(lambda:cool_sphere(x_vt.get_value(),y_vt.get_value()))

        self.play(FadeIn(ball))
        def atom(pos):
            return Dot(pos, radius=0.5, color=teal)

        atom_1 = always_redraw(lambda:atom(DOWN*2.5+(un_normalise(x_vt.get_value())+un_normalise(y_vt.get_value()))/2*8*LEFT))
        atom_2 = always_redraw(lambda:atom(DOWN*2.5+(un_normalise(x_vt.get_value())-un_normalise(y_vt.get_value()))/2*8*LEFT))
        atom_3 = always_redraw(lambda:atom(DOWN*2.5+(un_normalise(x_vt.get_value())+un_normalise(y_vt.get_value()))/2*8*RIGHT))

        lab_1 = always_redraw(lambda:Tex(r"$\mathbf{r}_1$").move_to(atom_1))
        lab_2 = always_redraw(lambda:Tex(r"$\mathbf{r}_2$").move_to(atom_2))
        lab_3 = always_redraw(lambda:Tex(r"$\mathbf{r}_3$").move_to(atom_3))

        line_12 = always_redraw(lambda:Line(atom_1.get_center(), atom_2.get_center()))
        line_23 = always_redraw(lambda:Line(atom_2.get_center(), atom_3.get_center()))

        r_12_lab = always_redraw(lambda:Tex("$r_{12}$").next_to(line_12,2*UP))
        r_23_lab = always_redraw(lambda:Tex("$r_{23}$").next_to(line_23,2*DOWN))

        self.add_fixed_orientation_mobjects(line_12,line_23,atom_1,atom_2,atom_3,r_12_lab,r_23_lab,lab_1,lab_2,lab_3)
        self.add_fixed_in_frame_mobjects(line_12,line_23,atom_1,atom_2,atom_3,r_12_lab,r_23_lab,lab_1,lab_2,lab_3)
        self.play(Create(line_12),Create(line_23),Create(atom_1),Create(atom_2),Create(atom_3),Create(r_12_lab),Create(r_23_lab),Create(lab_1),Create(lab_2),Create(lab_3))


        self.next_slide()
        self.move_camera(phi=45 * DEGREES, theta=80 * DEGREES,zoom = 0.3)
        self.play(x_vt.animate.set_value(normalise(0.7)),y_vt.animate.set_value(normalise(0.9)))
        self.next_slide()
        self.move_camera(phi=45 * DEGREES, theta=50 * DEGREES,zoom = 0.3)
        self.play(x_vt.animate.set_value(normalise(0.1)),y_vt.animate.set_value(normalise(0.6)))
        self.next_slide()
        self.move_camera(phi=45 * DEGREES, theta=40 * DEGREES,zoom = 0.3)
        self.play(x_vt.animate.set_value(normalise(0.05)),y_vt.animate.set_value(normalise(0.05)))
        self.next_slide()
        self.move_camera(phi=45 * DEGREES, theta=30 * DEGREES,zoom = 0.3)
        self.play(x_vt.animate.set_value(r_min),y_vt.animate.set_value(r_min))
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.next_slide()
