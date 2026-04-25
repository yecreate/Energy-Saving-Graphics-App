import sys
from OpenGL.GL import *
from OpenGL.GLUT import *

light_on = True

def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(font, ord(char))

def draw_room():
    """Draws a simple house/room outline"""
    glLineWidth(3)
    if light_on:
        glColor3f(0.4, 0.4, 0.4) 
    else:
        glColor3f(0.7, 0.7, 0.7)
    
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.5, -0.4) # Bottom Left
    glVertex2f(0.5, -0.4)  # Bottom Right
    glVertex2f(0.5, 0.7)   # Top Right
    glVertex2f(0.0, 0.9)   # Roof Peak
    glVertex2f(-0.5, 0.7)  # Top Left
    glEnd()

def draw_bulb():
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.7)
    glVertex2f(0.0, 0.5)
    glEnd()
    
    if light_on:
        glColor3f(1.0, 0.9, 0.0) 
    else:
        glColor3f(0.2, 0.2, 0.2) 
        
    glBegin(GL_POLYGON)
    for i in range(360):
        import math
        theta = i * math.pi / 180
        glVertex2f(0.1 * math.cos(theta), 0.5 + 0.1 * math.sin(theta))
    glEnd()

def draw_ui():
    """Draws the labels, the energy meter, and control instructions"""
    # 1. Header Info (Student Details)
    glColor3f(0.5, 0.5, 0.5)
    draw_text(-0.95, 0.9, "Youssef Sameh Ahmed | 24030126", GLUT_BITMAP_HELVETICA_12)
    draw_text(-0.95, 0.85, "FCIT - Level 2 - Innovation University", GLUT_BITMAP_HELVETICA_12)

    # 2. Control Instructions
    if light_on:
        glColor3f(0.2, 0.2, 0.2) # Dark text for light background
    else:
        glColor3f(0.8, 0.8, 0.8) # Light text for dark background
    draw_text(-0.95, 0.75, "CONTROLS:", GLUT_BITMAP_HELVETICA_12)
    draw_text(-0.95, 0.70, "[S] - Save Energy", GLUT_BITMAP_HELVETICA_12)
    draw_text(-0.95, 0.65, "[L] - Toggle Light", GLUT_BITMAP_HELVETICA_12)

    # 3. Energy Meter Label
    glColor3f(0.5, 0.5, 0.5)
    draw_text(-0.75, -0.65, "ENERGY CONSUMPTION", GLUT_BITMAP_HELVETICA_12)
    
    # 4. Meter Background
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(-0.8, -0.7)
    glVertex2f(0.8, -0.7)
    glVertex2f(0.8, -0.8)
    glVertex2f(-0.8, -0.8)
    glEnd()

    # 5. Meter Fill & Campaign Slogan
    if light_on:
        glColor3f(1.0, 0.2, 0.2) # Red
        fill = 0.75
        draw_text(-0.25, -0.92, "WASTING ELECTRICITY!", GLUT_BITMAP_HELVETICA_18)
    else:
        glColor3f(0.2, 1.0, 0.2) # Green
        fill = 0.15
        draw_text(-0.35, -0.92, "حملة وفرها ونورها - Wafarha w Nawarha", GLUT_BITMAP_HELVETICA_18)

    glBegin(GL_QUADS)
    glVertex2f(-0.8, -0.7)
    glVertex2f(-0.8 + (fill * 1.6), -0.7)
    glVertex2f(-0.8 + (fill * 1.6), -0.8)
    glVertex2f(-0.8, -0.8)
    glEnd()

def keyboard(key, x, y):
    global light_on
    # Convert input to lowercase string
    input_key = key.decode().lower()
    
    # Check for S, L, or Space
    if input_key in ['s', 'l', ' ']:
        light_on = not light_on
        
    # Redraw the screen
    glutPostRedisplay()

def display():
    if light_on:
        glClearColor(0.95, 0.95, 1.0, 1.0) # Soft blue-white
    else:
        glClearColor(0.05, 0.05, 0.1, 1.0) # Midnight blue
    
    glClear(GL_COLOR_BUFFER_BIT)
    
    draw_room()
    draw_bulb()
    draw_ui()
    
    # Creative Slogan Text
    if not light_on:
        glColor3f(1.0, 1.0, 1.0)
        draw_text(-0.2, 0.1, "Save it and Light it up!")
    
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(900, 700)
    glutCreateWindow(b"Assignment 9 - Energy Awareness Application")
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    print("Application Ready. Press 'S' or 'SPACE' to toggle light.")
    glutMainLoop()

main()