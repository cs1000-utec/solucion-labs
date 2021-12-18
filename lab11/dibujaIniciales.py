from ursina import *

app = Ursina()

camera.orthographic = True

#letra R
Entity(model='cube', color=color.blue, position=(-12,2,0), texture='auto')
Entity(model='cube', color=color.blue, position=(-12,3,0), texture='auto')
Entity(model='cube', color=color.blue, position=(-12,4,0), texture='auto')
Entity(model='cube', color=color.blue, position=(-12,5,0), texture='auto')
Entity(model='cube', color=color.blue, position=(-12,6,0), texture='auto')

Entity(model='cube', color=color.blue, position=(-11,6,0), texture='auto')
Entity(model='cube', color=color.blue, position=(-10,6,0), texture='auto')

Entity(model='cube', color=color.blue, position=(-9,5,0), texture='auto')

Entity(model='cube', color=color.blue, position=(-10,4,0), texture='auto')
Entity(model='cube', color=color.blue, position=(-11,4,0), texture='auto')

Entity(model='cube', color=color.blue, position=(-10,3,0), texture='auto')
Entity(model='cube', color=color.blue, position=(-9,2,0), texture='auto')


#letra S
Entity(model='cube', color=color.red, position=(-7,2,0), texture='brick')
Entity(model='cube', color=color.red, position=(-6,2,0), texture='brick')
Entity(model='cube', color=color.red, position=(-5,2,0), texture='brick')

Entity(model='cube', color=color.red, position=(-4,3,0), texture='brick')

Entity(model='cube', color=color.red, position=(-5,4,0), texture='brick')
Entity(model='cube', color=color.red, position=(-5,4,0), texture='brick')

Entity(model='cube', color=color.red, position=(-7,5,0), texture='brick')

Entity(model='cube', color=color.red, position=(-6,6,0), texture='brick')
Entity(model='cube', color=color.red, position=(-5,6,0), texture='brick')
Entity(model='cube', color=color.red, position=(-4,6,0), texture='brick')


#letra T
Entity(model='cube', color=color.green, position=(-1,2,0), texture='grass')
Entity(model='cube', color=color.green, position=(-1,3,0), texture='grass')
Entity(model='cube', color=color.green, position=(-1,4,0), texture='grass')
Entity(model='cube', color=color.green, position=(-1,5,0), texture='grass')

Entity(model='cube', color=color.green, position=(0,6,0), texture='grass')
Entity(model='cube', color=color.green, position=(-1,6,0), texture='grass')
Entity(model='cube', color=color.green, position=(-2,6,0), texture='grass')


#letra M
Entity(model='cube', color=color.orange, position=(2,2,0), texture='circle')
Entity(model='cube', color=color.orange, position=(2,3,0), texture='circle')
Entity(model='cube', color=color.orange, position=(2,4,0), texture='circle')
Entity(model='cube', color=color.orange, position=(2,5,0), texture='circle')
Entity(model='cube', color=color.orange, position=(2,6,0), texture='circle')

Entity(model='cube', color=color.orange, position=(3,5,0), texture='circle')

Entity(model='cube', color=color.orange, position=(4,4,0), texture='circle')

Entity(model='cube', color=color.orange, position=(5,5,0), texture='circle')

Entity(model='cube', color=color.orange, position=(6,2,0), texture='circle')
Entity(model='cube', color=color.orange, position=(6,3,0), texture='circle')
Entity(model='cube', color=color.orange, position=(6,4,0), texture='circle')
Entity(model='cube', color=color.orange, position=(6,5,0), texture='circle')
Entity(model='cube', color=color.orange, position=(6,6,0), texture='circle')

EditorCamera()

app.run()