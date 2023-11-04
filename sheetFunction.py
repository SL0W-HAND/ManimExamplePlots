from manim import *
import numpy as np


class Sheet(ThreeDScene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#ece6e2"
        # 3d axis scene configurations
        axes_3d = ThreeDAxes(
            x_range=(0, 15),
            y_range=(0, 16),
            z_range=(0, 1.5),
            z_length=3,
            # fill_color=BLACK,
            axis_config={"include_numbers": True}
        )
        axes_3d.set_color(BLACK)

        # Labels
        y_label = axes_3d.get_y_axis_label("y").shift(LEFT*2).shift(UP)
        x_label = axes_3d.get_x_axis_label("x").shift(DOWN*2)
        z_label = axes_3d.get_z_axis_label("z").shift(DOWN*2)

        for i in range(0, 1):
            axes_3d.get_z_axis().numbers[i].rotate(
                axis=RIGHT, angle=180 * DEGREES).rotate(axis=UP, angle=-90 * DEGREES)

        grid_labels = VGroup(x_label, y_label, z_label)
        grid_labels.set_color(BLACK)

        # Math functions
        def heatFunction(x, y):
            return (np.e**(-0.4*y))*(np.sin(x))

        # Math functions to graphs
        resolution_fa = 30

        # Surface sheet
        surface = Surface(
            lambda u, v: axes_3d.c2p(u, v, heatFunction(u, v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=[0, 15],
            u_range=[0, 14],
            stroke_color=GRAY,
        )
        surface.set_style(fill_opacity=0.1)

        color_curves = VGroup(*[
            Surface(
                lambda u, v: axes_3d.c2p(u, y, heatFunction(u, y)),
                resolution=(resolution_fa, resolution_fa),
                u_range=[0, 14],
                v_range=[0, 15],
                stroke_width=5
            ).set_fill_by_value(axes=axes_3d, colorscale=[(RED, -0.5), (GRAY, 0), (BLUE, 0.5)], axis=2)
            for y in range(0, 15, 3)])

        # Elements in scene
        self.add(axes_3d, grid_labels, surface, color_curves)

        # Camara config
        self.set_camera_orientation(
            phi=75*DEGREES,
            theta=-60*DEGREES,
            zoom=0.9,
            focal_distance=10000
        )


with tempconfig({"quality": "medium_quality", "preview": False, "pixel_width": 1920, "pixel_height": 1080}):
    scene = Sheet()
    scene.render()
