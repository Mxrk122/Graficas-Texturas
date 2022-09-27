import gl
import texture
from vector3 import *
import color
import math

# Elegir el nombre del archivo
filename = 'result.bmp'


nvidia = gl.gl(filename)

nvidia.glCreateWindow(1000, 1000)

nvidia.glClearColor(1, 1, 1)

nvidia.glClear()

# Elegir las escalas del objeto
scale = (50, 50, 50)
translate = (300, 0, 0)
rotate = (0, 0, 0)

# Elegir el color del objeto
object_color = (0,1,1)

# elegir el objeto
object = nvidia.glSetObject("Nutella_Milkshake.obj")

# Elegir la textura del objeto
t = texture.Texture("Nutella-Milkshake.bmp")

# REalizar la pintada del modelo en el archivo
# y añadir la textura al final como parametro
nvidia.glObjectMode(scale, translate, rotate, object_color, t)

# Se escribio en result.bmp
nvidia.glFinish()