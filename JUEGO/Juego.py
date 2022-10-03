"""
Nasa Space App Challenge
Team: Rocket
"""
from ursina import *
import webbrowser
from time import sleep
Juego = Ursina()
camera.orthographic = True
camera.fov = 8
T = J = S = 0
#-------------- LINKS ----------------------
def URL_Jupiter():
    webbrowser.open_new('https://www.nasa.gov/jupiter')
def URL_JWEBB():
    webbrowser.open_new('https://www.nationalgeographicla.com/ciencia/2021/12/se-lanzo-el-telescopio-espacial-james-webb-el-mas-potente-de-la-historia')
def URL_Saturno():
    webbrowser.open_new('https://www.nasa.gov/feature/goddard/2022/new-webb-image-captures-clearest-view-of-neptune-s-rings-in-decades')
#------------- Entidades ----------------------
Logo = Entity(
    model='quad',
    texture='Recursos/LOGO',
    position=(-6, 3,-1),
    scale = (1.5,1.5)
)
Jugador = Entity(
    model='quad',
    texture='Recursos\WEBB',
    z = -1,
    position=(0, 0),
    scale=0.2,
    collider = 'box'
)
map = Entity(
    model = 'quad',
    texture = 'Recursos\Fondo2',
    z = 0,
    scale = (16,9),
    collider = 'box'
    )
Sol = Entity(
    model = 'quad',
    texture = 'Recursos\Sol',
    x = -8,
    y = 0,
    z = -1,
    scale = (2,2),
    collider='box',
)
Mercurio = Entity(
    model = 'quad',
    texture = 'Recursos\Mercurio',
    x = -2,
    y = -3,
    z = -1,
    scale = (0.1,0.1),
    collider = 'box',
)
Venus = Entity(
    model='quad',
    texture='Recursos\Mercurio',
    x = 4,
    y = -3,
    z = -1,
    scale = (0.2, 0.2),
    collider = 'box',
)
Tierra = Entity(
    model = 'quad',
    texture = 'Recursos\Tierra',
    x = -2,
    y = 0,
    z = -1,
    scale = (1,1),
    collider = 'box',
    on_click = URL_JWEBB
)
Marte = Entity(
    model = 'quad',
    texture = 'Recursos\Marte',
    x = 4,
    y = -1,
    z = -1,
    scale = (0.2,0.2),
    collider = 'box',
)
Jupiter = Entity(
    model = 'quad',
    texture = 'Recursos\Jupiter',
    z = -1,
    x = 5,
    y = 2,
    scale = (0.3,0.3),
    collider='box',
    on_click = URL_Jupiter
    )
Saturno = Entity(
    model = 'quad',
    texture = 'Recursos\Saturno',
    z = -1,
    x = 0,
    y = 3,
    scale = (0.2, 0.1),
    collider = 'box',
    on_click = URL_Saturno
    )
Urano = Entity(
    model = 'quad',
    texture = 'Recursos/Urano',
    z = -1,
    x = -3,
    y = 3,
    scale = (0.08, 0.08),
    collider = 'box',
)
Neptuno =  Entity(
    model = 'quad',
    texture = 'Recursos/Neptuno',
    z = -1,
    x = -6,
    y = 3.5,
    scale = (0.04, 0.04),
    collider = 'box',
)
#------- IMG Informativas ----------
def TierraInf():
    TR_INF = Entity(
        model='quad',
        texture='Recursos\TR_INF',
        z=-2,
        x=-1.5,
        y=0.5,
        scale=(0.7, 0.7)
    )
def JupiterInf():
    JP_INF = Entity(
        model = 'quad',
        texture = 'Recursos\JP_INF',
        z=-2,
        x=5.5,
        y=2.5,
        scale=(0.7, 0.7)
    )
def SaturnoInf():
    ST_INF = Entity(
        model='quad',
        texture='Recursos\ST_INF',
        z=-2,
        x=0.5,
        y=3,
        scale=(0.7, 0.7)
    )
#--------Movimientos------------
def update():
    global T, J, S
    const = 0.02
    zoom = 0.06
    #Movimiento JW
    Jugador.x -= held_keys['a'] * const
    Jugador.y -= held_keys['s'] * const
    Jugador.x += held_keys['d'] * const
    Jugador.y += held_keys['w'] * const

    map.x -= held_keys['a'] * const
    map.y -= held_keys['s'] * const
    map.x += held_keys['d'] * const
    map.y += held_keys['w'] * const
    #Limitar zoom
    if camera.fov <= 8:
        camera.fov += held_keys['-'] * zoom
        camera.fov -= held_keys['+'] * zoom
    else:
        camera.fov -= held_keys['+'] * zoom
    #Movimiento Camara
    camera.x -= held_keys['a'] * const
    camera.y -= held_keys['s'] * const
    camera.x += held_keys['d'] * const
    camera.y += held_keys['w'] * const
    #Fijar Logo
    Logo.x -= held_keys['a'] * const
    Logo.y -= held_keys['s'] * const
    Logo.x += held_keys['d'] * const
    Logo.y += held_keys['w'] * const
    #Si se tocan los objetos.
    if (Jugador.intersects(Saturno).hit and S == 0):
        SaturnoInf()
        S = 1
    if (Jugador.intersects(Tierra).hit and T == 0):
        TierraInf()
        T = 1
    if (Jugador.intersects(Jupiter).hit and J == 0):
        JupiterInf()
        J = 1
Juego.run()