from manim import *


class ComplexExp(ThreeDScene):
    def construct(self):
        # white theme
        self.camera.background_color = "#ece6e2"

        axes = ThreeDAxes(x_range=(-0.1, 4.25), y_range=(-1.5, 1.5),
                          z_range=(-1.5, 1.5), y_length=5, z_length=5, axis_config={"color": BLACK})

        curve = ParametricFunction(
            lambda p: axes.coords_to_point(
                p, np.exp(complex(0, PI*p)).real, np.exp(complex(0, PI*p)).imag),
            t_range=(0, 4, 0.1), color=BLACK
        )
        curve_extension = ParametricFunction(
            lambda p: axes.coords_to_point(
                p, np.exp(complex(0, PI*p)).real, np.exp(complex(0, PI*p)).imag),
            t_range=(2, 4, 0.1), color=BLACK
        )
        t = MathTex("z = e^{t \pi i}, \quad t\in [0, 2]", fill_color=BLACK)
        t.rotate(axis=OUT, angle=90*DEGREES).rotate(axis=UP, angle=90*DEGREES)
        t.next_to(curve, UP + OUT)
        self.set_camera_orientation(
            phi=90*DEGREES, theta=0, focal_distance=10000)
        self.add(axes)
        self.play(Create(curve, run_time=2), Write(t))
        self.wait()
        self.move_camera(phi=75*DEGREES, theta=-30*DEGREES)
        self.wait()
        four = MathTex("4", fill_color=BLACK).rotate(axis=OUT, angle=90 *
                                                     DEGREES).rotate(axis=UP, angle=90*DEGREES)
        four.move_to(t[0][12])
        self.play(Create(curve_extension, run_time=2),
                  t[0][12].animate.become(four))
        self.wait()
        self.move_camera(phi=90*DEGREES, theta=-90 *
                         DEGREES, focal_distance=10000)
        self.wait()
        self.move_camera(phi=75*DEGREES, theta=-30*DEGREES)
        self.wait()
        self.move_camera(phi=0, theta=-90*DEGREES, focal_distance=10000)
        self.wait()
        self.move_camera(phi=75*DEGREES, theta=-30*DEGREES)
        self.wait()
        self.play(FadeOut(axes, curve, curve_extension, t, shift=IN))
        self.wait()


with tempconfig({"quality": "medium_quality", "preview": False}):
    scene = ComplexExp()
    scene.render()
