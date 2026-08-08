#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
  EXPLORACAO ESPACIAL 3D  (SEM DEPENDENCIA DE NOISE)
  Um jogo de exploracao espacial com multiplos sistemas estelares
  Controles angulares: WS (angulo X), A/D (angulo Y)
  O = ligar motores, P =/ desligar motores
================================================================================
"""

import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import glm
import numpy as np
import math
import random
import time
import sys

# ================================================================================
# RUIDO PROCEDURAL PROPRIETARIO (sem dependencia externa)
# ================================================================================

def hash3(x, y, z):
    """Funcao de hash 3D simples para gerar ruido procedural."""
    n = int(x * 374761393) + int(y * 668265263) + int(z * 1274126177)
    n = (n ^ (n >> 13)) * 1274126177
    n = n ^ (n >> 16)
    return (n & 0x7fffffff) / 0x7fffffff

def hash3_smooth(x, y, z):
    """Hash com interpolação suave."""
    ix, iy, iz = int(math.floor(x)), int(math.floor(y)), int(math.floor(z))
    fx, fy, fz = x - ix, y - iy, z - iz

    # Interpolacao suave (smoothstep)
    fx = fx * fx * (3.0 - 2.0 * fx)
    fy = fy * fy * (3.0 - 2.0 * fy)
    fz = fz * fz * (3.0 - 2.0 * fz)

    def h(i, j, k):
        return hash3(ix + i, iy + j, iz + k)

    # Trilinear interpolation
    v000 = h(0, 0, 0)
    v100 = h(1, 0, 0)
    v010 = h(0, 1, 0)
    v110 = h(1, 1, 0)
    v001 = h(0, 0, 1)
    v101 = h(1, 0, 1)
    v011 = h(0, 1, 1)
    v111 = h(1, 1, 1)

    v00 = v000 * (1 - fx) + v100 * fx
    v10 = v010 * (1 - fx) + v110 * fx
    v01 = v001 * (1 - fx) + v101 * fx
    v11 = v011 * (1 - fx) + v111 * fx

    v0 = v00 * (1 - fy) + v10 * fy
    v1 = v01 * (1 - fy) + v11 * fy

    return v0 * (1 - fz) + v1 * fz

def fbm3(x, y, z, octaves=4, persistence=0.5, lacunarity=2.0, seed=0):
    """Fractal Brownian Motion 3D."""
    value = 0.0
    amplitude = 1.0
    frequency = 1.0
    max_value = 0.0

    sx, sy, sz = x + seed * 100, y + seed * 100, z + seed * 100

    for _ in range(octaves):
        value += amplitude * hash3_smooth(sx * frequency, sy * frequency, sz * frequency)
        max_value += amplitude
        amplitude *= persistence
        frequency *= lacunarity

    return value / max_value

def fbm2(x, y, octaves=4, persistence=0.5, lacunarity=2.0, seed=0):
    """Fractal Brownian Motion 2D."""
    value = 0.0
    amplitude = 1.0
    frequency = 1.0
    max_value = 0.0

    sx, sy = x + seed * 100, y + seed * 100

    for _ in range(octaves):
        value += amplitude * hash3_smooth(sx * frequency, sy * frequency, 0.0)
        max_value += amplitude
        amplitude *= persistence
        frequency *= lacunarity

    return value / max_value

# ================================================================================
# SHADERS GLSL (como strings, como solicitado)
# ================================================================================

VERTEX_SHADER = """
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aNormal;
layout (location = 2) in vec3 aColor;

out vec3 FragPos;
out vec3 Normal;
out vec3 Color;
out vec3 LightPos;
out float DistanceFromStar;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;
uniform vec3 lightPos;
uniform float distanceFromStar;

void main() {
    FragPos = vec3(model * vec4(aPos, 1.0));
    Normal = mat3(transpose(inverse(model))) * aNormal;
    Color = aColor;
    LightPos = lightPos;
    DistanceFromStar = distanceFromStar;
    gl_Position = projection * view * vec4(FragPos, 1.0);
}
"""

FRAGMENT_SHADER = """
#version 330 core
in vec3 FragPos;
in vec3 Normal;
in vec3 Color;
in vec3 LightPos;
in float DistanceFromStar;

out vec4 FragColor;

void main() {
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(LightPos - FragPos);

    float diff = max(dot(norm, lightDir), 0.0);

    vec3 viewDir = normalize(-FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32.0);

    float attenuation = 1.0 / (1.0 + 0.001 * DistanceFromStar + 0.00001 * DistanceFromStar * DistanceFromStar);

    vec3 ambient = 0.15 * Color;
    vec3 diffuse = diff * Color * attenuation;
    vec3 specular = vec3(0.3) * spec * attenuation;

    vec3 result = ambient + diffuse + specular;
    FragColor = vec4(result, 1.0);
}
"""

STAR_VERTEX_SHADER = """
#version 330 core
layout (location = 0) in vec3 aPos;
layout (location = 1) in vec3 aNormal;
layout (location = 2) in vec3 aColor;

out vec3 Color;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main() {
    Color = aColor;
    gl_Position = projection * view * model * vec4(aPos, 1.0);
}
"""

STAR_FRAGMENT_SHADER = """
#version 330 core
in vec3 Color;
out vec4 FragColor;

void main() {
    FragColor = vec4(Color, 1.0);
}
"""

ORBIT_VERTEX_SHADER = """
#version 330 core
layout (location = 0) in vec3 aPos;

uniform mat4 mvp;

void main() {
    gl_Position = mvp * vec4(aPos, 1.0);
}
"""

ORBIT_FRAGMENT_SHADER = """
#version 330 core
out vec4 FragColor;

void main() {
    FragColor = vec4(0.3, 0.5, 0.7, 0.3);
}
"""

SKY_VERTEX_SHADER = """
#version 330 core
layout (location = 0) in vec3 aPos;

out vec3 TexCoord;

uniform mat4 projection;
uniform mat4 view;

void main() {
    TexCoord = aPos;
    vec4 pos = projection * view * vec4(aPos, 1.0);
    gl_Position = pos.xyww;
}
"""

SKY_FRAGMENT_SHADER = """
#version 330 core
in vec3 TexCoord;
out vec4 FragColor;

void main() {
    float star = 0.0;
    vec3 p = TexCoord * 50.0;
    float n = fract(sin(dot(floor(p.xz), vec2(12.9898, 78.233))) * 43758.5453);
    if (n > 0.998) {
        star = 1.0;
    }
    vec3 color = vec3(0.001, 0.002, 0.005) + vec3(star);
    FragColor = vec4(color, 1.0);
}
"""

# ================================================================================
# FUNCOES DE GERACAO DE GEOMETRIA
# ================================================================================

def create_sphere(radius, segments, rings, color_func=None, displacement=0.0, seed=0):
    vertices = []
    indices = []

    random.seed(seed)

    for i in range(rings + 1):
        phi = math.pi * i / rings
        for j in range(segments + 1):
            theta = 2.0 * math.pi * j / segments

            x = math.sin(phi) * math.cos(theta)
            y = math.cos(phi)
            z = math.sin(phi) * math.sin(theta)

            if displacement > 0:
                disp = fbm3(
                    x * 2.5 + seed * 10,
                    y * 2.5 + seed * 10,
                    z * 2.5 + seed * 10,
                    octaves=4,
                    persistence=0.5,
                    lacunarity=2.0
                ) * displacement
                r = radius + disp
            else:
                r = radius

            px = x * r
            py = y * r
            pz = z * r

            nx = x
            ny = y
            nz = z

            if color_func:
                cx, cy, cz = color_func(x, y, z, phi, theta)
            else:
                cx, cy, cz = 0.5, 0.5, 0.5

            vertices.extend([px, py, pz, nx, ny, nz, cx, cy, cz])

    for i in range(rings):
        for j in range(segments):
            a = i * (segments + 1) + j
            b = a + segments + 1

            indices.extend([a, b, a + 1])
            indices.extend([b, b + 1, a + 1])

    return np.array(vertices, dtype=np.float32), np.array(indices, dtype=np.uint32)


def create_skybox():
    vertices = np.array([
        -1,  1, -1,  -1, -1, -1,   1, -1, -1,   1, -1, -1,   1,  1, -1,  -1,  1, -1,
        -1, -1,  1,  -1, -1, -1,  -1,  1, -1,  -1,  1, -1,  -1,  1,  1,  -1, -1,  1,
         1, -1, -1,   1, -1,  1,   1,  1,  1,   1,  1,  1,   1,  1, -1,   1, -1, -1,
        -1, -1,  1,  -1,  1,  1,   1,  1,  1,   1,  1,  1,   1, -1,  1,  -1, -1,  1,
        -1,  1, -1,   1,  1, -1,   1,  1,  1,   1,  1,  1,  -1,  1,  1,  -1,  1, -1,
        -1, -1, -1,  -1, -1,  1,   1, -1, -1,   1, -1, -1,  -1, -1,  1,   1, -1,  1
    ], dtype=np.float32)
    return vertices


def create_orbit_ring(radius, segments=64):
    vertices = []
    for i in range(segments + 1):
        theta = 2.0 * math.pi * i / segments
        x = radius * math.cos(theta)
        z = radius * math.sin(theta)
        y = 0.0
        vertices.extend([x, y, z])
    return np.array(vertices, dtype=np.float32)


# ================================================================================
# CLASSES DOS ASTROS
# ================================================================================

class CelestialBody:
    def __init__(self, name, radius, position, color,
                 orbit_radius=0, orbit_speed=0, orbit_tilt=0,
                 rotation_speed=0, seed=0, displacement=0.0):
        self.name = name
        self.radius = radius
        self.position = glm.vec3(position)
        self.base_position = glm.vec3(position)
        self.color = color
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.orbit_tilt = orbit_tilt
        self.rotation_speed = rotation_speed
        self.seed = seed
        self.displacement = displacement
        self.orbit_angle = random.random() * 2 * math.pi
        self.rotation_angle = 0.0
        self.vao = None
        self.vbo = None
        self.ebo = None
        self.index_count = 0
        self.orbit_vao = None
        self.orbit_vbo = None
        self.orbit_segments = 64

    def generate_mesh(self, color_func=None):
        verts, idx = create_sphere(
            self.radius, 32, 32,
            color_func=color_func,
            displacement=self.displacement,
            seed=self.seed
        )
        self.index_count = len(idx)

        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)
        self.ebo = glGenBuffers(1)

        glBindVertexArray(self.vao)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, verts.nbytes, verts, GL_STATIC_DRAW)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, idx.nbytes, idx, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 9 * 4, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 9 * 4, ctypes.c_void_p(3 * 4))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 9 * 4, ctypes.c_void_p(6 * 4))
        glEnableVertexAttribArray(2)

        glBindVertexArray(0)

    def generate_orbit(self):
        if self.orbit_radius > 0:
            orbit_verts = create_orbit_ring(self.orbit_radius, self.orbit_segments)

            self.orbit_vao = glGenVertexArrays(1)
            self.orbit_vbo = glGenBuffers(1)

            glBindVertexArray(self.orbit_vao)
            glBindBuffer(GL_ARRAY_BUFFER, self.orbit_vbo)
            glBufferData(GL_ARRAY_BUFFER, orbit_verts.nbytes, orbit_verts, GL_STATIC_DRAW)
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, ctypes.c_void_p(0))
            glEnableVertexAttribArray(0)
            glBindVertexArray(0)

    def update(self, dt, parent_pos=None):
        self.rotation_angle += self.rotation_speed * dt

        if self.orbit_radius > 0 and parent_pos is not None:
            self.orbit_angle += self.orbit_speed * dt

            x = self.orbit_radius * math.cos(self.orbit_angle)
            z = self.orbit_radius * math.sin(self.orbit_angle)
            y = z * math.sin(self.orbit_tilt)
            z = z * math.cos(self.orbit_tilt)

            self.position = parent_pos + glm.vec3(x, y, z)

    def draw(self, shader, view, projection, light_pos, distance_from_star):
        if self.vao is None:
            return

        model = glm.mat4(1.0)
        model = glm.translate(model, self.position)
        model = glm.rotate(model, self.rotation_angle, glm.vec3(0, 1, 0))

        glUniformMatrix4fv(glGetUniformLocation(shader, "model"), 1, GL_FALSE, glm.value_ptr(model))
        glUniformMatrix4fv(glGetUniformLocation(shader, "view"), 1, GL_FALSE, glm.value_ptr(view))
        glUniformMatrix4fv(glGetUniformLocation(shader, "projection"), 1, GL_FALSE, glm.value_ptr(projection))
        glUniform3f(glGetUniformLocation(shader, "lightPos"), light_pos.x, light_pos.y, light_pos.z)
        glUniform1f(glGetUniformLocation(shader, "distanceFromStar"), distance_from_star)

        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, self.index_count, GL_UNSIGNED_INT, None)
        glBindVertexArray(0)

    def draw_orbit(self, orbit_shader, mvp):
        if self.orbit_vao is None:
            return
        glUniformMatrix4fv(glGetUniformLocation(orbit_shader, "mvp"), 1, GL_FALSE, glm.value_ptr(mvp))
        glBindVertexArray(self.orbit_vao)
        glDrawArrays(GL_LINE_STRIP, 0, self.orbit_segments + 1)
        glBindVertexArray(0)


class Star(CelestialBody):
    def __init__(self, name, radius, position, color, seed=0):
        super().__init__(name, radius, position, color, seed=seed)
        self.pulse = 0.0
        self.pulse_speed = random.uniform(0.5, 2.0)

    def generate_mesh(self):
        def star_color(x, y, z, phi, theta):
            r = self.color[0] + fbm3(x*3, y*3, z*3, octaves=2, seed=self.seed) * 0.1
            g = self.color[1] + fbm3(x*3+10, y*3+10, z*3+10, octaves=2, seed=self.seed) * 0.1
            b = self.color[2] + fbm3(x*3+20, y*3+20, z*3+20, octaves=2, seed=self.seed) * 0.1
            return max(0, min(1, r)), max(0, min(1, g)), max(0, min(1, b))
        super().generate_mesh(color_func=star_color)

    def update(self, dt, parent_pos=None):
        self.pulse += self.pulse_speed * dt
        self.rotation_angle += 0.1 * dt

    def draw(self, shader, view, projection):
        if self.vao is None:
            return

        pulse_scale = 1.0 + math.sin(self.pulse) * 0.02

        model = glm.mat4(1.0)
        model = glm.translate(model, self.position)
        model = glm.scale(model, glm.vec3(pulse_scale))
        model = glm.rotate(model, self.rotation_angle, glm.vec3(0, 1, 0))

        glUniformMatrix4fv(glGetUniformLocation(shader, "model"), 1, GL_FALSE, glm.value_ptr(model))
        glUniformMatrix4fv(glGetUniformLocation(shader, "view"), 1, GL_FALSE, glm.value_ptr(view))
        glUniformMatrix4fv(glGetUniformLocation(shader, "projection"), 1, GL_FALSE, glm.value_ptr(projection))

        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, self.index_count, GL_UNSIGNED_INT, None)
        glBindVertexArray(0)


class Planet(CelestialBody):
    def __init__(self, name, radius, orbit_radius, orbit_speed,
                 color_type="earth", orbit_tilt=0, rotation_speed=0.5,
                 seed=0, displacement=0.05, has_rings=False):
        self.color_type = color_type
        self.has_rings = has_rings
        super().__init__(
            name, radius, (0, 0, 0), (0.5, 0.5, 0.5),
            orbit_radius=orbit_radius, orbit_speed=orbit_speed,
            orbit_tilt=orbit_tilt, rotation_speed=rotation_speed,
            seed=seed, displacement=displacement
        )
        self.satellites = []

    def generate_mesh(self):
        def planet_color(x, y, z, phi, theta):
            if self.color_type == "earth":
                n = fbm3(x*2, y*2, z*2, octaves=3, persistence=0.5, seed=self.seed)
                if n > 0.2:
                    return 0.2, 0.6 + n*0.2, 0.2
                elif n > 0.0:
                    return 0.8, 0.7, 0.5
                else:
                    return 0.1, 0.3, 0.6 + abs(n)*0.3
            elif self.color_type == "mars":
                n = fbm3(x*3, y*3, z*3, octaves=4, seed=self.seed)
                r = 0.7 + n * 0.2
                g = 0.2 + n * 0.1
                b = 0.1
                return r, g, b
            elif self.color_type == "gas_giant":
                band = math.sin(phi * 8 + fbm3(x, y*3, z, octaves=2, seed=self.seed)*2)
                if band > 0.3:
                    return 0.8, 0.6, 0.3
                elif band > 0:
                    return 0.6, 0.4, 0.2
                else:
                    return 0.5, 0.3, 0.15
            elif self.color_type == "ice":
                n = fbm3(x*2, y*2, z*2, octaves=3, seed=self.seed)
                return 0.7 + n*0.2, 0.8 + n*0.2, 0.9
            elif self.color_type == "volcanic":
                n = fbm3(x*4, y*4, z*4, octaves=5, seed=self.seed)
                if n > 0.5:
                    return 1.0, 0.3, 0.1
                else:
                    return 0.2, 0.1, 0.1
            elif self.color_type == "desert":
                n = fbm3(x*2, y*2, z*2, octaves=3, seed=self.seed)
                return 0.8, 0.6 + n*0.2, 0.3
            else:
                return 0.5, 0.5, 0.5

        super().generate_mesh(color_func=planet_color)
        self.generate_orbit()

    def add_satellite(self, satellite):
        self.satellites.append(satellite)

    def update(self, dt, star_pos):
        super().update(dt, star_pos)
        for sat in self.satellites:
            sat.update(dt, self.position)

    def draw(self, shader, view, projection, light_pos):
        dist = glm.distance(self.position, light_pos)
        super().draw(shader, view, projection, light_pos, dist)
        for sat in self.satellites:
            sat.draw(shader, view, projection, light_pos, dist)

    def draw_orbits(self, orbit_shader, view, projection, star_pos):
        if self.orbit_vao:
            model = glm.mat4(1.0)
            model = glm.translate(model, star_pos)
            mvp = projection * view * model
            self.draw_orbit(orbit_shader, mvp)
        for sat in self.satellites:
            if sat.orbit_vao:
                model = glm.mat4(1.0)
                model = glm.translate(model, self.position)
                mvp = projection * view * model
                sat.draw_orbit(orbit_shader, mvp)


class Satellite(CelestialBody):
    def __init__(self, name, radius, orbit_radius, orbit_speed,
                 color_type="moon", seed=0, displacement=0.02):
        self.color_type = color_type
        super().__init__(
            name, radius, (0, 0, 0), (0.5, 0.5, 0.5),
            orbit_radius=orbit_radius, orbit_speed=orbit_speed,
            rotation_speed=orbit_speed, seed=seed, displacement=displacement
        )

    def generate_mesh(self):
        def moon_color(x, y, z, phi, theta):
            n = fbm3(x*3, y*3, z*3, octaves=4, seed=self.seed)
            if self.color_type == "moon":
                gray = 0.5 + n * 0.3
                return gray, gray, gray + 0.05
            elif self.color_type == "icy_moon":
                return 0.7 + n*0.2, 0.8 + n*0.2, 0.9
            elif self.color_type == "volcanic_moon":
                if n > 0.6:
                    return 1.0, 0.4, 0.1
                return 0.3, 0.2, 0.2
            else:
                return 0.5, 0.5, 0.5

        super().generate_mesh(color_func=moon_color)
        self.generate_orbit()


# ================================================================================
# SISTEMA ESTELAR
# ================================================================================

class StarSystem:
    def __init__(self, name, position, seed=0):
        self.name = name
        self.position = glm.vec3(position)
        self.seed = seed
        random.seed(seed)

        self.star = None
        self.planets = []
        self.generate_system()

    def generate_system(self):
        random.seed(self.seed)

        star_types = [
            ("Sol Amarelo", 3.0, (1.0, 0.9, 0.5)),
            ("Gigante Vermelha", 5.0, (1.0, 0.4, 0.2)),
            ("Ana Branca", 1.5, (0.9, 0.95, 1.0)),
            ("Estrela Azul", 4.0, (0.5, 0.7, 1.0)),
            ("Estrela Laranja", 2.5, (1.0, 0.7, 0.3)),
        ]
        star_type = random.choice(star_types)
        self.star = Star(
            star_type[0], star_type[1], self.position, star_type[2], seed=self.seed
        )
        self.star.generate_mesh()

        num_planets = random.randint(3, 7)
        for i in range(num_planets):
            planet_seed = self.seed + i * 100
            random.seed(planet_seed)

            orbit_radius = 15 + i * 12 + random.uniform(-3, 3)
            orbit_speed = random.uniform(0.1, 0.4) / (orbit_radius * 0.1)
            orbit_tilt = random.uniform(-0.3, 0.3)
            radius = random.uniform(0.8, 2.5)
            rotation_speed = random.uniform(0.2, 1.0)

            if i == 0:
                ptype = random.choice(["volcanic", "desert"])
                disp = 0.08
            elif i < 3:
                ptype = random.choice(["earth", "mars", "desert"])
                disp = 0.05
            else:
                ptype = random.choice(["gas_giant", "ice"])
                disp = 0.02 if ptype == "gas_giant" else 0.04

            planet = Planet(
                f"Planeta {i+1}", radius, orbit_radius, orbit_speed,
                color_type=ptype, orbit_tilt=orbit_tilt,
                rotation_speed=rotation_speed, seed=planet_seed,
                displacement=disp
            )
            planet.generate_mesh()

            num_moons = random.randint(0, 3) if ptype != "gas_giant" else random.randint(1, 5)
            for j in range(num_moons):
                moon_seed = planet_seed + j * 50
                moon_radius = radius * random.uniform(0.15, 0.35)
                moon_orbit = radius * 2 + j * 2 + random.uniform(1, 3)
                moon_speed = random.uniform(0.5, 2.0) / (moon_orbit * 0.1)

                moon_types = ["moon", "icy_moon", "volcanic_moon"]
                mtype = random.choice(moon_types)

                moon = Satellite(
                    f"Lua {j+1}", moon_radius, moon_orbit, moon_speed,
                    color_type=mtype, seed=moon_seed
                )
                moon.generate_mesh()
                planet.add_satellite(moon)

            self.planets.append(planet)

    def update(self, dt):
        self.star.update(dt)
        for planet in self.planets:
            planet.update(dt, self.star.position)

    def draw(self, planet_shader, star_shader, orbit_shader, view, projection):
        for planet in self.planets:
            planet.draw_orbits(orbit_shader, view, projection, self.star.position)

        glUseProgram(star_shader)
        self.star.draw(star_shader, view, projection)

        glUseProgram(planet_shader)
        for planet in self.planets:
            planet.draw(planet_shader, view, projection, self.star.position)


# ================================================================================
# CAMERA / NAVE
# ================================================================================

class SpaceShip:
    def __init__(self, position=(0, 5, 30)):
        self.position = glm.vec3(position)
        self.angle_x = 0.0
        self.angle_y = 0.0
        self.velocity = glm.vec3(0.0)
        self.speed = 15.0
        self.engines_on = False
        self.max_angle = math.pi / 2.0 - 0.01

    def get_forward(self):
        forward = glm.vec3(
            math.sin(self.angle_y) * math.cos(self.angle_x),
            math.sin(self.angle_x),
            -math.cos(self.angle_y) * math.cos(self.angle_x)
        )
        return glm.normalize(forward)

    def get_up(self):
        forward = self.get_forward()
        right = glm.normalize(glm.cross(forward, glm.vec3(0, 1, 0)))
        return glm.normalize(glm.cross(right, forward))

    def update(self, dt, keys):
        angular_speed = 1.5 * dt

        if keys['w']:
            self.angle_x += angular_speed
        if keys['s']:
            self.angle_x -= angular_speed
        if keys['a']:
            self.angle_y += angular_speed
        if keys['d']:
            self.angle_y -= angular_speed

        self.angle_x = max(-self.max_angle, min(self.max_angle, self.angle_x))

        if self.engines_on:
            forward = self.get_forward()
            self.velocity = forward * self.speed
        else:
            self.velocity *= 0.98

        self.position += self.velocity * dt

    def get_view_matrix(self):
        forward = self.get_forward()
        target = self.position + forward
        up = self.get_up()
        return glm.lookAt(self.position, target, up)


# ================================================================================
# JOGO PRINCIPAL
# ================================================================================

class SpaceGame:
    def __init__(self):
        self.window = None
        self.width = 1280
        self.height = 720

        self.planet_shader = None
        self.star_shader = None
        self.orbit_shader = None
        self.sky_shader = None

        self.ship = SpaceShip()
        self.systems = []
        self.keys = {'w': False, 's': False, 'a': False, 'd': False}

        self.sky_vao = None
        self.sky_vbo = None

        self.last_time = 0.0
        self.fps = 0
        self.frame_count = 0
        self.fps_time = 0

    def init_glfw(self):
        if not glfw.init():
            print("Falha ao inicializar GLFW!")
            return False

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

        self.window = glfw.create_window(self.width, self.height,
            "Exploracao Espacial 3D - O=Motor ON | P=Motor OFF | WASD=Direcao | ESC=Sair",
            None, None)

        if not self.window:
            glfw.terminate()
            print("Falha ao criar janela!")
            return False

        glfw.make_context_current(self.window)
        glfw.set_key_callback(self.window, self.key_callback)
        glfw.set_framebuffer_size_callback(self.window, self.resize_callback)
        glfw.set_input_mode(self.window, glfw.CURSOR, glfw.CURSOR_DISABLED)

        return True

    def init_shaders(self):
        try:
            self.planet_shader = compileProgram(
                compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
                compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
            )

            self.star_shader = compileProgram(
                compileShader(STAR_VERTEX_SHADER, GL_VERTEX_SHADER),
                compileShader(STAR_FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
            )

            self.orbit_shader = compileProgram(
                compileShader(ORBIT_VERTEX_SHADER, GL_VERTEX_SHADER),
                compileShader(ORBIT_FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
            )

            self.sky_shader = compileProgram(
                compileShader(SKY_VERTEX_SHADER, GL_VERTEX_SHADER),
                compileShader(SKY_FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
            )

            print("Shaders compilados com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao compilar shaders: {e}")
            return False

    def init_skybox(self):
        sky_verts = create_skybox()

        self.sky_vao = glGenVertexArrays(1)
        self.sky_vbo = glGenBuffers(1)

        glBindVertexArray(self.sky_vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.sky_vbo)
        glBufferData(GL_ARRAY_BUFFER, sky_verts.nbytes, sky_verts, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        glBindVertexArray(0)

    def generate_universe(self):
        print("Gerando universo...")

        system1 = StarSystem("Sistema Solar", (0, 0, 0), seed=42)
        self.systems.append(system1)

        system2 = StarSystem("Sistema Alpha", (200, 30, -150), seed=123)
        self.systems.append(system2)

        system3 = StarSystem("Sistema Beta", (-180, -20, 200), seed=456)
        self.systems.append(system3)

        system4 = StarSystem("Sistema Gamma", (300, 50, 300), seed=789)
        self.systems.append(system4)

        system5 = StarSystem("Sistema Delta", (-250, -40, -200), seed=999)
        self.systems.append(system5)

        print(f"Universo gerado com {len(self.systems)} sistemas estelares!")
        for sys in self.systems:
            print(f"  - {sys.name}: {len(sys.planets)} planetas")

    def key_callback(self, window, key, scancode, action, mods):
        if action == glfw.PRESS:
            if key == glfw.KEY_ESCAPE:
                glfw.set_window_should_close(window, True)
            elif key == glfw.KEY_O:
                self.ship.engines_on = True
                print("Motores LIGADOS!")
            elif key == glfw.KEY_P:
                self.ship.engines_on = False
                print("Motores DESLIGADOS!")
            elif key == glfw.KEY_W:
                self.keys['w'] = True
            elif key == glfw.KEY_S:
                self.keys['s'] = True
            elif key == glfw.KEY_A:
                self.keys['a'] = True
            elif key == glfw.KEY_D:
                self.keys['d'] = True
            elif key == glfw.KEY_1:
                self.ship.position = glm.vec3(0, 5, 30)
                print("Teleportado para Sistema Solar")
            elif key == glfw.KEY_2:
                self.ship.position = glm.vec3(200, 30, -150)
                print("Teleportado para Sistema Alpha")
            elif key == glfw.KEY_3:
                self.ship.position = glm.vec3(-180, -20, 200)
                print("Teleportado para Sistema Beta")
            elif key == glfw.KEY_4:
                self.ship.position = glm.vec3(300, 50, 300)
                print("Teleportado para Sistema Gamma")
            elif key == glfw.KEY_5:
                self.ship.position = glm.vec3(-250, -40, -200)
                print("Teleportado para Sistema Delta")

        elif action == glfw.RELEASE:
            if key == glfw.KEY_W:
                self.keys['w'] = False
            elif key == glfw.KEY_S:
                self.keys['s'] = False
            elif key == glfw.KEY_A:
                self.keys['a'] = False
            elif key == glfw.KEY_D:
                self.keys['d'] = False

    def resize_callback(self, window, width, height):
        self.width = width
        self.height = height
        glViewport(0, 0, width, height)

    def draw_skybox(self, view, projection):
        glDepthFunc(GL_LEQUAL)
        glUseProgram(self.sky_shader)

        sky_view = glm.mat4(glm.mat3(view))

        glUniformMatrix4fv(glGetUniformLocation(self.sky_shader, "view"), 1, GL_FALSE, glm.value_ptr(sky_view))
        glUniformMatrix4fv(glGetUniformLocation(self.sky_shader, "projection"), 1, GL_FALSE, glm.value_ptr(projection))

        glBindVertexArray(self.sky_vao)
        glDrawArrays(GL_TRIANGLES, 0, 36)
        glBindVertexArray(0)
        glDepthFunc(GL_LESS)

    def render_hud(self):
        closest_system = None
        closest_dist = float('inf')
        for sys in self.systems:
            dist = glm.distance(self.ship.position, sys.position)
            if dist < closest_dist:
                closest_dist = dist
                closest_system = sys

        closest_planet = None
        closest_planet_dist = float('inf')
        if closest_system:
            for planet in closest_system.planets:
                dist = glm.distance(self.ship.position, planet.position)
                if dist < closest_planet_dist:
                    closest_planet_dist = dist
                    closest_planet = planet

        status = "LIGADO" if self.ship.engines_on else "DESLIGADO"

        print(f"\r{'='*80}", end="")
        print(f"\r  EXPLORACAO ESPACIAL 3D  |  FPS: {self.fps}  |  Motores: {status}", end="")
        print(f"\n  Posicao: ({self.ship.position.x:.1f}, {self.ship.position.y:.1f}, {self.ship.position.z:.1f})")
        print(f"  Angulos: Pitch={math.degrees(self.ship.angle_x):.1f}  Yaw={math.degrees(self.ship.angle_y):.1f}")
        if closest_system:
            print(f"  Sistema mais proximo: {closest_system.name} ({closest_dist:.1f} UA)")
        if closest_planet:
            print(f"  Planeta mais proximo: {closest_planet.name} ({closest_planet_dist:.1f} UA)")
        print(f"  [1-5] Teletransporte  |  [O] Motor ON  |  [P] Motor OFF  |  [ESC] Sair")
        try:
            sys.stdout.write("\033[F" * 7)
            sys.stdout.flush()
        except:
            print('não é erro meu')

    def run(self):
        if not self.init_glfw():
            return

        if not self.init_shaders():
            return

        self.init_skybox()
        self.generate_universe()

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glClearColor(0.0, 0.0, 0.0, 1.0)

        self.last_time = glfw.get_time()

        print("\n" * 8)

        while not glfw.window_should_close(self.window):
            current_time = glfw.get_time()
            dt = current_time - self.last_time
            self.last_time = current_time

            self.frame_count += 1
            if current_time - self.fps_time >= 1.0:
                self.fps = self.frame_count
                self.frame_count = 0
                self.fps_time = current_time

            self.ship.update(dt, self.keys)
            for system in self.systems:
                system.update(dt)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            view = self.ship.get_view_matrix()
            projection = glm.perspective(glm.radians(60.0), self.width / self.height, 0.1, 2000.0)

            self.draw_skybox(view, projection)

            for system in self.systems:
                system.draw(self.planet_shader, self.star_shader, self.orbit_shader, view, projection)

            glfw.swap_buffers(self.window)
            glfw.poll_events()

            if self.frame_count % 10 == 0:
                self.render_hud()

        sys.stdout.write("\n" * 7)
        print("\nObrigado por explorar o universo!")
        glfw.terminate()


# ================================================================================
# MAIN
# ================================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("  EXPLORACAO ESPACIAL 3D  (SEM DEPENDENCIA DE NOISE)")
    print("=" * 80)
    print("  Controles:")
    print("    W / S  ->  Alterar angulo do eixo X (Pitch)")
    print("    A / D  ->  Alterar angulo do eixo Y (Yaw)")
    print("    O      ->  Ligar motores")
    print("    P      ->  Desligar motores")
    print("    1-5    ->  Teletransportar para sistemas")
    print("    ESC    ->  Sair")
    print("=" * 80)
    print("\nIniciando...")

    game = SpaceGame()
    game.run()