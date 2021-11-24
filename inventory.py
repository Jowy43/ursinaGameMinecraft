from ursina import *


class Hud(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent=camera.ui,
            model=Quad(radius=.015),
            texture='white_cube',
            texture_scale=(4, 1),
            scale=(.4, .1),
            origin=(0, 4.3),
            color=color.color(0, 0, .1, .9),
        )


class Item(Entity):
    def __init__(self,texture):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(0.09, 0.09),
            position=(-.151, 0),
            origin=(0, 4.8),
            texture=texture
        )


class Inventory(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent=camera.ui,
            model=Quad(radius=.015),
            texture='white_cube',
            texture_scale=(6, 4),
            scale=(.6, .4),
            origin=(0, 0),
            color=color.color(0, 0, .1, .9)
        )
