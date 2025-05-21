import pygame
import math
import numpy as np
from pygame.locals import *

# Inicializar Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cubo 3D en Pygame")
clock = pygame.time.Clock()

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Definir los vértices del cubo (coordenadas 3D)
vertices = [
    [-1, -1, -1],  # 0
    [1, -1, -1],   # 1
    [1, 1, -1],    # 2
    [-1, 1, -1],   # 3
    [-1, -1, 1],   # 4
    [1, -1, 1],    # 5
    [1, 1, 1],     # 6
    [-1, 1, 1]     # 7
]

# Definir las aristas (conexiones entre vértices)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Cara trasera
    (4, 5), (5, 6), (6, 7), (7, 4),  # Cara frontal
    (0, 4), (1, 5), (2, 6), (3, 7)   # Conexiones
]

# Colores para cada arista
edge_colors = [RED, GREEN, BLUE, WHITE, RED, GREEN, BLUE, WHITE, 
               RED, GREEN, BLUE, WHITE]

# Parámetros 3D
scale = 100  # Escala para visualización
angle_x, angle_y, angle_z = 0, 0, 0  # Ángulos de rotación

# Función para proyectar 3D a 2D
def project_point(point, angle_x, angle_y, angle_z):
    # Rotación en X
    x, y, z = point
    cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
    y = y * cos_x - z * sin_x
    z = y * sin_x + z * cos_x
    
    # Rotación en Y
    cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
    x = x * cos_y + z * sin_y
    z = -x * sin_y + z * cos_y
    
    # Rotación en Z
    cos_z, sin_z = math.cos(angle_z), math.sin(angle_z)
    x = x * cos_z - y * sin_z
    y = x * sin_z + y * cos_z
    
    # Proyección perspectiva
    distance = 5  # Distancia de la cámara
    factor = distance / (distance + z)
    x_proj = x * factor * scale + width // 2
    y_proj = -y * factor * scale + height // 2
    
    return (x_proj, y_proj)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    # Limpiar pantalla
    screen.fill(BLACK)
    
    # Rotación automática
    angle_x += 0.01
    angle_y += 0.01
    angle_z += 0.005
    
    # Dibujar el cubo
    for i, edge in enumerate(edges):
        start = vertices[edge[0]]
        end = vertices[edge[1]]
        
        start_proj = project_point(start, angle_x, angle_y, angle_z)
        end_proj = project_point(end, angle_x, angle_y, angle_z)
        
        pygame.draw.line(screen, edge_colors[i], start_proj, end_proj, 2)
    
    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)

pygame.quit()