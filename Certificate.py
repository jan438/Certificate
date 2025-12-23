import os
import sys
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color, red, blue, yellow, green, white, HexColor
from reportlab.lib.units import mm, cm

def drawBGRect(c, x, y, w, h):    
    c.saveState()
    p = c.beginPath()
    p.rect(0, 0, width, height)
    c.clipPath(p, stroke=0)
    c.linearGradient(x, y, width, height,(Color(0.9, 0.95, 1), Color(0.7, 0.85, 1)), (0, 1))
    c.restoreState()

if sys.platform[0] == 'l':
    path = '/home/jan/git/Certificate'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Certificate"
os.chdir(path)
c = Canvas("PDF/Certificate.pdf", pagesize=letter)
width, height = letter
drawBGRect(c, 0, 0, width, height)
c.save()  

key = input("Wait")
